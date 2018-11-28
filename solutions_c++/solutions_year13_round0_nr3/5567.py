#include<iostream>
#include<fstream>
#include<math.h>
#include<time.h>
#include<stdlib.h>

using namespace std;
int getFairAndSquare(int a,int b);
int getFairAndSquare(long long a,long long b);
bool isPalindrome(long long i);

const int size=101;
int main()
{
	const long long maxB=100000000000000;
	ofstream f("out.txt");
	int i=0,t,s;
	long long a,b,*out;
	cin>>t;
	out=new long long[t];
	srand(time(NULL));
	clock_t startTime=clock();
	while(i<t)
	{
		cin>>a>>b;
		//b=rand()%maxB+1;
		//a=rand()%100+1;
		//cin<<"a = "<<a<<"b = "<<b<<"\n";
		out[i]=getFairAndSquare(a,b);
		i++;
	}
	for(i=0;i<t;i++)
	{
		f<<"Case #"<<i+1<<": "<<out[i]<<"\n";
	}
	cout<<"time of execution : "<<((double)(clock()-startTime)/(double)(CLOCKS_PER_SEC))<<"\n";
	delete [] out;
	f.close();
	return 0;
}

int getFairAndSquare(long long a,long long b)
{
	int count=0;
	long long sqra=sqrt(a);
	long long sqrb=sqrt(b);
	long long i;
	if((sqra*sqra)==a)
	{
		i=sqra;
	} 
    else
    {
   		i=sqra+1;
    }

	for(;i<=sqrb;i++)
	{
		if(isPalindrome(i))
		{
			long long sqr=(i*i);
			if(isPalindrome(sqr))
			{
				count++;
			}
		}
	}
	return count;
}

bool isPalindrome(long long i)
{
	int a[size],k=0;
	while(i>0)
	{
		a[k++]=(i%10);
		i/=10;
	}
	for(int j=0;j<(k/2);j++)
	{
		if(a[j]!=a[k-j-1])
		{
			return false;
		}
	}
	return true;
}
