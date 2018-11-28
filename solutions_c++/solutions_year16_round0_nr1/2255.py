#include <cstdio> // freopen
#include <iostream>
#include <string> // getline
#include <sstream> // stringstream
#include <vector>
#include <utility> // pair
#include <algorithm> // min
using namespace std;

//#define SMALL
#define LARGE

long countingSleep(long N);

int main() {
	string filename = "A";
	//string testin = filename + ".txt";
	//freopen(testin.c_str(), "rt", stdin);
	
#ifdef SMALL
	string smallin = filename + "-small-attempt0.in";
	if (freopen(smallin.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-small.in!" << endl;
		return -1;
	}
	string smallout = filename + "-small.out";
	freopen(smallout.c_str(), "wt", stdout);
#endif
#ifdef LARGE
	string largein = filename + "-large.in";
	if (freopen(largein.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-large.in!" << endl;
		return -1;
	}
	string largeout = filename + "-large.out";
	freopen(largeout.c_str(), "wt", stdout);
#endif

	int T;
	long N;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N;
		if (N == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": " << countingSleep(N) << endl;
		}
	}
	return 0;
}

long countingSleep(long N) {
	int count = 0;
	bool exist[10] = {false}; // ??
	long res = 0;
	while (true) {
		res += N;
		long temp = res;
		while (temp != 0) {
			long mod = temp % 10;
			if (!exist[mod]) {
				exist[mod] = true;
				count++;
			}
			temp /= 10;
		}
		if (count == 10) {
			return res;
		}
	}
}