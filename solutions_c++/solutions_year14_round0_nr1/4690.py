#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
#define rep(i,n) for(int i=1;i<=n;++i)
using namespace std;
int n,m;
int T;
int s[5][5];
int x[17],y[17];
int main()
{
  //  freopen("A.in","r",stdin);
  //  freopen("A.out","w",stdout);
    
    scanf("%d",&T);
    for(int ii=1;ii<=T;++ii)
    {
		scanf("%d",&n);
		rep(i,4)rep(j,4)
		{
			int z;
			scanf("%d",&z);
			x[z]=i;
			s[i][j]=-1;
		}
		scanf("%d",&m);
		rep(i,4)rep(j,4)
		{
			int z;
			scanf("%d",&z);
			y[z]=i;
			if(s[x[z]][y[z]]<0)s[x[z]][y[z]]=z;
			else s[x[z]][y[z]]=0;
		}		
		if(s[n][m]>0)printf("Case #%d: %d\n",ii,s[n][m]);else
			if(s[n][m]==0)printf("Case #%d: Bad magician!\n",ii);
				else printf("Case #%d: Volunteer cheated!\n",ii);
	}
	return 0;
}
 