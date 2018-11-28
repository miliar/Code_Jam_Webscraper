#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main () {
	int T; 
	cin >> T; 
	string line;
	getline(cin,line);
	int R, N, M, K;
	cin >> R >> N >> M >> K;
	getline(cin,line);
	cout << "Case #1:" << endl;
	for (int i = 0; i < R; ++i) {
		vector<int> p;
		for (int j = 0; j < K; ++j) {
			int tmp;
			cin >> tmp;
			p.push_back(tmp);
		}
		getline(cin,line);
		int n3 = 0;
		int n4 = 0;
		int n5 = 0;
		for (int j = 0; j < p.size(); ++j) {
			if (p[j] % 3 == 0) n3 = 1;
			if (p[j] % 9 == 0) n3 = 2;
			if (p[j] % 27 == 0) n3 = 3;
			if (p[j] % 4 == 0) n4 = 1;
			if (p[j] % 16 == 0) n4 = 2;
			if (p[j] % 64 == 0) n4 = 3;
			if (p[j] % 5 == 0) n5 = 1;
			if (p[j] % 25 == 0) n5 = 2;
			if (p[j] % 125 == 0) n5 = 3;
		}
		int printed = 3;
		while (n3) { cout << "3"; n3--; printed--; }
		while (n4) { cout << "4"; n4--; printed--; }
		while (n5) { cout << "5"; n5--; printed--; }
		while (printed) { cout << "2"; printed--; }
		cout << endl;
	}
}
