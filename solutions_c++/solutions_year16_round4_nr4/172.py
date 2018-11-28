#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#define rep(i,s,t) for (int i=(s); i<=(t); ++i)
#define dep(i,t,s) for (int i=(t); i>=(s); --i)

using namespace std;

int T,n;

char str[10][10];
int tot,inp[10][10],ans;

template<class T>
inline void get(T &n) {
    char c = getchar();
    while (c!='-' && (c<'0' || c>'9')) c = getchar();
    n = 0; T s = 1; if (c=='-') s = -1,c = getchar();
    while (c>='0' && c<='9') n*=10,n+=c-'0',c=getchar();
    n *= s;
}

template<class T> inline T sqr(T x) { return x*x; }

int main() {
    int Test;
    get(Test);
    rep(Ti,1,Test) {
        get(n); tot = 0;
        rep(i,0,n-1) scanf("%s",str[i]);
		int width = 1<<sqr(n); ans = sqr(n);
        rep(i,0,width-1) {
			int pr = i,tmp = 0;
			bool ok = true;
            rep(j,0,n-1)
                rep(k,0,n-1) {
					inp[j][k] = pr&1;
					if (str[j][k]-'0' > inp[j][k]) ok = false;
					if (str[j][k]-'0' < inp[j][k]) ++tmp;
					pr >>= 1;
				}
			if (ok) {
                rep(j,0,n-1) {
					int p = 0;
                    rep(k,0,n-1) p += inp[j][k];
					if (p == 0) ok = false;
					if (p == n) continue;
					int qp = 0,sk = 0;
                    rep(k,0,n-1) if (inp[j][k] == 1) {
                        rep(l,0,n-1) if (l != j && inp[l][k] == 1) qp |= 1<<l;
                        sk ++;
                    }
					int nk = 0;
                    rep(k,0,n-1) if ((qp>>k) & 1) nk++;
					if (nk >= sk) ok = false; 
				}
			}
			if (ok && tmp < ans) ans = tmp;
		}
		printf("Case #%d: %d\n",Ti,ans);
	}
	return 0;
}
