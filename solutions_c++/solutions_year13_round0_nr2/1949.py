#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#define mod 1000000007
using namespace std;

bool mark[110],flash;
int t,w,v,i,s,q,a[110][110],n,m,g,h,j,k;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;v=w;
	while(w--)
	{
		cin>>n>>m;
		for(i=1;i<=100;i++)
		{
			mark[i]=0;
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				cin>>a[i][j];
				mark[a[i][j]]=1;
			}
		}
		for(k=1;k<=100;k++)
		{
			if(mark[k]==1)
			{
				for(i=1;i<=n;i++)
				{
					for(j=1;j<=m;j++)
					{
						if(a[i][j]==k)
						{
							flash=1;
							q=0;
							for(g=1;g<=m;g++)
							{
								if(a[i][g]==k || a[i][g]==0)
								{
									q++;
								}
								else
								{
									break;
								}
							}
							if(q==m)
							{
								flash=0;
								for(g=1;g<=m;g++)
								{
									a[i][g]=0;
								}
							}
							q=0;
							for(g=1;g<=n;g++)
							{
								if(a[g][j]==k || a[g][j]==0)
								{
									q++;
								}
								else
								{
									break;
								}
							}
							if(q==n)
							{
								flash=0;
								for(g=1;g<=n;g++)
								{
									a[g][j]=0;
								}
							}
							if(flash==1)
							{
								cout<<"Case #"<<v-w<<": NO"<<endl;
								goto cikl;
							}
						}
					}
				}
			}
		}
		cout<<"Case #"<<v-w<<": YES"<<endl;
cikl:;
	}
	return 0;
}