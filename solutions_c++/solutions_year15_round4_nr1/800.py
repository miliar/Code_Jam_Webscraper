#include <iostream>
#include<cstdio>
using namespace std;
char s[110][110];
int a[110][110];
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.txt","w",stdout);
	
	int t,r,c,ch,U,L,D,R,IMPOSSIBLE,cc;
	cin >> t;
	for(int aa=0;aa<t;aa++)
	{
		cc=0;
		IMPOSSIBLE = 0;
		cin >> r >> c;
		for(int i=0;i<r;i++)
		{
			scanf("%s",s[i]);
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='.') a[i][j]=1;
				else a[i][j]=0;
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				ch=0,U=0,L=0,D=0,R=0;
				if(a[i][j]==1)
				{
					for(int k=0;k<i;k++)
					{
						if(a[k][j]==1)
						{
							U=1;
							break;
						}
					}
					for(int k=i+1;k<r;k++)
					{
						if(a[k][j]==1)
						{
							D=1;
							break;
						}											}	
					for(int k=0;k<j;k++)
					{
						if(a[i][k]==1)
						{
							L=1;
							break;
						}
					}
					for(int k=j+1;k<c;k++)
					{
						if(a[i][k]==1)
						{
							R=1;
							break;
						}
					}
					if(L+R+D+U==0)
					{
						IMPOSSIBLE = 1;
					}
					else
					{
						if(L==0 and s[i][j]=='<') cc++;
						if(R==0 and s[i][j]=='>') cc++;
						if(U==0 and s[i][j]=='^') cc++;
						if(D==0 and s[i][j]=='v') cc++;
					}
					
				}
			}
		}
		cout << "Case #" << aa+1 << ": " ;
		
		if(IMPOSSIBLE == 1) cout << "IMPOSSIBLE" << endl;
		else cout << cc << endl;
		
		
	}
}