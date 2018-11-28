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
const int N = -1;
const long long INF = 1e9 + 19;


int n, l;
char s[11111];

void read() {
	scanf("%d%d", &n, &l);
	bool flag = 1;
	for (int i = 0; i < n; i++) {
		scanf("%s", s);
		bool g = 1;
		for (int j = 0; j < l; j++)
			g &= s[j] == '1';
		if (g)
			flag = 0;
	}
	scanf("%s", s);
	if (!flag) {
		puts("IMPOSSIBLE");
		return;
	}
	else {
		printf("0");
		for (int i = 0; i < l - 1; i++)
			printf("1");
		printf(" ");
		for (int i = 0; i < l; i++)
			printf("0?");
		puts("");
	}
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


