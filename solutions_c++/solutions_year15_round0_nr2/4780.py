#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
const int MAXP = MAXN;
int T, D, P[MAXN];

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> T;
	for(int t=1; t<=T; ++t){
		cin >> D;
		int best = 1e9;
		for(int i=0; i<D; ++i) cin >> P[i];
		for(int c = 1; c<MAXN; ++c){
			int time = c;
			for(int i=0; i<D; ++i) time += (P[i]-1) / c;
			if(time < best) best = time;
		}
		cout << "Case #" << t << ": " << best << '\n';
	}
}
