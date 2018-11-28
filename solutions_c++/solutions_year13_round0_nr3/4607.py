#include <fstream>
#include <cmath>
#define rep(x,y,z) for (int x=y;x<=z;x++)
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
int tr,a,b,c;
double k;
int pol(int x)
{
    int t=1,x1=x,s[50];
    while (x1>0)
    {
          s[t]=x1%10;
          x1/=10;
          t++;
          }
    x1=x;
    t--;
    rep(i,1,t/2)
    if (s[i]!=s[t-i+1]) return 0;
    return 1;
}
int main()
{
    fin>>tr;
    rep(t,1,tr)
    {
              c=0;
              fin>>a>>b;
              fout<<"Case #"<<t<<": ";
              rep(i,a,b)
              if (pol(i))
              {  
                 k=sqrt(i);
                 if (k==(int)k) if (pol((int)k)) c++;
                 }
              fout<<c<<"\n";
              }
                   
}
