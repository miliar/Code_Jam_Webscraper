#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i, 0, n)
#define pb push_back
typedef long double D;
#define LIM 50000000
#define time sdlkfj
#define N 20

int _normal[(1<<10) + 5][(1<<10) + 5], n;
int _cheat[(1<<10) + 5][(1<<10) + 5];
D A[N], B[N];

int normal(int m1, int m2){
	if(!m1) return 0;
	int& pd = _normal[m1][m2];
	if(~pd) return pd;
	pd = 0;

	rep(i, n) if(m1 & (1<<i)){

		int least = 1000000;
		rep(j, n) if(m2 & (1<<j)){
			least = min(least, (A[i] > B[j]) + normal(m1 ^ (1<<i), m2 ^ (1<<j)));
		}

		pd = max(pd, least);
	}

	return pd;
}

int cheat(int m1, int m2){
	if(!m1) return 0;

	int& pd = _cheat[m1][m2];
	if(~pd) return pd;
	pd = 0;

	rep(i, n) if(m1 & (1<<i)){
		vector<D> caras;
		rep(j, n) if(m2 & (1<<j)) caras.pb(B[j]);
		if(caras[0] != 0) caras.insert(caras.begin(), 0);
		caras.push_back(1);

		fr(k, 1, caras.size()){
			int least = 1000000, choice;
			D val = (caras[k] + caras[k-1]) / 2;

			rep(j, n) if(m2 & (1<<j)){
				int cost = (val > B[j]) + normal(m1 ^ (1<<i), m2 ^ (1<<j));
				if(cost < least) least = cost, choice = j;
			}

			if(!((val > B[choice] && A[i] > B[choice]) || (val < B[choice] && A[i] < B[choice]))) continue;
			pd = max(pd, (val > B[choice]) + cheat(m1 ^ (1<<i), m2 ^ (1<<choice)));
		}
	}	

	return pd;
}

int main(){
	ios::sync_with_stdio(false);
	int T;
	cin >> T;

	fr(tt, 1, T+1){
		memset(_normal, -1, sizeof _normal);
		memset(_cheat, -1, sizeof _cheat);
		printf("Case #%d: ", tt);
		cin >> n;

		rep(i, n) cin >> A[i];
		rep(i, n) cin >> B[i];
		sort(B, B + n);
		printf("%d %d\n", cheat((1<<n)-1, (1<<n)-1),  normal((1<<n)-1, (1<<n)-1));
	}
}



