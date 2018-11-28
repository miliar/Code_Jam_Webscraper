#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;

int N, R, P, S;
char a[1<<13], ans[1<<13];
bool ok;

char check(int tl, int tr){
	if (tl == tr) return a[tl];
	int mid = (tl + tr)/2;
	char t1 = check(tl, mid);
	char t2 = check(mid+1, tr);
	if (t1 == 'X' || t2 == 'X' || t1 == t2){
		return 'X';
	}
	if (t1 > t2) swap(t1, t2);
	// R -> S -> P -> R
	if (mp(t1, t2) == mp('R', 'S')) return 'R';
	if (mp(t1, t2) == mp('S', 'P')) return 'S';
	if (mp(t1, t2) == mp('P', 'R')) return 'P';

	if (mp(t2, t1) == mp('R', 'S')) return 'R';
	if (mp(t2, t1) == mp('S', 'P')) return 'S';
	if (mp(t2, t1) == mp('P', 'R')) return 'P';
	return 'X';
}

void rec(int pos, int p, int r, int s){
	if (ok) return;
	if (pos == (1<<N)){		
		if (check(0, (1<<N) - 1) != 'X'){
			for (int i=0;i<(1<<N);i++){
				ans[i] = a[i];
			}
			ok = true;
		}
		return;
	}
	if (p){
		a[pos] = 'P';
		rec(pos+1, p-1, r, s);
	}
	if (r){
		a[pos] = 'R';
		rec(pos+1, p, r-1, s);
	}
	if (s){
		a[pos] = 'S';
		rec(pos+1, p, r, s-1);
	}
}

void solve(){
	scanf("%d%d%d%d", &N, &R, &P, &S);
	ok = false;
	rec(0, P, R, S);
	if (!ok){
		printf("IMPOSSIBLE\n");
	}
	else {
		for (int i=0;i<(1<<N);i++){
			printf("%c", ans[i]);
		}
		printf("\n");
	}
}

int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    int T;
    scanf("%d", &T);

    for (int i=0;i<T;i++){
    	printf("Case #%d: ", i+1);
    	solve();
    }


    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
