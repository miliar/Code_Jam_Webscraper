#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("outlarge.out","w",stdout);
	int t;
	cin>>t;
	for(int x=1;x<=t;++x)
	{
		int n;
		cin>>n;
		int A[2*n-1][n];
		for(int i=0;i<2*n-1;++i)
			for(int j=0;j<n;++j)
				cin>>A[i][j];
		int B[2501]={0};
		for(int i=0;i<2*n-1;++i)
			for(int j=0;j<n;++j)
			{
				B[A[i][j]]++;
			}
		int C[n];
		int y=0;
		for(int i=1;i<2501;++i)	
		{
			if(B[i]%2)
				C[y++]=i;
		}
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<n;++i)
			cout<<C[i]<<" ";
		cout<<endl;			
	}
}


