#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out1777.out","w",stdout);
	int test;
	cin>>test;
	for(int x=1;x<=test;++x)
	{
		int n,y=0;
		cin>>n;
		int Arr[2*n-1][n];
		for(int pp=0;pp<2*n-1;++pp)
			for(int qq=0;qq<n;++qq)
				cin>>Arr[pp][qq];
		int B[2501]={0};
		for(int rr=0;rr<2*n-1;++rr)
			for(int ss=0;ss<n;++ss)
			{
				B[Arr[rr][ss]]++;
			}
		int out[n];
		for(int i=1;i<2501;++i)	
		{
			if(B[i]%2)
				out[y++]=i;
		}
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<n;++i)
			cout<<out[i]<<" ";
		cout<<endl;			
	}
}
