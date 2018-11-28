#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
#define M 0x7ffffff
int map[105][105];
int flag;
int t,cnt=0,n,m;
void check(int x,int y,int p)
{
	int a=0,b=0;
	for(int i=1;i<=n;i++)
		if(map[i][y]>p)
		{
			a=1;break;
		}
	for(int i=1;i<=m;i++)
		if(map[x][i]>p)
		{
			b=1;break;
			
		}
	if(a==1&&b==1)
		flag=1;
	return;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++)
    {
        memset(map,0,sizeof(map));
		scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                scanf("%d",&map[i][j]);

            }
        flag=0;
        for(int i=1;i<=n;i++)
        {
			for(int j=1;j<=m;j++)
            {
                
				   check(i,j,map[i][j]);
				   if(flag==1)
					   	break;
				
			}
			if(flag==1)
				break;
		}
        
        printf("Case #%d: ",cnt);

        if(flag==1)
            printf("NO\n");
        
        else printf("YES\n");
    }
    return 0;
}
