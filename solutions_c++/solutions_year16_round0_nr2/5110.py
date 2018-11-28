#include<fstream>
#include<cstring>
using namespace std;
ifstream f("in");
ofstream g("out");
int t,i,j,n,m,a[101];
char s[100];
int main()
{
    f>>t;
    f.get();
    for(i=1;i<=t;++i) { f.getline(s,101);
                        n=strlen(s);
                        m=0;
                        for(j=0;j<n;++j) if(s[j]=='+') a[j+1]=1;
                                         else a[j+1]=0;
                        j=1;
                        if(!a[1]) { for(j=2;j<=n,!a[j];++j);
                                    m=1;
                                    }
                        for(;j<=n;++j) if(!a[j]) { m+=2;
                                                   for(++j;j<=n,!a[j];++j);
                                                   }
                        g<<"Case #"<<i<<": "<<m<<'\n';
                        }
    return 0;
}
