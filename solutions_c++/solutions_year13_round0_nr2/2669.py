#include<iostream>
#include<cstdio>
using namespace std;
#include<algorithm>
int main()
{
    int a[11][11],r,c,i,j,test,tc;
     freopen("C:\\Users\\SAGAR\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\SAGAR\\Desktop\\output.txt","w",stdout);
     scanf("%d",&test);
    for(tc=1;tc<=test;tc++)
    {
                           int f=0,b[11][11];
                           scanf("%d%d",&r,&c);
                           for(i=0;i<r;i++)
                           for(j=0;j<c;j++)
                           scanf("%d",&a[i][j]);
                           for(i=0;i<r;i++)
                           for(j=0;j<c;j++)
                           b[i][j]=2;
                           for(i=0;i<r;i++)
                           {
                           f=0;
                           for(j=0;j<c;j++)
                           if(a[i][j]!=1)
                           {f=1;break;}
                           if(!f)
                           for(j=0;j<c;j++)
                           b[i][j]=1;
                           }
                           
                           for(i=0;i<c;i++)
                           {
                           f=0;
                           for(j=0;j<r;j++)
                           if(a[j][i]!=1)
                           {f=1;break;}
                           if(!f)
                           for(j=0;j<r;j++)
                           b[j][i]=1;
                           }
                           f=0;
                           for(i=0;i<r;i++)
                           {
                                           for(j=0;j<c;j++)
                                           if(a[i][j]!=b[i][j])
                                           {
                                           f=1;
                                           break;
                                           }
                                           if(f)
                                           break;
                           }
                           if(f)
                           printf("Case #%d: NO\n",tc);
                           else
                           printf("Case #%d: YES\n",tc);
    }
    return 0;
}
                           
