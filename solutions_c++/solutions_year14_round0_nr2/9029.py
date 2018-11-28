#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		double c, f, x;
		cin >> c >> f >> x;
		double ans = x / 2.;
		double tm = c / 2.;
		double k = 2 + f;
		while(tm + 1e-10 < ans){
			ans = min(ans, tm + x / k);
			tm += c / k;
			k += f;
		}
		cout.flags(ios::fixed | ios::showpoint);
		cout.precision(7);
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}