/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define chk(a,k) ((bool)(a&(1LL<<(k))))
#define off(a,k) (a&(~(1LL<<(k))))
#define on(a,k) (a|(1LL<<(k)))

#define mx 20

int a[mx][mx],r,c;

int main(){
    read("bin.txt");
    rite("bout.txt");
    ios_base::sync_with_stdio(0);
    int test,kas=0;
    cin>>test;
    while(test--){
        cin>>r>>c;
        rep(i,r) rep(j,c) {
            cin>>a[i][j];
            a[i][j]=2-a[i][j];
        }
        bool ok=0;
        for(int mask=0; mask<=1<<c; mask++){
            int f=1;
            rep(i,r){
                bool kk=0;
                rep(k,2){
                    kk=1;
                    rep(j,c) if(a[i][j]!=max((int)chk(mask,j),k)){
                        kk=0;
                        break;
                    }
                    if(kk) break;
                }
                if(!kk) {
                    f=0;
                    break;
                }
            }
            if(f) ok=1;
            if(ok) break;
        }
        printf("Case #%d: ",++kas);
        if(ok) puts("YES");
        else puts("NO");
    }
    return 0;
}
