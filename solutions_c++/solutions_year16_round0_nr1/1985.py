#include <iostream>
#include <sstream>
#include <string>
using namespace std;

typedef long long ll;

int main() {
	ll T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		ll N;
		ll accume;
		ll res = -1;

		cin >> N;
		accume = N;
		int tmp = 0;
		for(int j = 0; j < 1000; j++) {
			stringstream sstr;
			string s;
			sstr << accume;
			sstr >> s;
			for(int k = 0; k < s.size(); k++) {
				tmp |= 1 << (s[k]-'0');
			}
			if(tmp == 0x3ff) {
				res = accume;
				break;
			}
			accume += N;
		}

		cout << "Case #" << i << ": ";
		if(res+1)
			cout << res << endl;
		else
			cout << "INSOMNIA" << endl;
	}
}
