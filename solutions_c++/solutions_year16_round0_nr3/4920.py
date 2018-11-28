#include <iostream>
#include <math.h>

using namespace std;

long long int* getnext(long long int *a,long long int N)
{
	for(long long int i = 1;i < N-1;i++)
	{
		if(a[i]==0)
		{
			a[i] = 1;
			return a;
		}
		else
			a[i] = 0;
	}
}

long long int checkprime(long long int t)
{
	for(long long int i = 2; i <= (long long int)sqrt(t); i++)
	{
		if(t%i == 0)
			return i;
	}
	return 0;
}

long long int pow1(long long int a,long long int b)
{
	long long int c = 1;
	for( int i = 1; i <= b;i++)
		c = c * a;
	return c;	
}

int main()
{
	long long int count=1,T,f,x,N,i,J,j,*a = new long long int[32],t;
	cin >> T;
	long long int b[10];
	for (i = 0; i<T ;i++)
		cin >> N >> J;
	for (i = 0; i<N; i++)
		a[i] = 0;
	a[N-1] = 1;
	a[0] = 1;
	for (long long int ld = 0; ld < T;ld++)
	{
		cout << "Case #" <<ld+1 << ":"<< endl;
		while(J!=0)
		{
			a = getnext(a,N);	
			f = 0;
			for( i =2; i <= 10; i++)
			{
				t = 0;
				
				for (j = 0; j<N; j++)
					t = t + a[j]*pow1(i,j);
			
					
				x = checkprime(t);
				
				if(x == 0)
				{
					f = 1;
					break;
				}
				else
					b[i] = x;
			}
			if(f == 0)
			{
				cout << t;
				for( i =2; i <= 10 ; i++)
					cout << " " << b[i];
				cout << endl;	
				J--;
			}
		}
	}
	return 0;
}
