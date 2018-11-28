#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXV 10000
#define MAXS 15
#define MAXN 5000

char voc[MAXV][MAXS];
int  cnt;

char s[100500];
char w[100500];

vi v;
vi vv[500];

int a[MAXN];
int b[MAXN];
int c[MAXN];
int d[MAXN];
int n;

int get_num(char *s) {
	for(int i=0; i<cnt; ++i) if (!strcmp(voc[i], s)) return i;
	strcpy(voc[cnt], s);
	int r = cnt++;
	return r;
}

void parse(vi &v) {
	v.clear();
	gets(s);
	char *p = &s[0];
	char *q;
	while (*p != 0) {
		while (*p == ' ') p++;
		if (*p == 0) break;

		q = &w[0];
		while (*p > ' ') {
			*q++ = *p++;
		}
		*q = 0;
		v.pb (get_num(w) );
	}
	//gets(s);
}

void dd() {
	printf("====\n");
	for(int i=0; i<cnt; ++i) printf("%2i: %15s %i %i %i %i\n", i, voc[i], a[i], b[i], c[i], d[i]);

	for(int i=0; i<n-2; ++i) {
		for(int j=0; j<vv[i].size(); ++j) printf("%i ", vv[i][j]);
		printf("\n");
	}
}

int main() {
	int tc;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	gets(s);
	sscanf(s, "%i", &tc);

	for(int tt=1; tt<=tc; ++tt) {
		cnt = 0;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		printf("Case #%i: ", tt);

		gets(s);
		sscanf(s, "%i", &n);

		parse(v);
		for(int i=0; i<v.size(); ++i) a[ v[i] ] = 1;

		parse(v);
		for(int i=0; i<v.size(); ++i) b[ v[i] ] = 1;

		

		for(int i=0; i<n-2; ++i) {
			parse(vv[i]);
		}

		//dd();
		//return 0;

		int basic = 0;
		for(int i=0; i<cnt; ++i) if (a[i] && b[i]) basic++;

		int m = n - 2;
		int M = 1<<m;
		int best = 100000000;

		for(int mask=0; mask<M; ++mask) {
			bool ok  = true;
			int  tmp = 0;
			memset(c, 0, sizeof(c));
			memset(d, 0, sizeof(d));

			for(int i=0; i<m; ++i) if ((mask>>i) & 1) {
				// eng				
				for(int j=0; j<vv[i].size(); ++j) {
					//if (b[ vv[i][j] ]) ok = false;
					c[ vv[i][j] ] = 1;
				}
			} else {
				// fr			
				for(int j=0; j<vv[i].size(); ++j) {
					//if (a[ vv[i][j] ]) ok = false;
					d[ vv[i][j] ] = 1;
				}
			}

			
			for(int i=0; i<cnt; ++i) {
				if (a[i] && b[i]) continue;
				if ((a[i] || c[i]) && (b[i] || d[i])) tmp++;
				//if (c[i] && d[i] && !(a[i] && b[i])) tmp++;
			}

			if (tmp < best) {
				best = tmp;
				//printf("best = %i  mask=%i\n", best, mask);
				//dd();
			}
			
		}
		printf("%i\n", best + basic);

	}
    return 0;
}