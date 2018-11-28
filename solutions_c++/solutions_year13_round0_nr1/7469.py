#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

template <class T>
void jacob(int w, int typ, T eps, int norma)
{
	printf("\nWyniki dla wymiaru %i ", w);
	if(typ==1)
		printf("(float)\n\n");
	else if(typ==2)
		printf("(double)\n\n");
	else
		printf("(long double)\n\n");
		
	int wym = w;
	
	T** matrix = new T*[wym+1];
	for(int i=1; i<=wym; ++i)
		matrix[i] = new T[wym+1];
		
	T* wynik = new T[wym+1];

	for(int i=1; i<=wym; ++i)
	{
		for(int j=1; j<=wym; ++j)
		{
			if(j==i)
				matrix[i][j] = T(6.0);
			else
				matrix[i][j] = T(0.5)/T(T(wym)-T(i)-T(j)+T(1.5));
		}
	}
	
	T* iks = new T[wym+1];

	for(int i=1; i<=wym; ++i)
	{
	    if(i%4 == 0)
	       iks[i] = T(-1.0);
	    else
	      iks[i] = T(1.0);
	}

	for(int i=1; i<=wym; ++i)
	{
	    wynik[i] = 0.0;
		for(int j=1; j<=wym; ++j)
		{
		    wynik[i] += matrix[i][j]*iks[j];
		}
	}
	
	T** M = new T*[wym+1];
	for(int i=1; i<=wym; ++i)
		M[i] = new T[wym+1];
		
	for(int i=1; i<=wym; ++i)
	{
		for(int j=1; j<=wym; ++j)
		{
			M[i][j] = matrix[i][j];    
		}
	}
	
	T* ww = new T[wym+1];
	T* wek = new T[wym+1];
	
	for(int i=1; i<=wym; ++i)
	{
		wek[i] = T(0.0);
		ww[i] = T(1.0);
	}
		
	for(int i=1; i<=wym; ++i)
	{
		for(int j=1; j<=wym; ++j)
		{
		    M[i][j] = matrix[i][j];
		}
	}
	
	T* diag = new T[wym+1];
	
	for(int i = 1; i <= wym; ++i)
	{
		diag[i] = T(1.0)/matrix[i][i];
		matrix[i][i] = T(0.0);
	}
	
	for(int i=1; i<=wym; ++i)
	{
		for(int j=1; j<=wym; ++j)
		{
		   matrix[i][j] = -(diag[i]*matrix[i][j]);
		}
	}
	
	T* it1 = new T[wym+1];
	T* it2 = new T[wym+1];
	
	for(int i = 1; i <= wym; ++i)
	{
		it1[i] = it2[i] = T(0.0);
	}
	
	T blad = 10.0;
	int u = 0;
	
	while(blad > eps)
	{
		++u;
		for(int j=1; j<=wym; ++j)
		{
			it2[j] = diag[j]*wynik[j];
			for(int k=1; k<=wym; ++k)
			{
			   	it2[j] += it1[k]*matrix[j][k];
			}
		}
		
		if(norma == 1)
		{
			blad = T(0.0);
			for(int d = 1; d <= wym; ++d)
			{
				blad += (it2[d]-it1[d])*(it2[d]-it1[d]);
			}
			blad = sqrt(blad);
		}
		else
		{
			blad = T(0.0);
			for(int j=1; j<=wym; ++j)
			{
				for(int k=1; k<=wym; ++k)
				{
				  	blad += it1[k]*M[j][k];
				}
				blad -= wynik[j];
			}
			if(blad < T(0.0))
			  blad *= T(-1.0);
		}
		
		for(int d = 1; d <= wym; ++d)
		{
			it1[d] = it2[d];
		}
	}
	
	T* maks = new T[wym+1];
	
	for(int z = 1; z <= wym; ++z)
	{
		maks[z] = T(-1.0);
	}
	
	for(int z = 0; z < 1000; ++z)
	{
		for(int d = 1; d <= wym; ++d)
		{
			wek[d] = T(0.0);
			for(int k=1; k<=wym; ++k)
			{
				wek[d] += matrix[d][k]*ww[k];
			}
		}
		
		for(int d = 1; d <= wym; ++d)
		{
			if(wek[d] < T(0.0))
			{
				if((-wek[d]) > maks[d])
					maks[d] = (-wek[d]);
			}
			else
			{
				if(wek[d] > maks[d])
					maks[d] = wek[d];
			}
		}
		
		for(int d = 1; d <= wym; ++d)
		{
			ww[d] = wek[d]/maks[d];
		}
	}
	    
    T prom = T(-1.0);
    
    for(int j=1; j<=wym; ++j)
	{
		if(maks[j] > prom)
			prom = maks[j];
	}
	
	for(int i = 1; i <= wym; ++i)
	{
		wynik[i] = it1[i];
	}	

	std::cout << "Epsylon: " << eps << " Blad (norma 1): " << blad << " Liczba iteracji: " << u;

    printf("\n");
    
	T q = 0.0;
	for(int j=1; j<=wym; ++j)
	{
	    q += (wynik[j]-iks[j])*(wynik[j]-iks[j]);
	}

    q = sqrt(q);

	T r = 0.0;
	for(int j=1; j<=wym; ++j)
	{
	    if(wynik[j]-iks[j] > r)
	      r = wynik[j]-iks[j];
	}

    q = sqrt(q);

	std::cout << "Promien spektralny " << prom << std::endl;
    std:: cout << "Norma euklidesowa " << q << std::endl;
    std:: cout << "Norma maksimum " << r << std::endl;

		
	for(int i=1; i<=wym; ++i)
		delete matrix[i];
	for(int i=1; i<=wym; ++i)
		delete M[i];
	delete [] diag;
	delete [] matrix;
	delete [] wynik;
	delete [] iks;
	delete [] it1;
	delete [] it2;
	delete [] ww;
	delete [] wek;
	delete [] maks;
}


int main(int argc, char* args[])
{
	int tryb = 1;
	double blad = 0.0001;
	jacob<float>(7, 1, blad, tryb);
	jacob<double>(7, 2, blad, tryb);
	jacob<long double>(7, 3, blad, tryb);
	jacob<float>(15, 1, blad, tryb);
	jacob<double>(15, 2, blad, tryb);
	jacob<long double>(15, 3, blad, tryb);
	jacob<float>(30, 1, blad, tryb);
	jacob<double>(30, 2, blad, tryb);
	jacob<long double>(30, 3, blad, tryb);
	jacob<float>(100, 1, blad, tryb);
	jacob<double>(100, 2, blad, tryb);
	jacob<long double>(100, 3, blad, tryb);
	jacob<float>(2000, 1, blad, tryb);
	jacob<double>(2000, 2, blad, tryb);
	jacob<long double>(2000, 3, blad, tryb);
	jacob<float>(5000, 1, blad, tryb);
	jacob<double>(5000, 2, blad, tryb);
	jacob<long double>(5000, 3, blad, tryb);
	
	return 0;
}

