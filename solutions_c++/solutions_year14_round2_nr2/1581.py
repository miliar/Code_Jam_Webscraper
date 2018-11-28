#include <iostream>
#include <cstdlib>
#include <string>
#include <cmath>
#define N 1001

using namespace std;

int a[N][N];



int main()
{
	int i,j,k;
	int A,B,K,T,S;
	long long int sum;

	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			a[i][j]=i&j;
		}
	}
	cin>>S;
	T=S;
	while(S--)
	{
		cin>>A>>B>>K;
		for(i=0,sum=0;i<A;i++)
		{
			for(j=0;j<B;j++)
			{
				if(a[i][j]<K)
					sum++;
			}
		}
		cout<<"Case #"<<T-S<<": ";
		cout<<sum<<endl;

	}
	return 0;
}