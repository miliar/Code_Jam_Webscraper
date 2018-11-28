#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <cassert>
#include <map>
#define INF 0x3f3f3f3f
#define mem(a, b) memset((a), (b), sizeof(a))

using namespace std;

const double eps = 1e-8;
const long long mod = 998244353ll;
const long long _3 =   333333336ll;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

long long fpow(long long a, long long b) {
    long long ret = 1;
    while(b) {
        if(b % 2 == 1) {
            ret *= a;
            ret %= mod;
        }
        a = a * a;
        a %= mod;
        b /= 2;
    }
    return ret;
}

char cread;
inline void read(int &x) {
    while((cread=getchar())<'0') {}
    x = cread - '0';
    while((cread=getchar())>='0') x = x * 10 + cread - '0';
}

double sqr(double a) {
    return a * a;
}

const double pi = acos(-1.0);

int n, m;
char num[109][109];

int ans;

bool up(int a, int b) {
	for(int i = a - 1; i >= 0; i--) if(num[i][b] != '.') return true;
	return false;
}

bool down(int a, int b) {
	for(int i = a + 1; i < n; i++) if(num[i][b] != '.') return true;
	return false;
}

bool left(int a, int b) {
	for(int i = b - 1; i >= 0; i--) if(num[a][i] != '.') return true;
	return false;
}

bool right(int a, int b) {
	for(int i = b + 1; i < m; i++) {
		if(num[a][i] != '.') return true;
	}
	return false;
}

bool check(int a, int b) {
	if(num[a][b] == '.') return true;
	bool f = false;
	if(up(a, b) && num[a][b] == '^') return true;
	if(left(a, b) && num[a][b] == '<') return true;
	if(right(a, b) && num[a][b] == '>') return true;
	if(down(a, b) && num[a][b] == 'v') return true;
	if(up(a, b) || left(a, b) || right(a, b) || down(a, b)) f = true;
	if(f) {
		ans++;
		return true;
	}
	return false;
}

int MAIN() {
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++) {
		scanf("%s", num[i]);
	}
	ans = 0;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(!check(i, j)) {
				printf("IMPOSSIBLE\n");
				return 0;
			}
		}
	}
	printf("%d\n", ans);
    return 0;
}

int main() {
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    
    
    while(cases--) {
    //while(~scanf("%d", &n)) {
    	printf("Case #%d: ", cc++);    
        MAIN();
    }
    return 0;
}
