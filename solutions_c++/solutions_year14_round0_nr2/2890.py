#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

template<class T> inline void _min(T& data, const T& comp) {
	if(comp < data)
		data = comp;
}

long double& getMinTime(const long double &c, const long double &f, const long double &x) {
	static long double ans, pre, cp;
	ans = 1e1000L;
	pre = .0L;
	cp = 2;
	for(;;) {
		_min(ans, pre + (x / cp));
		pre += c / cp;
		cp += f;
		if(pre >= ans) break;
	}
	return ans;
}

int main(void) {
	int T;
	cin >> T;
	cout.setf(ios::fixed);
	cout.precision(10);
	for(int t = 1; t <= T; ++ t) {
		long double c, f, x;
		cin >> c >> f >> x;
		cout << "Case #" << t << ": " << getMinTime(c, f, x) << endl;
	}
	return 0;
}
