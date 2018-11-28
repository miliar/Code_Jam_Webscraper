#include <iostream>
#include <iomanip> 

using namespace std;

void solve(int cs) {

	double C,F,X;
	cin >> C >> F >> X;
	
	int mc=int(X/C)+1;	
	double ans= X/2.0;
	double t, ot=0;
	for (int i=1; i<mc; ++i) {
		t= ot+C/(2.0+(i-1)*F);
		ot = t;
		ans = min(ans, t+X/(2.0+i*F));
	}
	
	cout << fixed << setprecision(6) << "Case #" << cs << ": " << ans << endl;
}

int main() {
	
	int T;
	cin >> T;
	for (int i=1; i<=T; ++i)
		solve(i);
	
	return 0;
}