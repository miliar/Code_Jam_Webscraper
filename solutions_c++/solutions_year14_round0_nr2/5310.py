#include <iostream>
#include <iomanip>

using namespace std;

void work() {
	double c, f, x, t=0, ans=1000000000;
	int num=0;
	cin >> c >> f >> x;
	while (ans > t) {
		if (ans > t + x/(2+num*f)) ans = t + x/(2+num*f);
		t = t + (c/(2+num*f));
		num++;
	}
 	cout << setiosflags(ios::fixed) << setprecision(7) << ans <<endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int n;
	cin >> n;
	for (int i=0; i<n; i++) {
		cout << "Case #" << i+1<< ": ";
		work();
	}
} 