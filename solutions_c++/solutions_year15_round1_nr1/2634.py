#include <bits/stdc++.h>
using namespace std;
long long int N;
long long int minisum(long long int A[])
{

	long long int sum=0;
	for(int i=0;i<N-1;i++)
	{
		if(A[i+1]<A[i])
		{
			sum+=(A[i]-A[i+1]);
		}
	}
	return sum;
}

long long int maxisum(long long int A[])
{

	long long int maxdiff=0,sum=0;
	for(int i=0;i<N-1;i++)
	{
		maxdiff=max(maxdiff,(A[i]-A[i+1]));
	}
	for(int i=0;i<N-1;i++)
	{
		if(A[i]<=maxdiff)
		sum+=A[i];
		else
		sum+=(maxdiff);
	}
	return sum;
}
int main() {
	long long int minsum,maxsum,A[10000],T,x,y;
	cin>>T;
	for(int k=0;k<T;k++)
	{
	cin>>N;
	for(int i=0;i<N;i++)
	{
		cin>>A[i];
	}

	x=minisum(A);
	y=maxisum(A);
	cout<<"Case #"<<k+1<<": "<<x<<" "<<y<<endl;
	}
	// your code goes here
	return 0;
}