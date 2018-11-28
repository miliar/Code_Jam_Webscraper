#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=a;i>=b;i--)
#define RREP(i,n) RFOR(i,n-1,0)
#define ECH(it, v) for(auto it=v.begin();it!=v.end();++it)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define MOD 1000000007
typedef long long LL;
typedef unsigned int UI;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<vector<int>> VVI;
typedef vector<string> VS;

int main() {
    #ifdef raaja
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int zz, qq= 0;
    scanf("%d", &zz);
    string a[100], s, t;
    int in[100], sm[100];
    while(qq++ < zz) {
        int n;
        cin>>n;
        REP(i, n) cin>>a[i];
        s = "";
        REP(i, a[0].size()-1) if(a[0][i] != a[0][i+1]) s += a[0][i];
        s += a[0][a[0].size()-1];
        bool fl = 0;
        FOR(j, 1, n) {
            t = "";
            REP(i, a[j].size()-1) if(a[j][i] != a[j][i+1]) t += a[j][i];
            t += a[j][a[j].size()-1];
            if(t != s) {
                cout<<"Case #"<<qq<<": Fegla Won\n";
            //cout<<t<<":"<<s<<endl;
                fl = 1;
                break;
            }
        }
        if(fl) continue;
        CLR(in);
        int ret = 0;
        REP(i, s.size()) {
            CLR(sm);
            REP(j, n) {
                while(in[j] < a[j].size() && a[j][in[j]] == s[i]) in[j]++, sm[j]++;
            }
            int tt = 0;
            REP(j, n) tt += sm[j];
            tt += n/2;
            tt /= n;
            REP(j, n) ret += abs(tt - sm[j]);
        }
        cout<<"Case #"<<qq<<": "<<ret<<endl;
    }
}
