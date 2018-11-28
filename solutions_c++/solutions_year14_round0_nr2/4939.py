#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i, 0, n)
typedef long double D;
#define LIM 1000000
#define time sdlkfj

int main(){
	ios::sync_with_stdio(false);
	cout.precision(6);
	int T;
	cin >> T;

	fr(tt, 1, T+1){
		printf("Case #%d: ", tt);
		D c, f, x, sum = 0, best;
		cin >> c >> f >> x;


		rep(i, LIM){
			D val = sum + x / (i*f+2);
			if(!i || val < best) best = val;
			sum += c / (2 + i*f);
		}

		printf("%.6Lf\n", best);
	}

}



