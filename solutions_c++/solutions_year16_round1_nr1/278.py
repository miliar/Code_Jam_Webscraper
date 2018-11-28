#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <map>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <queue>
#include <fstream>
using namespace std;

/* --------------------------------- */
 
#define ios ios_base::sync_with_stdio(false)

template<class T> T stoi(string str) {
	T ret = 0;
	for (int i = 0; i < str.size(); i++) ret = ret * 10 + str[i] - '0';
	return ret;
}

bool updateType1(int now, int &ans) {
	if (ans == -1 || ans > now) {
		ans = now;
		return true;
	}
	return false;
}

bool updateType2(int now, int &ans) {
	if (ans == -1 || ans < now) {
		ans = now;
		return true;
	}
	return false;
}

vector<long long> primesUnder(unsigned long long limit) {
	vector<long long> ret;
	vector<bool> u(limit + 1, false);
	for (long long j = 2; j <= limit; j++) if (!u[j]) {
		ret.push_back(j);
		if (j <= limit / j) {
			for (int k = j * j; k <= limit; k += j) u[k] = true;
		}
	}
	return ret;
}

class Edge {
public:
	int from, to;
	Edge *next;
	Edge(int from_, int to_, Edge *next_):from(from_), to(to_), next(next_) {} 
};

/* --------------------------------- */

int testCase = 0;

int main() {
	ios;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int tasks;
	cin >> tasks;
	for (int task = 1; task <= tasks; task ++) {
		string str;
		cin >> str;
		int n = str.length();
		string ans = "";
		vector<bool> bo(n, false);
		int j = n - 1;
		while (j >= 0) {
			for (int i = j - 1; i >= 0; i--) if (str[i] > str[j]) j = i;
			bo[j] =true;
			ans = ans + str[j];
			//cout << j << ' ' << str[j] << endl;
			j = j - 1;
		}
		for (int i = 0; i < n; i++) if (!bo[i]) ans = ans + str[i];
		cout << "Case #" << task << ": " << ans << endl;
	}
	
	return 0;
}
