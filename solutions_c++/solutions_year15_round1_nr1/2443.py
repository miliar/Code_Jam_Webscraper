#include<bits/stdc++.h>
using namespace std;
typedef long long int longx;
int main()
{
	longx T,N,res1,res2,a[100001];
	cin>>T;
	for(longx j=1;j<=T;j++)
	{
		cin>>N;
		for(longx i=0;i<N;i++)
			cin>>a[i];
		res1=res2=0;
		longx m=0;
		for(longx i=0;i<N-1;i++)
		{
			if(a[i]>a[i+1])
				res1+=a[i]-a[i+1];
			m=max(m,a[i]-a[i+1]);
		}
		for(longx i=0;i<N-1;i++)
		{
			if(a[i]>=m)
				res2+=m;
			else
				res2+=a[i];
		}
		cout<<"Case #"<<j<<": "<<res1<<" "<<res2<<endl;
	}
}