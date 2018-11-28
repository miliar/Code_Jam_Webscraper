#include <iostream>
#include <fstream>
#include <cmath>
#include <stdint.h>



using namespace std;

int64_t notPrime(int64_t number)
    {
        if (number < 2) return 0;
        if (number % 2 == 0) return 2;
        int64_t root = (int64_t) sqrt((long double)number);
	int64_t i = 3;
        while (i <= root )
        {
            if (number % i == 0) return i;
	    else i += 2;
        }
        return 0;
    }

int64_t predbase (int64_t number, int n, int base)
  {
	int64_t a =0;
	int64_t b= number;
	for (int i=0; i<n; i++)
	  {
		a+=(b%10)* (int64_t) pow((long double)base, (long double)i);
		b/=10;
	  }
	return a;
  }

bool ttnotprime (int64_t number, int n)
  {
	int64_t x;
	int64_t tab[9];
	for (int i=2; i<11; i++)
	  {
		x=0; 		
		x=notPrime(predbase(number, n, i));
		if (x==0)
	 	  {
			return false;
		  }
		else
		  {
			tab[i-2]=x;	
		  }
	  }
	ofstream fout("output.out",ios::app);
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	fout << number<<" ";
	for (int m=0; m<8; m++)
	  {
		fout << tab[m]<<" ";
	  }
	fout << tab[8]<<endl;
	fout.close();
	return true;	  
  }

int64_t generate(int64_t n, int itteration)
  {
	int64_t start=1+ (int64_t) pow((long double)10, (long double)(n-1));
	int64_t x= itteration;
	int64_t y=0;
	while (x !=0)
	  {
		start+= 10*(x%2)* (int64_t) pow((long double)10, (long double)y);
		x/=2;
		y++;
	  }
	return start;
  }

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out",ios::app);

    //-- check if the files were opened successfully 
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int64_t i, n,j;
    for (i = 0; i < numCase; i++)
    {
        fin >> n;
	fin >>j;
	fout << "Case #" << (i + 1) << ": "<< endl;
	int k=0;
	int g=0;
	int64_t m=0;
	while (k<j)
	{
		m = generate(n,g);
		if (ttnotprime(m,n))
		  {
			k++;
		  }
		g++;
				 
	}
	



        
	
    }
    fin.close();
    fout.close();
    return 0;
}
