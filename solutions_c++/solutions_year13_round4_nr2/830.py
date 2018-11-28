//{ Template
using namespace std;
//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-10
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define INF 1<<29
#define ll long long
#define db double
#define pb push_back
#define pii pair<int ,int >
#define NL puts("")
#define mx 100005
//{
//Intput_Output
#define II ({ int a; scanf("%d",&a); a;})
#define IL ({ ll a; scanf("%lld",&a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define OC printf("Case %d:",cs);
#define FI freopen("in.txt","r",stdin);
#define FO freopen("out.txt","w",stdout);
//}
//}

struct player{
    int id;
    string st;
    player(int a){
        id = a;
        st = "";
    }
};
vector<player >v;
int n,p,P;
bool cmp(player a,player b){
    if(a.st > b.st) return true;
    if(a.st == b.st && a.id < b.id) return true;
    return false;
}
bool flag[1024];
int main(){
#ifdef IOfromFile
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif
    int t = II;
    For(cs,t){
        v.clear();
        n = II , p = II;
        P = pow(2,n);
        rep(i,P){
            v.pb(player(i));
        }

        while(n){
            for(int i = 0;i < P; i+= 2){
                if(v[i].id < v[i+1].id){
                    v[i].st += 'w';
                    v[i+1].st += 'l';
                }
                else{
                    v[i].st += 'l';
                    v[i+1].st += 'w';
                }
            }
            sort(all(v),cmp);
            n--;
        }
        memo(flag,false);
        rep(i,p)
            flag[v[i].id] = true;
        int ans ;
        rep(i,P){
             if(!flag[i]) break;
             ans = i;
        }
        printf("Case #%d: %d ",cs,ans);
        rep(i,P){
            if(flag[i]) ans = max(ans,i);
        }
        cout << ans << endl;
    }
}
