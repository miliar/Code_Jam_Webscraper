#include<iostream>
#include<cstring>

using namespace std;

int a[101][101],row[101],col[101];

int main()
{
    freopen("lawnis.in","r",stdin);
    freopen("lawnos.txt","w",stdout);
    int t,n,m,i,j,tc=1;
    scanf("%d",&t);
    while(t--)
    {
              int min=101;
              scanf("%d%d",&n,&m);
              for(i=0;i<n;i++)
              {
                 row[i]=1;
                 for(j=0;j<m;j++)
                 {
                     col[j]=1;
                     scanf("%d",&a[i][j]);
                     if(min>a[i][j])
                     min=a[i][j];
                 }
              }
              for(i=0;i<n;i++)
              {
                  for(j=0;j<m;j++)
                  {
                     if(a[i][j]!=min)
                     {
                        row[i]=0;
                        break;
                     }
                  }
              }
              
              for(i=0;i<m;i++)
              {
                  for(j=0;j<n;j++)
                  {
                     if(a[j][i]!=min)
                     {
                        col[i]=0;
                        break;
                     }
                  }
              }
              
              /*for(i=0;i<n;i++)
              {
                 cout<<row[i]<<":";
              }
              
              cout<<endl;
              for(i=0;i<m;i++)
              {
                 cout<<col[i]<<":";
              }
              cout<<endl;*/
              int flag=1;
              for(i=0;i<n;i++)
              {
                 for(j=0;j<m;j++)
                 {
                    if(a[i][j]==min && row[i]==0 && col[j]==0)
                    {
                       flag=0;
                       break;
                    }
                 }
                 if(!flag)
                 break;
              }
              printf("Case #%d: ",tc++);
              if(flag)
              printf("YES\n");
              else
              printf("NO\n"); 
    }
    return 0;
}
