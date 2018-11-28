#include<iostream>
#include<map>
#include<math.h>
#include<stdlib.h>
using namespace std;
int main()
{freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
cin>>t;
for(int l=1;l<=t;l++)
{int z=0;
int n,m,a[100][100],c[100],r[100];
cin>>n>>m;
for(int i=0;i<n;i++)
{r[i]=0;for(int j=0;j<m;j++)
{cin>>a[i][j]; r[i]=r[i]+a[i][j]; }
}
for(int i=0;i<m;i++)
{
    c[i]=0;for(int j=0;j<n;j++)
    { c[i]=c[i]+a[j][i];}
}
int f=0;
for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {f=0;
              if(a[i][j]==1)
              {
                  if(c[j]!=n&&r[i]!=m)
                  {  f=1;break;}
                  
              }
            }
            if(f==1)
                break;
        }
        cout<<"Case #"<<l<<": ";
        if(f==1)
            cout<<"NO"<<"\n";
        else
            cout<<"YES\n";
}
return 0;
}
