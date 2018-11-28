#include <iostream>
#include <fstream>

using namespace std;
int main() {
	int nTests = 0;
	cin >> nTests;

	for(int i=0; i<nTests;++i) {
		int res = 0;
		int shyMax = 0;
		cin >> shyMax;

		char buf[1024];
		cin >> buf;

		int nStanding = 0;
		for(int j=0; buf[j]; ++j) {
			int v = buf[j] - '0';
			if(v<0 || v>9)
				exit(1);

			while(nStanding < j) {
				res++;
				nStanding++;
			}

			nStanding += v;
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}
