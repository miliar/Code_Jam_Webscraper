#include<iostream>
#include<string>
#include<math.h>
// #include<vector>
// #include<algorithm>
// #include<map>
// #include<utility>
// #include<sstream>
// #include<ctype.h>
// #include<queue>

using namespace std;

int main(){
//	cout.precision(10);
	int T;
	double C, F, X;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> C >> F >> X;
		double res = X/2;
		if (X <  C) {
                        cout.precision((int)log10(res)+10);
			cout << "Case #" << i+1 << ": " << res << "\n";
		} else {
			double res2 = C/2 + X/(2+F);
			double nbf = 1;
			while (res2 < res) {
				res = res2;
				res2 = res + (C-X)/(2+nbf*F) + X/(2+(nbf+1)*F);
				nbf = nbf + 1;
			}
			cout.precision((int)log10(res)+10);
                        cout << "Case #" << i+1 << ": " << res << "\n";
		}
	}
}
