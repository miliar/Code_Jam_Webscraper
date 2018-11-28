#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <functional>
#include <numeric>
#include <algorithm>

using namespace std;

int T, N;
double Naomi[1234], Ken[1234];

int main (void) {
	cin >> T;
	for (int i = 1; i<= T; i++) {
		cout << "Case #" << i << ": ";
		cout.setf(ios::fixed); 
		cout.precision(7);
		cin >> N;
		for (int j = 0; j < N; j++) cin >> Naomi[j];
		for (int j = 0; j < N; j++) cin >> Ken[j];
		sort (Naomi, Naomi + N);
		sort (Ken, Ken + N);
		int s = 0;
		int p1 = 0;
		int p2 = 0;
		while (p1 < N) {
			if (Naomi[p1] > Ken[p2]) {
				p2++;
				s++;
			}
			p1++;
		}
		cout << s << " ";
		s = 0;
		p1 = 0;
		p2 = 0;
		while (p2 < N) {
			while ((Naomi[p1] > Ken[p2]) && (p2 < N)) {
				p2++;
				s++;
			}
			p1++;
			p2++;
		}
		cout << s << "\n";
	}
}
