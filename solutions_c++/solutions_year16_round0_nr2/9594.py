#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

#define LARGE

using namespace std;

int main(int argc, char *argv[]) {

	//freopen("A-small.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
	int T;
	cin >> T;
	cin.ignore(1, '\n');
	for (int i = 0; i < T; i++) {
		std::string N;
		std::getline(cin, N);
		bool state = (N[0] == '+') ? true : false;
		int ret = 0;
		for (int j = 0; j < N.size(); j++) {
			if (N[j] == '+') {
				if (!state) {
					ret++;
					state = true;
				}
			} else {
				if (state) {
					ret++;
					state = false;
				}
			}
		}	
		if (!state)
			ret++;
		cout << "Case #"<<(i+1)<<": "<<ret<<"\n";
	}
	return 0;
}