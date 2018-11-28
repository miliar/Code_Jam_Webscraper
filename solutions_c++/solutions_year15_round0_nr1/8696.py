#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int main() {
	int ncases;
	cin >> ncases;

	for (int c = 1; c <= ncases; c++) {
		int n;
		cin >> n;
		string v;
		cin >> v;
		
		int nfriends = 0;
		int people_up = 0;
		for (int i = 0; i < n+1; i++) {
			int cv = v[i] - '0';

			if (people_up < i) {
				nfriends += (i - people_up);
				people_up = i;
			}

			people_up += cv;
		}

		cout << "Case #" << c << ": " << nfriends << endl;
	}
}
