#include<iostream>
#include<stdio.h>
using namespace std;
int i1,i,j,k,l,n,m,t,ax,ay,o;
int a[102][102];
bool b[102][102];
main()
{
      freopen("B-large.in","r",stdin);
      freopen("B-large.out","w",stdout);
      scanf("%d",&t);
      for(i1=1;i1<=t;i1++)
      {
                         scanf("%d %d",&n,&m);
                         for(i=1;i<=n;i++)
                                          for(j=1;j<=m;j++)
                                          {
                                                           scanf("%d",&a[i][j]);
                                                           b[i][j]=false;
                                          }
                         
                        // l=100;ax=1;ay=1;
                         for(i=1;i<=n;i++)
                                          for(j=1;j<=m;j++)
                                          {
                                                           if(!b[i][j])
                                                           {
                                                                       o=0;
                                                                       for(k=1;k<=n&&o==0;k++)
                                                                                        if(a[k][j]>a[i][j])o=1;
                                                                       if(o==0)
                                                                       {
                                                                               for(k=1;k<=n;k++)
                                                                                                if(a[k][j]==a[i][j])b[k][j]=true;
                                                                       }
                                                                       o=0;
                                                                       for(k=1;k<=m&&o==0;k++)
                                                                                        if(a[i][k]>a[i][j])o=1;
                                                                       if(o==0)
                                                                       {
                                                                               for(k=1;k<=m;k++)
                                                                                                if(a[i][k]==a[i][j])b[i][k]=true;
                                                                       }
                                                           }
                                          }
                         /*for(i=1;i<=n;i++)
                         {
                                          for(j=1;j<=m;j++)
                                                           cout<<b[i][j]<<" ";
                                          cout<<endl;
                         }*/
                         o=0;
                         for(i=1;i<=n&&o==0;i++)
                                          for(j=1;j<=m&&o==0;j++)
                                                           if(!b[i][j])o=1;
                         if(o==0)printf("Case #%d: YES\n",i1);
                         else printf("Case #%d: NO\n",i1);
      }
      //system("pause");
}
