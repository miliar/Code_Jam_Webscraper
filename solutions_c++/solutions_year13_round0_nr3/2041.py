#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
long long A,B;
unsigned int Test_Cases;
int Array[20];

void read_test_cases(void);

void Check(unsigned int);
int Fair(long long X);

main()
{
	read_test_cases();
	return 0;
}

void read_test_cases(void)
{
	ifstream fin("A.in");
	fin >> Test_Cases ;
	unsigned int Number_of_iterations;
	for(Number_of_iterations=0;Number_of_iterations<Test_Cases;Number_of_iterations++)
	{
		fin>>A;
		fin>>B;
		Check(Number_of_iterations+1);
	}
}

void Check(unsigned int Case)
{
		long double x;
		long long a,b,Number,i;
		int j;
		int Yes;
		x= sqrt(A);
		a= sqrt(A);
		if(x>a)
		a++;
		b= sqrt(B);
		Number=0;
		for(i=a;i<=b;i++)
		{
			Yes=Fair(i);
			if(Yes==1)
			{
				Yes=Fair(i*i);
				if(Yes==1)	Number++;	
			}
		}
		
		
		cout<<"Case #"<<Case<<": "<<Number<<'\n';
		return;

}		

int Fair(long long X)
{
		int i;
		long long T1,T2;
		
		if(X<10) return 1;

		if(X<100)
		{
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		if(X<1000)
		{
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		if(X<10000)
		{
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}


		
		if(X<100000)
		{
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}
		


		if(X<1000000)
		{
			T1=X/100000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000*T1;
			X=X/10;			
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}
		
		if(X<10000000)
		{
			T1=X/1000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000*T1;
			X=X/10;			
		
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		
		if(X<100000000)
		{
			T1=X/10000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000*T1;
			X=X/10;			
			T1=X/100000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000*T1;
			X=X/10;			
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}
		
		if(X<1000000000)
		{
			T1=X/100000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000*T1;
			X=X/10;			
		
		
			T1=X/1000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000*T1;
			X=X/10;			
		
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}
		
		if(X<10000000000)
		{
			T1=X/1000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000000*T1;
			X=X/10;			
		
		
			T1=X/10000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000*T1;
			X=X/10;			
			T1=X/100000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000*T1;
			X=X/10;			
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		if(X<100000000000)
		{
			T1=X/10000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000000*T1;
			X=X/10;			

			T1=X/100000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000*T1;
			X=X/10;			
		
		
			T1=X/1000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000*T1;
			X=X/10;			
		
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		if(X<1000000000000)
		{
			T1=X/100000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000000*T1;
			X=X/10;			

		
			T1=X/1000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000000*T1;
			X=X/10;			
		
		
			T1=X/10000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000*T1;
			X=X/10;			
			T1=X/100000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000*T1;
			X=X/10;			
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		
		if(X<10000000000000)
		{
			T1=X/1000000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000000000*T1;
			X=X/10;			

		
			T1=X/10000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000000*T1;
			X=X/10;			

			T1=X/100000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000*T1;
			X=X/10;			
		
		
			T1=X/1000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000*T1;
			X=X/10;			
		
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}


		if(X<100000000000000)
		{
			T1=X/10000000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000000000*T1;
			X=X/10;			

		
		T1=X/100000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000000*T1;
			X=X/10;			

		
			T1=X/1000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000000*T1;
			X=X/10;			
		
		
			T1=X/10000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000*T1;
			X=X/10;			
			T1=X/100000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000*T1;
			X=X/10;			
			T1=X/1000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000*T1;
			X=X/10;
			T1=X/10;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}

		if(X<1000000000000000)
		{
			T1=X/100000000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000000000*T1;
			X=X/10;			
		
		
			T1=X/1000000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000000000*T1;
			X=X/10;			

		
			T1=X/10000000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000000000*T1;
			X=X/10;			

			T1=X/100000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-100000000*T1;
			X=X/10;			
		
		
			T1=X/1000000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-1000000*T1;
			X=X/10;			
		
			T1=X/10000;
			T2=X%10;
			if(T1!=T2) return 0;
			X=X-10000*T1;
			X=X/10;
			T1=X/100;
			T2=X%10;
			if(T1!=T2) return 0;
			return 1;
		}


		
}