#include <iostream>
#include <cstdio>
#include <climits>
#include <iomanip>
using namespace std;

int t;
double c, f, x, ans;

int main(){
	cin >> t;
	cout << fixed << setprecision(7);
	for(int k = 1; k <= t; ++k){
		cin >> c >> f >> x;
		ans = x/2.0;
		double temp = 0.0;
		for(int a = 1; a < (x/c)+1; ++a){
			temp += c/((a-1)*f+2.0);
			ans = min(ans, temp + x/(a*f+2));
		}
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}
