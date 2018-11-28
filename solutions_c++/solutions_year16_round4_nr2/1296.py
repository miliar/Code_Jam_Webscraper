#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

int n, k;
vector<double> v;


double p(int bs, int idx, int yes){
	if (idx == k)return 1.0;
	int x = 0;
	for (int i = 0; i < n; i++){
		if (bs&(1 << i)){
			if (x == idx){ x = i; break; }
			x++;
		}
	}
	double pb = v[x];
	double yp = 0, np = 0;
	if (yes < k / 2){
		yp = pb*p(bs, idx + 1, yes + 1);
//		cout << yp << endl;
	}
	if ((idx - yes) < k / 2){
		np = (1 - pb)*p(bs, idx + 1, yes);
	}
	return yp + np;
}

double p(int bs){
	return p(bs, 0, 0);
}

double f(){
	double ans = 0;
	for (int i = 0; i < 1 << n; i++){
		if (__popcnt(i) == k){
			ans = max(ans, p(i));
		}
	}
	return ans;
}

int main(){
	int T, tc = 0; cin >> T;
	while (T--){
		tc++;
		cin >> n >> k;
		v.assign(n, 0);
		for (int i = 0; i < n; i++)
			cin >> v[i];

		//		cout << "Case #" << tc << ": " << f() << endl;
		printf("Case #%i: %.10f\n", tc, f());
	}
}