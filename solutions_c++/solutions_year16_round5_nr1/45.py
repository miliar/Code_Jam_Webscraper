#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 1e6;
const long long INF = 1e9 + 19;

char s[N];
char st[N];

void read() {
	scanf("%s", s);
	int n = strlen(s);
	int cur = 0;
	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (cur > 0 && st[cur - 1] == s[i]) {
			answer += 10;
			cur--;
		}		
		else {
			st[cur++] = s[i];
		}
	}
	answer += (cur / 2) * 5;
	cout << answer << endl;

}

void solve() {

}

void stress() {

}

int main(){
#ifdef MY_DEBUG
    freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
		scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
			printf("Case #%d: ", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}

