/*
 *		Problem		: 
 *		Author		: Yicheng Huang from Dept.Computer Science & Technology, PKU
 *		Date		: 
 *		Algorithm	:
 *
 */

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <ctime>
#include <queue>

#define PB push_back
#define MP make_pair
#define two(X) (1<<(X))
#define ME(a) memset(a, 0, sizeof(a))
#define MCP(a, b) memcpy(a, b, sizeof(b))
#define eps 1e-8
#define sqr(x) ((x) * (x))
typedef long long LL;

using namespace std;

const int MOD = 1000002013;

vector<int> station;
int P;
int a[200000];
LL c[200000];
LL s[200000], t[200000], p[200000];
LL org, my;
LL N, M;

LL cal(LL k) {
	if (k == 0) return 0;
	return (N + N - k + 1) * k / 2 % MOD;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int testcase;
    cin >> testcase;
    for (int tt = 1; tt <= testcase; tt++){
        printf("Case #%d: ", tt);
        cin >> N >> M;
        my = 0; org = 0;
        for (int i = 1; i <= M; i++){
            cin >> s[i] >> t[i] >> p[i];
            station.PB(s[i]);
            station.PB(t[i]);
            org = (org + cal(t[i] - s[i]) * p[i] % MOD + MOD) % MOD;
        }
        sort(station.begin(),station.end());
        P = 1;
        a[1] = station[0];
        for (int i = 1; i < station.size(); i++)
            if (station[i] != station[i - 1])
                a[++P] = station[i];
        for (int i = 1; i <= P; i++){
            LL leave = 0;
            for (int j = 1; j <= M; j++){
                if (s[j] == a[i])
                    c[i] += p[j];
                if (t[j] == a[i])
                    leave += p[j];
            }
            for (int k = i; k >= 1; k--){
                if (leave == 0) break;
                LL need = min(leave, c[k]);
                if (need == 0)continue;
                leave -= need;
                c[k] -= need;
                my = (my + need * cal(a[i] - a[k]) % MOD + MOD) % MOD;
            }
        }
        cout << ((org - my) % MOD + MOD) % MOD << endl;
    }
}
