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

#define N 150

int Vx[] = {-1, 0, 1, 0};
int Vy[] = {0, 1, 0, -1};

int n, m;
char M[N][N];

int C (char c){
	if (c == '^') return 0;
	if (c == '>') return 1;
	if (c == 'v') return 2;
	if (c == '<') return 3;
	return -1;
}

bool out (int i, int j){
	return min(i,j) < 0 || i >= n || j >= m;
}


int sai (int i, int j, int d){
	i = i+Vx[d], j = j+Vy[d];
	while (1){
		if (out(i,j)) return 1;
		if (C(M[i][j]) != -1) return 0;
		i = i+Vx[d], j = j+Vy[d];
	}
}


int main (){
	int tt; cin >> tt;
	f (kaso, 1, tt+1){
		bool ok = 1;
		int ans = 0;
		cin >> n >> m;
		f (i, 0, n) scanf(" %s", M[i]);
		f (i, 0, n) f (j, 0, m){
			int x = C(M[i][j]);
			if (x == -1) continue;
			int y = sai (i, j, x);
			if (y == 0) continue;
			int sum = 0;
			f (k, 0, 4){
				int a = sai(i, j, k);
				if (!a) sum++;

			}
			if (sum) ans++;
			else  ok = 0;
		}

		printf("Case #%d: ", kaso);
		if (ok) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;

	}
	return 0;
}
