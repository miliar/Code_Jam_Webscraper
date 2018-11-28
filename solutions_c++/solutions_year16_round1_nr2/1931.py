#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out90.out","w",stdout);
	int t;
	cin>>t;
	for(int z=0;z<t;z++)
	{
		int m;
		cin>>m;
		int a[2*m-1][m];
		for(int i=0;i<2*m-1;++i)
			for(int j=0;j<m;++j)
				cin>>a[i][j];
		int b[2501]={0};
		for(int i=0;i<2*m-1;++i)
			for(int j=0;j<m;++j)
			{
				b[a[i][j]]++;
			}
		int c[m];
		int v=0;
		for(int i=1;i<2501;++i)	
		{
			if(b[i]%2)
				c[v++]=i;
		}
		cout<<"Case #"<<z+1<<": ";
		for(int i=0;i<m;++i)
			cout<<c[i]<<" ";
		cout<<endl;			
	}
}
