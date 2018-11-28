#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
    freopen("outsmallyesyes.out","w",stdout);
	int test;
	cin>>test;
	for(int x=1;x<=test;++x)
	{
		int N;
		cin>>N;
		int A[2*N-1][N];
		for(int j=0;j<2*N-1;++j)
			for(int k=0;k<N;++k)
				cin>>A[j][k];
		int P[2501]={0};
		for(int i=0;i<2*N-1;++i)
			for(int j=0;j<N;++j)
			{
				P[A[i][j]]++;
			}
		int C[N];
		int y=0;
		for(int i=1;i<2501;++i)	
		{
			if(P[i]%2)
				C[y++]=i;
		}
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<N;++i)
			cout<<C[i]<<" ";
		cout<<endl;			
	}
}
