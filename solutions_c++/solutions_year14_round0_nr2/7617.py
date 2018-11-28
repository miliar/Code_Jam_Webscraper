#include <iostream>
#include <set>
#include <limits>
#include <iomanip>

using namespace std;

void outcase(double r, int i) {
	cout<<"Case #"<<i<<": "<<r<<endl;
}

int main() {
	cin.sync_with_stdio(false);
	cout<<fixed<<setprecision(8);

	int T; cin>>T;

	for(int count = 1; count <= T; count++) {
		double C,F,X; cin>>C>>F>>X;

		double sec = 0, cps = 2;
		double opt = INT_MAX;

		int it = 0;

		while(X/cps + sec < opt) {
			opt = X/cps + sec;
			sec += C/cps;
			cps += F;

/*			if(it++ > 2*X)
				break;*/
		}

		outcase(opt,count);
	}

	return 0;
}
