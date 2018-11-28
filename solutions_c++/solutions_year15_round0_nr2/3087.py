//============================================================================//
//------------------------>Nguyen Quoc Nhan<----------------------------------//
//--------------------->quocnhan1843@gmail.com<-------------------------------//
//============================================================================//

#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define oo 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932
#define MaxN 1000000

int GCD(int a, int b){return(b==0?a:GCD(b,a%b));}
int LCM(int a, int b){return a*(b/GCD(a,b));}

int T, _max, D;
int P[1005];

int main(){

    #ifndef ONLINE_JUDGE
    freopen("INPUT.INP", "r", stdin);
    freopen("OUTPUT.OUT", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> T;

    fr(tc, 1, T){
        _max = -1;
        cin >> D;
        rep(i, D){
            cin >> P[i];
            _max = max(_max, P[i]);
        }
        int ans = _max;
        for(int i=1; i<=_max; i++){
            int cur = i;
            for(int j = 0; j < D; j++){
                if(P[j] > i){
                    cur += P[j] / i;
                    if(P[j] % i == 0) cur--;
                }
            }
            ans = min(ans, cur);
        }
        printf("Case #%d: %d\n",tc,ans);
    }
return 0;
}
