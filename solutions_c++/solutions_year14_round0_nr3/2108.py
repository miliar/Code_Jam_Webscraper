
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
#include <ctime>
#include <limits.h>
using namespace std;

typedef long long ll;
const double pi=acos (-1.0);
const double eps=1e-8 ;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf=0x3f3f3f3f ;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define snuke(c,itr) for( __typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP make_pair
#define fi first
#define se second
typedef pair <int, int> PII;

int r,c,m;
int a[55][55];
bool f[55][55];
bool g[55][55];
bool jud(int x,int y) {
	return x >= 0 && x < r && y >= 0 && y < c;
}
int dx[8] = {0,0,1,-1,1,1,-1,-1};
int dy[8] = {1,-1,0,0,1,-1,1,-1};



bool ok() {
	int i,j;
	FILL(f,0);
	FILL(g,0);
	g[0][0] = 1;
	f[0][0] = 1;
	queue<PII> q;
	q.push(MP(0,0));
	while (!q.empty()) {
		PII tp = q.front();
		q.pop();
		int x = tp.fi;
		int y = tp.se;
		bool tg = 1;
		rep(i,8) {
			int tx = x + dx[i],
					ty = y + dy[i];
			if (jud(tx,ty)) {
				if (a[tx][ty] == 0) tg = 0;
			}
		}
		if (tg) {
			rep(i,8) {
				int tx = x + dx[i],
						ty = y + dy[i];
				if (jud(tx,ty)) {
					f[tx][ty] = 1;
					if (!g[tx][ty]) {
						g[tx][ty] = 1;
						q.push(MP(tx,ty));
					}
				}
			}
		}
	}
	int rec = 0;
	rep(i,r) rep(j,c) if (f[i][j]) rec++;
	return rec == m;
}
void show() {
	int i,j;
	rep(i,r) {
		rep(j,c) {
			if (i + j == 0){
				putchar('c');continue;
			}
			if (a[i][j]) putchar('.');
			else putchar('*');
		}
		cout<<endl;
	}
}
void show2() {
	int i,j;
//	cout<<"?"<<c<<' '<<r<<endl;
	rep(i,c) {
		rep(j,r) {
			if (i + j == 0){
				putchar('c');continue;
			}
			if (a[j][i]) putchar('.');
			else putchar('*');
		}
		cout<<endl;
	}
}

void work() {
	FILL(a,0);
	int i, j, t;
	cin>>r>>c>>m;
	if (r * c == m) {
		puts("Impossible");return;
	}
	if (r * c == m +1) {
		rep(i,r){
			rep(j,c) {
				if (i+j == 0) {
					putchar('c');
				}
				else putchar('*');
			}
			cout<<endl;
		}
		return;
	}
	m = r * c - m;
	for(int i = 1;i <= c;i ++) {
		FILL(a,0);

		int tp = m / i;
		if (m % i) tp++;
		if(tp > r) continue;
		int mm = m;
		rep(j,tp) {
			rep(t,i) {
				if (mm) {
					mm --;
					a[j][t] = 1;
				}
			}
		}
		if (ok()){
			show();return;
		}
	}
//	cout<<"?"<<r<<' '<<c<<endl;
	swap(r,c);
//	cout<<"?"<<r<<' '<<c<<endl;
	for(int i = 1;i <= c;i ++) {
		FILL(a,0);

		int tp = m / i;
		if (m % i) tp++;
		if(tp > r) continue;
		int mm = m;
		rep(j,tp) {
			rep(t,i) {
				if (mm) {
					mm --;
					a[j][t] = 1;
				}
			}
		}
		if (ok()){
			show2();return;
		}
	}
	swap(r,c);

	FILL(a,0);
	int m2 = m;
	rep(i,max(r,c)) {
		if (i <= r) {
			rep(j,c) {
				if (!a[i][j]) {
					if (m2) {
						m2 --;
						a[i][j] = 1;
					}
				}
			}
		}
		if (i <= c) {
			rep(j,r) {
				if (!a[j][i]) {
					if (m2) {
						m2 --;
						a[j][i] = 1;
					}
				}
			}
		}
	}
	if (ok()) {
		show();return;
	}

	FILL(a,0);
	m2 = m;
	rep(i,max(r,c)) {

		if (i <= c) {
			rep(j,r) {
				if (!a[j][i]) {
					if (m2) {
						m2 --;
						a[j][i] = 1;
					}
				}
			}
		}
		if (i <= r) {
			rep(j,c) {
				if (!a[i][j]) {
					if (m2) {
						m2 --;
						a[i][j] = 1;
					}
				}
			}
		}
	}
	if (ok()) {
		show();return;
	}


	puts("Impossible");return;
}

int main() {
	#ifdef LOCAL
		freopen("in.txt", "r", stdin);
		freopen ("test.out","w",stdout);
	#endif

	int t;
	cin>>t;
	int cas = 1;
	while(t--) {
		printf("Case #%d:\n",cas++);
		work();
	}

}






