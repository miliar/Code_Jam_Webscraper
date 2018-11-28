#include <bits/stdc++.h>

using namespace std;
 
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef map<string, int> MSI;
typedef long long LL;
typedef vector<VI> VII;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#define pb(x) push_back(x)
#define s(n)	scanf("%d", &n)
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define set(a,val) memset(a,val,sizeof(a))
#define REP(i,a,b) for(size_t i=a;i<b;i++)
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define MIN(a,b) (a) < (b) ? (a) : (b)
#define INF (int)1e9;
#define MOD (int) (1e9+7)
#define SZ(A) ((int) A.size())

#ifdef LOCAL
#define trace(a) cerr << #a << " -> " << a << "\t";
#define debug1(a) {trace(a);cerr << endl;}
#define debug2(a,b) {trace(a);trace(b);cerr << endl;}
#else
#define debug1(args...);
#define debug2(args...);
#endif

int main() {
    int t;
    cin >> t;
    for(int z=1;z<=t;++z){
        int a,b,k;
        cin >> a >> b >> k;
        int cnt=0;
        for(int i=0;i<a;++i) {
            for(int j=0;j<b;++j) {
                if((i&j) < k) cnt++;
            }
        }
       cout << "Case #" << z <<": " << cnt << "\n"; 
    }
    return 0;
}
