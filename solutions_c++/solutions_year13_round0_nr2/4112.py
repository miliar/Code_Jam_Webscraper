#include<stdio.h>
#include<string.h>
#include<map>

using namespace std;

int g[109][109];

int main()
{
    int i,j,k,l,m,n,t,flag,co=1,r,c,cnti,cntj,tmpi,tmpj;
    scanf("%d",&t);
    while(t--)
    {
        flag=0;
        //map<int,int> mp;
        //map<int,int>::iterator it;
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
            {
                scanf("%d",&g[i][j]);
                //mp[g[i][j]]=1;
            }

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                //if(g[i][j]==1)
                //{
                    cnti=cntj=0;
                    for(tmpj=0;tmpj<c;tmpj++)
                        if(g[i][tmpj]<=g[i][j])
                            cntj++;
                    if(cntj==c)
                        continue;
                    for(tmpi=0;tmpi<r;tmpi++)
                        if(g[tmpi][j]<=g[i][j])
                            cnti++;
                    if(cnti==r)
                        continue;
                    else
                    {
                        flag=1;
                        break;
                    }
                //}
            }
            if(flag)
                break;
        }
        if(!flag)
            printf("Case #%d: YES\n",co++);
        else
            printf("Case #%d: NO\n",co++);
    }
    return 0;
}
