#pragma comment(linker,"/STACK:102400000,102400000")
#include <algorithm>
#include <iostream>
#include <fstream>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define sf scanf
#define pf printf
#define fst first
#define scd second
#define pb push_back
#define mkp make_pair
#define cls(a,x) memset(a,x,sizeof a)
#define dt(x) cout<<#x<<"="<<x<<" ";
#define dte(x) cout<<#x<<"="<<x<<endl;



int g[55][55];
int main()
{
	int t,i,j,tt=0;
	int r,c,m;
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
			scanf("%d%d%d",&r,&c,&m);
			int n=r*c-m;
			printf("Case #%d:\n",++tt);
			if(r==1)
			{
					printf("c");
					for(i=1;i<n;i++)
					printf(".");
					for(i=0;i<m;i++)
					printf("*");
					puts("");
			}
			else if(c==1)
			{
					printf("c\n");
					for(i=1;i<n;i++)
					printf(".\n");
					for(i=0;i<m;i++)
					printf("*\n");
			}
			else if(n==1)
			{
					printf("c");
					for(i=1;i<c;i++)
					printf("*");
					puts("");
					for(i=1;i<r;i++)
					{
							for(j=0;j<c;j++)
							printf("*");
							puts("");
					}
			}
			else
			{
					memset(g,0,sizeof g);
					int biao=1;
					for(i=2;i<=r;i++)
					{
							if(n/i>1&&n%i!=1&&(n/i<c||n%i==0&&n/i<=c))
							{
									//printf("123:%d\n",i);
									biao=0;
									for(j=0;j<i;j++)
									for(int k=0;k<n/i;k++)
									g[j][k]=1;
									for(j=0;j<n%i;j++)
									g[j][n/i]=1;
									break;
							}
					}
					if(biao)
					for(i=2;i<=c;i++)
					{
							if(n/i>1&&n%i!=1&&(n/i<r||n%i==0&&n/i<=r))
							{
									biao=0;
									for(j=0;j<i;j++)
									for(int k=0;k<n/i;k++)
									g[k][j]=1;
									for(j=0;j<n%i;j++)
									g[n/i][j]=1;
									break;
							}
					}
					if(biao)
					{
							int bia=0;
							int  qwe=sqrt(m);
							if(qwe*qwe==m)
							{
									if(qwe<r-1&&qwe<c-1)
									{
											for(i=0;i<qwe;i++)
													for(j=0;j<qwe;j++)
													{
															g[r-1-i][c-1-j]=1;
													}
											bia=1;
									}
							}
							else  if(qwe*(qwe+1)>=m)
							{
									if(qwe<r-1&&(qwe+1)<c-1)
									{
											for(i=0;i<qwe;i++)
											for(j=0;j<qwe;j++)
											g[r-1-i][c-1-j]=1;
											for(i=0;i<(m-qwe*qwe);i++)
											g[r-1-i][c-1-qwe]=1;
											bia=1;
									}
									else if((qwe+1)<r-1&&qwe<c-1)
									{
											for(i=0;i<qwe;i++)
											for(j=0;j<qwe;j++)
											g[r-1-i][c-1-j]=1;
											for(i=0;i<(m-qwe*qwe);i++)
											g[r-1-qwe][c-1-i]=1;
											bia=1;
									}
							}
							else {
									if((qwe+1)<r-1&&(qwe+1)<c-1)
									{
											int su=m;
											for(i=0;i<qwe+1;i++){
													if(su==0) break;
													for(j=0;j<qwe+1;j++)
													{
															g[r-1-i][c-1-j]=1;
															su--;
															if(su==0) break;
													}
											}
											bia=1;
									}
							}
							if(bia)
							{
									g[0][0]=-1;
									for(i=0;i<r;i++)
									{
											for(j=0;j<c;j++)
											if(g[i][j]==-1)
											printf("c");
											else if(g[i][j]==0)
											printf(".");
											else printf("*");
											puts("");
									}
							}
							else puts("Impossible");
					}
					else
					{
							g[0][0]=-1;
							for(i=0;i<r;i++)
							{
									for(j=0;j<c;j++)
									if(g[i][j]==-1)
									printf("c");
									else if(g[i][j]==1)
									printf(".");
									else printf("*");
									puts("");
							}
					}
			}
	}
	return 0;
}
