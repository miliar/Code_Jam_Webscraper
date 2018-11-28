#include <fstream>
#define rep(x,y,z) for (int x=y;x<=z;x++)
using namespace std;
ifstream fin("B.in");
ofstream fout("B.out");
int r[102],c[102],n,m,k,maxx,tr,a[103][103];


int main()
{
    k=1;
    fin>>tr;
    rep(t,1,tr)
    {
    
              fin>>n>>m;
              rep(i,1,n)
              rep(j,1,m)
              fin>>a[i][j];
              fout<<"Case #"<<t<<": ";
              maxx=1;
              while (maxx>0 && k)
              {
                    maxx=0;
                    rep(i,1,n)
                    rep(j,1,m)
                    if (a[i][j]>maxx) maxx=a[i][j];
                    rep(i,1,n)
                    rep(j,1,m)
                    if (a[i][j]==maxx && (r[i]!=2 || c[j]!=2) && k) {if (r[i]==0) r[i]=1; if (c[j]==0) c[j]=1; a[i][j]=-1;} else if (k && a[i][j]==maxx) {fout<<"NO"; k=0; break;}
                    rep(i,1,n)
                    if (r[i]==1) r[i]=2;
                    rep(j,1,m)
                    if (c[j]==1) c[j]=2;
                    }
              if (k) fout<<"YES";
              k=1;
              rep(i,1,n)
              r[i]=0;
              rep(j,1,m)
              c[j]=0;
              fout<<"\n";
              }
}
