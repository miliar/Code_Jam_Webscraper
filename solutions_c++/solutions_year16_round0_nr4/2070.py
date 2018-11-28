#include <iostream>
#include <ios>
#include <cmath>

using namespace std;
typedef unsigned long long oolong;

int main() {
	long t;
	oolong K, C, S;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for(int i=1;i<=t;++i) {
		cout << "Case #" << i << ":";
		cin >> K >> C >> S;
		long mnm = ceil(1.0*K/C);
		if(S<mnm) cout << " IMPOSSIBLE" << endl;
		else {
			oolong tile=0;
			for(int digit=1, count=0; count < mnm; ++digit) {
				if(!(digit%C)) {
					cout << ' ' << (tile+1);
					tile=0;
					++count;
				}
				tile*=K;
				tile+=(digit%K);
			}
			cout << endl;
		}
	}
}