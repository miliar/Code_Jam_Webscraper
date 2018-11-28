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

LL two[100];
int N;
LL P;

LL f(LL pos) {
	LL leave = two[N];
	LL rank = 0;
	for (int i = 1; i <= N; i++){
	    if (pos == 0) break;
        rank += (leave >> 1);
        pos = (pos - 1) >> 1;
        leave >>= 1;
	}
	return rank + 1;
}

LL g(LL pos) {
	LL leave = two[N];
	pos = leave - pos - 1;
	LL rank = 0;
	for (int i = 1; i <= N; i++){
	    if (pos == 0) rank += (leave >> 1);
	    else pos = (pos - 1) >> 1;
	    leave >>= 1;
	}
	return rank + 1;
}


int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    two[0] = 1;
    for (int i = 1; i <= 55; i++)
        two[i] = two[i - 1] * 2;
    int testcase;
    cin >> testcase;
    for (int tt = 1; tt <= testcase; tt++){
        printf("Case #%d: ", tt);
        cin >> N >> P;
        LL l = 0, r = two[N] - 1;
        while (l + 1 < r){
            LL mid = (l + r) / 2;
            if (f(mid) <= P)
                l = mid;
            else r = mid - 1;
        }
        while (l < two[N] - 1 && f(l + 1) <= P) l++;
        LL ans1 = l;
        l = 0, r = two[N] - 1;
        while (l + 1 < r){
            LL mid = (l + r) / 2;
            if (g(mid) <= P)
                l = mid;
            else r = mid - 1;
        }
        while (l < two[N] - 1 && g(l + 1) <= P) l++;
        LL ans2 = l;
        cout << ans1 << " " << ans2 << endl;
    }
}
