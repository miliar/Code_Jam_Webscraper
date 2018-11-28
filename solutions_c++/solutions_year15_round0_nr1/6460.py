#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	int TC, c = 1, smax;
	char audience[1005];
	cin >> TC;
	while (TC--) {
		int friends = 0;
		int pl;
		cin >> smax >> audience;
		pl = audience[0] - '0';
		for (int i = 1; i < smax + 1; i++) {
			if (pl < i) {
				friends++;
				pl++;
			}
			pl += audience[i] - '0';
		}
		cout << "Case #" << c++ << ": " << friends << endl;
	}
	return 0;
}
