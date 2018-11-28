#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <climits>
using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RREP(i,n) for(int i=(int)n-1; i>=0; i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > pipii;
typedef vector<int> vi;

const int INF = 1e9;
const int MOD = 1e9+7;

int main(void){
	int T;
    cin >> T;
    REP(tt, T){
        int ms;
        cin >> ms;
        vi x(ms+1, 0);
        REP(i, ms+1){
            char c;
            cin >> c;
            x[i] = (int)(c-'0');
        }
        int ans = 0;
        REP(i, ms+1){
            if(!i) continue;
            if(x[i-1] < i){
                ans += i - x[i-1];
                x[i-1] = i;
            }
            x[i] += x[i-1];
        }
        cout << "Case #" << tt + 1 << ": ";
        cout << ans << endl;
    }
	
	return 0;
}

