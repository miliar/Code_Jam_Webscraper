#include <iostream>
using namespace std;

int n;
long double v, x;
const double eps = 1e-9;
long double r[110], c[110];

int main() {
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);
	int Tn, T;
	cin >> Tn;
	std::cout.precision(20);
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	for (T=1;T<=Tn;T++) {
		cin >> n >> v >> x;
		int i,j;
		bool hasgt = false, haslt = false;
		for (i=0;i<n;i++) {
			cin >> r[i] >> c[i];
			if (c[i]>=x-eps) hasgt = true;
			if (c[i]<=x+eps) haslt = true;
		}
		cout << "Case #" << T << ": ";
		if (!hasgt || !haslt) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (n==1) {		
			cout << v/r[0] << endl;			
		}
		else if (n==2) {
			if (c[0]<=c[1]+eps && c[0]>=c[1]-eps) {
				//long double maxr = max(r[0], r[1]);
				cout << v/(r[0]+r[1]) << endl;
			}
			//else if (c[0]==x) {
			//	cout << v/r[0] << endl;
			//}
			//else if (c[1]==x) {
			//	cout << v/r[1] << endl;
			//}
			else {
				long double t0 = v*(x-c[1])/(r[0]*(c[0]-c[1]));
				long double t1 = (v-t0*r[0])/r[1];
				cout << max(t0, t1) << endl;
			}
		}
		else {
			cout << "Errrrr" << endl;
		}
	}
}