#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>

#include <cassert>
#include <iomanip>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()


long double v,x;
int n;
int main()
{
    #define name "B-small-attempt4"
    freopen(name ".in","r",stdin);
    freopen(name ".out","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    cout<<fixed<<setprecision(8);
    REP(q,t){
        cin>>n;
        cin>>v>>x;
        vector<pair<LD,LD> > lesser;
        vector<pair<LD,LD> > greater;
        pair<LD,LD> equal = {0,0};
        REP(i,n){
            LD r,c;
            cin>>r>>c;
            if(c > x){
                greater.PB(MP(r,c));
            }
            if(c < x){
                lesser.PB(MP(r,c));
            }
            if(c == x){
                equal.ST += r;
                equal.ND += c;
            }
        }
        LD result = powl(10, 12);
        if(equal.ST != 0 && equal.ND != 0){
            result = min(result, v / equal.ST);
        }
        REP(i, (int) lesser.size()){
            REP(j, (int) greater.size()){
                pair<LD, LD> les = lesser[i];
                pair<LD, LD> gre = greater[j];
                LD t1 = les.ND;
                LD t2 = gre.ND;
                LD v2 = v * (x - t1) / (t2 - t1);
                LD v1 = v * (t2 - x) / (t2 - t1);
                if(abs((v1 * t1 + v2 * t2) / (v1 + v2) - x) <= powl(10,-6)){

                } else{
                    cout<<"LALALALA";
                }
                LD newres = max(v2 / gre.ST, v1 / les.ST);
                result = min(result, newres);
            }
        }
        cout<<"Case #"<<q + 1<<": ";
        if(result == powl(10,12)){
            cout<<"IMPOSSIBLE";
        } else{
            cout<<result;
        }
        cout<<"\n";
    }
    return 0;
}

