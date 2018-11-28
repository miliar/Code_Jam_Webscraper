#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int t,a[15][15],n,m,ans,mm;
main()
{
        freopen("B-small-attempt0.in","r",stdin);
        freopen("out11.txt","w",stdout);
        scanf("%d",&t);
        for(int r=1;r<=t;r++)
        {
                scanf("%d %d",&n,&m);
                for(int i=0;i<n;i++)
                {
                        for(int j=0;j<m;j++)
                        {
                                scanf("%d",&a[i][j]);
                        }
                }
                ans=0;
                for(int i=0;i<n;i++)
                {
                        for(int j=0;j<m;j++)
                        {
                                //printf("AA %d %d %d\n",i,j,a[i][j]);
                                if(a[i][j]==1)
                                {
                                        mm=0;
                                        for(int k=0;k<m;k++)
                                        {
                                                if(a[i][k]==2)
                                                {
                                                        mm++;
                                                        break;
                                                }
                                        }
                                        for(int k=0;k<n;k++)
                                        {
                                                if(a[k][j]==2)
                                                {
                                                        mm++;
                                                        break;
                                                }
                                        }
                                        //printf("%d %d %d\n",i,j,m);
                                        if(mm==2)
                                        {
                                                ans=1;
                                        }
                                }
                        }
                }
                printf("Case #%d: ",r);
                if(ans)
                {
                        printf("NO\n");
                }
                else
                {
                        printf("YES\n");
                }
        }
        //system("pause");
}
