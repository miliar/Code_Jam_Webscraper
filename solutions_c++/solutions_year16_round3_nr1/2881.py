#include<fstream>
using namespace std;
ifstream f("in");
ofstream g("out");
int t,tt,i,n,m,mini,imin1,imin2,imin3,p[27],a[27];
int main()
{
    f>>t;
    for(tt=1;tt<=t;++tt) { f>>n;
                           m=0;
                           for(i=1;i<=n;++i) { f>>p[i];
                                               m+=p[i];
                                               }
                           g<<"Case #"<<tt<<": ";
                           while(m) { mini=1001,imin1=imin2=imin3=0;
                                      for(i=1;i<=n;++i) { a[i]=m-2*p[i];
                                                          if(a[i]<mini) mini=a[i],imin1=i;
                                                          else if(a[i]==mini) { if(imin2) imin3=i;
                                                                                else imin2=i;
                                                                                }
                                                          }
                                      --p[imin1];
                                      g<<char(imin1+64);
                                      if(imin2&&!imin3) g<<char(imin2+64),--m,--p[imin2];
                                      g<<" ";
                                      --m;
                                      }
                           g<<'\n';
                           }
    return 0;
}
