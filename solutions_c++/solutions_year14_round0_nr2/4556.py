#include<cstdio>
#include<iostream>
using namespace std;

double c, f, x, ans, a, b;
int T, n;

int main(){
	freopen("B.in", "r", stdin);
	freopen("BB.out", "w", stdout);
	cin >> T;
	cout << fixed; cout.precision(7);
	for (int h=1; h<=T; h++){
		cin >> c >> f >> x;
		cout << "Case #" << h << ": ";
		ans = x / 2;
		a = c / 2;
		b = x / (2 + f);
		n = 1;
		while (ans > a + b){
			ans = a + b;
			a += c /(n * f + 2);
			n++;
			b = x /(n * f + 2);
		}
		cout << ans << endl;
	}
}
