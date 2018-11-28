#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

#define MAXN 110
#define MOD  1000000007

struct task {
	int    n;
	string s[MAXN];
} t[MAXN];

char   w[1000];
int    n;
vector<int> l, r, center, middle;
int    nn[MAXN];
int    num;

int solve(task &q) {
	/*
	cout << "subtask " << endl;
	for(int i=0; i<q.n; ++i) cout << i << " " << q.s[i] << endl;
	*/
	for(char c='a'; c <= 'z'; ++c) {
		center.clear();
		l.clear();
		r.clear();
		middle.clear();
		memset(nn, 0, sizeof(nn));

		for(int i=0; i<q.n; ++i) {
			int len = q.s[i].size();
			// center
			bool ok = true;
			bool lok = false;
			bool rok = false;
			int  mok = 0;
			for(int j=0; j<len; ++j) if (q.s[i][j] != c) ok = false;
			if (ok) {
				center.push_back(i);
				nn[i] = 1;
				continue;
			}
			// left && right
			if (q.s[i][0] == c && q.s[i][len-1] ==c) return 0;
			int l1 = 0;
			int r1 = len - 1;
			if (q.s[i][0] == c) {
				l.push_back(i);
				nn[i] = 1;
				lok = true;
				while (q.s[i][l1] == c) l1++;
			}
			if (q.s[i][len-1] == c) {
				r.push_back(i);
				nn[i] = 1;
				rok = true;
				while (q.s[i][r1] == c) r1--;
			}

			// middle
			for(int j=l1; j<=r1; ++j) if (q.s[i][j] == c) {
				nn[i] = 1;
				mok++;
				while (j <= r1 && q.s[i][j] == c) j++;
			}

			if (mok && (lok || rok)) return 0;
			if (mok > 1) return 0;
			if (mok) middle.push_back(i);
		}

		if (middle.size() + l.size() + r.size() + center.size() > 1) {
			if (l.size() > 1) return 0;
			if (r.size() > 1) return 0;
			if (middle.size() > 1) return 0;
			if (middle.size() == 1 && (l.size() + r.size() + center.size() > 0)) return 0;
			
			ll tmp = 1;
			for(int j=0; j<center.size(); ++j) tmp = (tmp * (j + 1)) % MOD;

			t[num].n = 0;
			for(int j=0; j<q.n; ++j) if (!nn[j]) {
				t[num].s[ t[num].n++ ] = q.s[j];
			}

			if (l.size() && r.size()) {
				t[num].s[ t[num].n++ ] = q.s[ r[0] ] + q.s[ l[0] ];
			} else if (l.size()) {
				t[num].s[ t[num].n++ ] = q.s[ l[0] ];
			} else if (r.size()) {
				t[num].s[ t[num].n++ ] = q.s[ r[0] ];
			} else if (center.size()) {
				t[num].s[ t[num].n++ ] = c;
			}

			num++;
			return (tmp * solve(t[num - 1]) ) % MOD;
		}
	}

	ll z = 1;
	for(int j=0; j<q.n; ++j) z = (z * (j + 1)) % MOD;
	return z;
}

int main(){
    int tc;
    freopen("b-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);

    //freopen("B.in", "r", stdin);
    //freopen("B.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
		fprintf(stderr, "test %i\n", tt);
		scanf("%i", &n);
		num = 1;
		t[0].n = n;
		for(int i=0; i<n; ++i) {
			scanf("%s", w);
			t[0].s[i] = w;
		}
		int ans = solve(t[0]);
        printf("Case #%i: ", tt);        
		printf("%i\n", ans);
    }

    return 0;
}

