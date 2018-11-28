#include <bits/stdc++.h>
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define N 1010

int v[N];
int n;

int pd[N][N];

int solve (int x, int y){
	if (x <= y) return 0;
	int& ans = pd[x][y];
	if (ans != -1) return ans;
	ans = N;
	f (i, 1, x){
		ans = min (ans, 1+ solve(i, y) + solve(x-i, y));
	}
	return ans;
}

int main (){
	int t; cin >> t;
	clr (pd, -1);
	f (tt, 1, t+1){
		cin >> n;
		f (i, 0, n) cin >> v[i];
		int ans = N;
		f (i, 1, N){
			int ret = 0;
			f (j, 0, n) ret += solve(v[j], i);
			ret += i;
			ans = min (ans, ret);
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}


