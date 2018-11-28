#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
	int T, smax;
	string v;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> smax;
		cin >> v;
		
		int ret = 0, up = 0;
		for (int shy = 0; shy <= smax; ++shy) {
			int additional = max(0, shy - up);
			ret += additional;
			up += additional + (v[shy] - '0');
		}
		
		cout << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}

