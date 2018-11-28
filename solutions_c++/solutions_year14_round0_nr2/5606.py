#include<iostream>
#include<iomanip>
#define li long int
#define ulli long long int
#define fri(n) for(li i=0;i<n;i++)
#define frj(n) for(li j=0;j<n;j++)
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.in", "w", stdout);
	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		double c, f, x;
		cin >> c >> f >> x;
		double ans = 0.0l;
		double rate = 2.0l;
		while ((x / rate) > (c/rate+(x)/(rate+f))) {
			ans += (c / rate);
			rate += f;
		}
		ans+=(x/rate);
		cout << "Case #" << t1 << ": ";
		cout << setprecision(7)<<fixed<<ans << "\n";
	}
	return 0;
}
