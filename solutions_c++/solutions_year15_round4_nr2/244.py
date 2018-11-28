#include<iostream>
#include<algorithm>
#include<cstdio>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<cstring>

using namespace std;
typedef long long Int;

#define INF (1LL<<60)
#define EPS (1e-10)
int T;

int n;
double v, x;
double c[1080], r[1080];
double ct[1080];

bool able(double t){
	double tv = 0;
	double vv = 0, xx = 0;
	for(int i = 0;i < n;i++){
		ct[i] = c[i] * t;
		xx = vv*xx + ct[i]*r[i];
		vv += ct[i];
		xx /= vv;
	}
	int ll = n - 1, rr = 0;
	if(x < xx){
		vv = 0, xx = 0;
		for(int i = 0;i < n;i++){
			double v1 = -(x - xx) / (x - r[i]) * vv;
			if(v1 > ct[i] || r[i] <= x || i == 0)v1 = ct[i];
			else{
				vv += v1;
				break;
			}
			xx = vv*xx + ct[i]*r[i];
			vv += ct[i];
			xx /= vv;
		}
	}

	else if(x > xx){
		vv = 0, xx = 0;
		for(int i = n-1;i >= 0;i--){
			double v1 = -(x - xx) / (x - r[i]) * vv;

			if(v1 > ct[i] || r[i] >= x || i == n -1)v1 = ct[i];
			else{
				vv += v1;
				break;
			}
			xx = vv*xx + ct[i]*r[i];
			vv += ct[i];
			xx /= vv;
		}
	}
/*	while(x < xx && x < r[ll]){ 
		double v1 = (x - xx) / (x - r[ll]) * vv;
		v1 = min(v1, ct[ll]);
		xx = vv*xx - r[ll]*v1;
		vv -= v1;
		xx /= vv;
		ll--;
	}
	while(x > xx && x > r[rr]){
		double v1 = (x - xx) / (x - r[rr]) * vv;
		v1 = min(v1, ct[rr]);
		xx = vv*xx - r[rr]*v1;
		vv -= v1;
		xx /= vv;
		rr++;
	}
*/	return v <= vv;
	
}

void solve(){
	cin >> n >> v >> x;
	bool lower = false, upper = false;
	for(int i = 0;i < n;i++){
		cin >> c[i] >> r[i];
		if(r[i] <= x)upper = true;
		if(r[i] >= x)lower = true;
	}
	for(int i = 0;i < n;i++){
		for(int j = 1;j < n;j++){
			if(r[j] < r[j-1]){
				swap(c[j], c[j-1]);
				swap(r[j], r[j-1]);
			}
		}
	}
	if(!lower || !upper){
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	double bottom = 0, top = 1e9;
	for(int i = 0;i < 200;i++){
		double mid = (top + bottom) / 2;
		if(able(mid))top = mid;
		else bottom = mid;
	}
	printf("%.9lf\n", top);
}

int main(){
	cin >> T;
	for(int i = 1;i <= T;i++){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;	
}