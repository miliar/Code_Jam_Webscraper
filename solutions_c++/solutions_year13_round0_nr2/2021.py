#include<iostream>
#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
int i,j,k,n,m,t,f,val,inde=0;
ifstream fi;
fi.open("in.txt");
ofstream fo;
fo.open("out.txt");
fi>>t;
int a[105][105];
while(t--)
{
          f=0;
          inde++;
          fi>>n>>m;
          for(i=0;i<n;i++)
          for(j=0;j<m;j++)
          fi>>a[i][j];
          for(i=0;i<n;i++)
          {
                          for(j=0;j<m;j++)
                          {
                               val=-1;           
                               for(k=0;k<n;k++) 
                               val=max(val,a[k][j]);
                               if(val>a[i][j])
                               {
                                              val=-1;
                                              for(k=0;k<m;k++)
                                              val=max(val,a[i][k]);
                                              if(val>a[i][j])
                                              {
                                                             f=1;
                                                             break;
                                              }
                               }
                          }
                          if(f==1)
                          break;
          }
          fo<<"Case #"<<inde<<": ";
          if(f==0)
          fo<<"YES\n";
          else
          fo<<"NO\n";
}
fo.close();
fi.close();
}
                               
                                         
