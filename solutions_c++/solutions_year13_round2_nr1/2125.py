#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#define rep(x,y,z) for (int x=y;x<=z;x++)
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int n,m,s,k,o,p,p1,t,x;

int main()
{
    fin>>t;    
    rep(k,1,t)
    {
              
              fin>>n>>s;
              vector <int> co(s);
              rep(i,0,s-1)
                        fin>>co[i];
              sort(co.begin(),co.begin()+s);
              m=s;
              x=0;
              fout<<"Case #"<<k<<": ";
              while (m)
              {
                    while (co[x]<n && x<s) {n+=co[x]; x++; m--; p1=0;}
                         p++;
                         p1++;
                    if (m==0) {fout<<p-1<<"\n"; break;}
                    if (m==p1){fout<<p<<"\n"; break;}
                    n+=n-1;
                    }
              p=0;
              p1=0;
              co.erase(co.begin(),co.end());
              }
    
}
