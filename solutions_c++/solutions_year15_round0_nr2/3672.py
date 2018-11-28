
#include <bits/stdc++.h>

using namespace std;

int h[1010][20];
bool vish[1010][20];
int H(int i, int j) {
	if(vish[i][j])
		return h[i][j];
	vish[i][j] = true;
	return h[i][j] = j ? max(H(i/2, j-1), H(i/2 + i%2, j-1)) : i;
}

int g[1010][20];
bool visg[1010][20];
int G(int i, int j) {
	if(visg[i][j])
		return g[i][j];
	visg[i][j] = true;
	if(i < 2)
		return g[i][j] = 0;
	return g[i][j] = j ? 1 + G(i/2, j-1) + G(i/2 + i%2, j-1) : 0;
}

int D, p[1010], time_limit, time_used, S;
bool vis[1010][1010], f[1010][1010];

bool F(int i, int j) {
	if(i == D)
		return true;
	else if(j > time_used)
		return false;
	else if(vis[i][j])
		return f[i][j];
	vis[i][j] = true;

//	for(int k = 0; p[i]>>k; k++) {
//		int timeToSplit = G(p[i], k);
//		int timeToEat = H(p[i], k);
	for(int k = 1; p[i]/k; k++) {
		int timeToSplit = k-1;//G(p[i], k);
		int timeToEat = p[i]/k + (p[i]%k > 0);//H(p[i], k);
		int timeToFinish = time_used + timeToEat;
//		cerr << i << ' ' << j << ' ' << k << ' ' << p[i] << ' ' << timeToSplit << ' ' << timeToEat << endl;
		if(timeToSplit + j <= time_used && timeToFinish <= time_limit)
			return f[i][j] = F(i+1, j + timeToSplit);
	}


	return f[i][j] = false;
}

int solve() {
	int L = 0, R = S;
	while(L < R) {
		bool good = false;
		time_limit = (L+R)/2;
		for(time_used = 0; time_used <= time_limit; time_used++) {
			memset(vis, false, sizeof vis);
			if(F(0,0)) {
				good = true;
				break;
			}
//			cerr << time_limit << "->" << time_used << "..NOK" << endl;
		}
		if(good)
//			cerr << time_limit << "->" << time_used << " OK <-" << endl,
			R = time_limit;
		else
//			cerr << time_limit << " NOK" << endl,
			L = time_limit+1;
	}
	return L;
}

int main() {
	freopen("B-large.in", "r", stdin);
//	freopen("B-small-attempt4.in", "r", stdin);
	freopen("output_large.out", "w", stdout);
	int T;
	cin >> T;
	for(int cse = 1;cse <= T; cse++) {
		cin >> D;
		S = 0;
		for(int i = 0; i < D; i++)
			cin >> p[i], S = max(S, p[i]);

		printf("Case #%d: %d\n", cse, solve());
		cerr << cse << endl;
	}

	return 0;
}
