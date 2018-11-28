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
#include <sstream>
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

int n;
map<unsigned int, int> mm;
vector<unsigned int> v[29];
bitset<10000> bt[29], eng, spn;
stringstream ss;
char str[1000009];
int ans;
int ttmp;

unsigned int BKDRHash(char *str)
{
    unsigned int seed = 13131; // 31 131 1313 13131 131313 etc..
    unsigned int hash = 0;
 
    while (*str)
    {
        hash = hash * seed + (*str++);
    }
 
    return (hash & 0x7FFFFFFF);
}

void gao(int a) {
	v[a].clear();
	ss.clear();
	ss.str(str);
	char tmp[109];
	while(ss >> tmp) {
		v[a].push_back(BKDRHash(tmp));
		mm[BKDRHash(tmp)] = 1;
	}
}

void pusheng(int a) {
	eng = eng | bt[a];
}

void pushspn(int a) {
	spn = spn | bt[a];
}

int MAIN() {
	scanf("%d\n", &n);
	mm.clear();
	for(int i = 0; i < n; i++) {
		gets(str);
		gao(i);
	}
	int cc = 1;
	for(map<unsigned int, int>::iterator it = mm.begin(); it != mm.end(); ++it) {
		it->second = cc++;
	}
	for(int i = 0; i < n; i++) {
		bt[i].reset();
		for(int j = 0; j < v[i].size(); j++) {
			bt[i].set(mm[v[i][j]]);
		}
	}
	ans = 0x3f3f3f3f;
	for(int i = 0; i < (1 << (n - 2)); i++) {
		ttmp = 0;
		eng.reset();
		spn.reset();
		pusheng(0);
		pushspn(1);
		for(int k = 2; k < n; k++) {
			if((1 << (k - 2)) & i) {
				pusheng(k);
			} else {
				pushspn(k);
			}
		}
		ans = min(ans, (int)(eng & spn).count());
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
