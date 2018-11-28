#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include <iomanip>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<stack>
#include<cstring>
#include<map>
#include<set>
using namespace std;
#define MOD 1000000007
string s[111];
int x[111];
int y[111];
int main()
{
	int t,T;
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int i,j,k,n,m;
	int re;
	int flag;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		re=0;
		flag=1;
		cin>>n>>m;
		for(i=0;i<n;i++)
			cin>>s[i];
		for(i=0;i<=100;i++)
			x[i]=y[i]=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				if(s[i][j]!='.')
				{
					x[i]++;
					y[j]++;
				}
			}
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				if(s[i][j]=='>')
				{
					for(k=j+1;k<m;k++)
						if(s[i][k]!='.')
							break;
					if(k==m)
					{
						if(x[i]>1||y[j]>1)
							re++;
						else
							flag=0;
					}
				}
				else if(s[i][j]=='<')
				{
					for(k=j-1;k>=0;k--)
						if(s[i][k]!='.')
							break;
					if(k<0)
					{
						if(x[i]>1||y[j]>1)
							re++;
						else
							flag=0;
					}
				}
				else if(s[i][j]=='^')
				{
					for(k=i-1;k>=0;k--)
						if(s[k][j]!='.')
							break;
					if(k<0)
					{
						if(x[i]>1||y[j]>1)
							re++;
						else
							flag=0;
					}
				}
				else if(s[i][j]=='v')
				{
					for(k=i+1;k<n;k++)
						if(s[k][j]!='.')
							break;
					if(k==n)
					{
						if(x[i]>1||y[j]>1)
							re++;
						else
							flag=0;
					}
				}
			}
		if(flag)
			cout<<re<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	//system("pause");
    return 0;
}