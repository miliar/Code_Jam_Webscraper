#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int T;
	cin >> T;
	cout << fixed << setprecision(10);
	for(int t = 1; t <= T; t++){
		long double res, C, F, X, s = 0;
		cin >> C >> F >> X;
		res = X / 2;
		for(int i = 0; 1; i++){
			s += C / (2 + i * F);
			if(s + X / (2 + F * (i + 1)) < res)  res = s + X / (2 + F * (i + 1));
			else break;
		}
		cout << "Case #" << t << ": " << res << '\n';
	}
}