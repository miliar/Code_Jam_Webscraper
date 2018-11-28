#include <iostream>
#include <cstring>
#include <cmath>
#include <iomanip>

using namespace std;

double pi = acos(-1.0);

double solve(long long t, long long r){
	long long lo = 0, hi = min(double(t / (2 * r - 1)), sqrt(double(t/2.0))) + 1;
	
	while(lo <= hi){
		long long mid = (lo + hi) / 2;
		if(2 * mid * mid + (2 * r - 1) * mid <= t){
			lo = mid + 1;
		}
		else{
			hi = mid - 1;
		}
	}
	
	return hi;
}

int main(){
	long long T, r, t;
	cin >> T;
	
	cout << fixed << setprecision(0);
	
	for(int tc = 1; tc <= T; tc++){
		cin >> r >> t;
		cout << "Case #" << tc << ": " << solve(t, r) << "\n";
	}
}
