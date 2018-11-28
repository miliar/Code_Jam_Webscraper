#include <iostream>
#include <stdio.h>
using namespace std;
long long is_par(long long n)
{
	int cnt=0;
	int a[20];
	while(n)
	{
		cnt++;
		a[cnt]=n%10;
		n/=10; 
	}
	int i;
	for(i=1;i<=cnt;i++)
	{
		if(a[i]!=a[1+cnt-i]) return false; 
	} 
	return true; 
} 
long long M[100000]; 
int N=0; 
int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,cas=0;
	long long i,j;
	for(i=1;i<=10000000;i++)
	{
		if(is_par(i)==false) continue;
		if(is_par(i*i)==false) continue; 
		N++;
		M[N]=i*i; 
	} 
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		printf("Case #%d: ",cas);
		long long A,B;
		cin>>A>>B;
		int ans=0;
		for(i=1;i<=N;i++)
		{
			if(M[i]>=A && M[i]<=B) ans++; 
		} 
		cout<<ans<<endl; 
	}
	return 0;
} 
