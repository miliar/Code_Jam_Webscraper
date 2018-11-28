#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
double k[1001],n[1001];
int i,j,kk,nn,t,T,N,win1,win2;
bool func(double a,double b)
{
	return a>b;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>N;
		win1 = win2 = kk = nn =0;
		for(i=0; i<N; i++)	cin>>n[i];
		for(i=0; i<N; i++)	cin>>k[i];
		sort(k,k+N,func);
		sort(n,n+N,func);
		while(kk<N)
		{
			if(k[kk]<n[nn])
				win1++,nn++;
			kk++;
		}
		kk = nn = 0;
		while(nn<N)
		{
			if(k[kk]>n[nn])
				win2++,kk++;
			nn++;
		}

		printf("Case #%d: %d %d\n",t,win1,N-win2);
	}

}