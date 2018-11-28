#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <sstream>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define F(i,a) FOR(i,0,a)

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output-small.out","w",stdout);
    int t,n,m;
    cin>>t;
    F(z,t)
    {
        cin>>n>>m;
        int a[n][m];
        bool r=true;
        F(i,n) F(j,m) cin>>a[i][j];
        F(i,n)
        {
            F(j,m)
            {
                if(a[i][j]==1)
                {
                    F(v,n)
                    {
                        if(a[v][j]!=1)
                        {
                            F(w,m) if(a[i][w]!=1){ r=false; break; }
                        }
                    }
                }
                if(r==false) break;
            }
        }
        if(r==true) cout<<"Case #"<<z+1<<": YES"<<endl;
        else cout<<"Case #"<<z+1<<": NO"<<endl;
    }
}
