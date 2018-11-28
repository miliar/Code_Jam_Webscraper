#include <bits/stdc++.h>
using namespace std; 

#define ALL(x) (x).begin(),(x).end() 

typedef long long ll;
const double eps = 1e-10;

int D;
int P[1010];
int solve(){
	vector<int> a(1001);
	for(int i = 0; i < D; ++i){
		a[P[i]]++;
	}
	int res = 1010, t = 0;
	for(int i = 1000; i > 1; --i){
		res = min(i+t, res);
		t += a[i];
		a[i/2] += a[i];
		a[(i+1)/2] += a[i];
	}
	res = min(1 + t, res);
	int tres = 1010;
	for(int i = 1000; i > 0; --i){
		int cnt = 0;
		for(int j = 0; j < D; ++j){
			cnt += (P[j] + i - 1) / i - 1;
		}
		tres = min(tres, cnt + i);
	}
	return tres;
}
int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		cin >> D;
		for(int i = 0; i < D; ++i){
			cin >> P[i];
		}
		int r = solve();
		cout << "Case #" << t << ": " << r << endl;
	}
}
