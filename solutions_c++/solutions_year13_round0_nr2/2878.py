#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int  n,m;
		cin>>n>>m;
		int x[n][m];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				cin>>x[i][j];
			}
		}
		bool ex=false;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				bool isok=true;
				for(int k=0;k<n;k++)
				{
					if(x[k][j]>x[i][j]) {isok=false;break;}
				}
				if(isok) continue;
				isok=true;
				for(int k=0;k<m;k++)
				{
					if(x[i][k]>x[i][j]) {isok=false;break;}
				}
				if(!isok) {ex=true;break;}
			}
			if(ex) break;
		}
		if(ex) cout<<"Case #"<<tt<<": NO"<<endl;
		else cout<<"Case #"<<tt<<": YES"<<endl;
	}
	return 0;
}
