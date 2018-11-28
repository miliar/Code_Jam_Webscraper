#include <iostream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <string>

using namespace std;


void solve() {
	int N;
	cin >> N ;
	string s[N];
	string pattern;
	int feq[100][100];
	int n = 0;
	for (int i = 0; i < N; i++) {
		cin >> s[i];
		string &k = s[i];
		string p;
		int count = 0;
		n = 0;
		int j = 0;
		for(j = 0; j < k.size(); j++) {
			if (j && k[j-1] != k[j]) {
				p += k[j-1];
				feq[n++][i] = count;
				count = 0;
			}
			count ++;
		}
		
		p += k[k.size()-1];
		feq[n++][i] = count;
		
		if (pattern.size() == 0) {
			pattern = p;
		}
		if (p != pattern) {
			cout << "Fegla Won";
			return;
		}
		
	}
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sort(feq[i], feq[i] + N);
		int* start, *end;
		start = feq[i];
		end = feq[i] + N;
		while(start < end) {
			sum += *(--end) - *(start++);
		}
	}
	cout << sum;
	return;
}

int main () {
	int T, cases = 0;
	cin >> T;
	while(T--) {
		cout << "Case #" <<  ++cases<< ": ";
		solve();
		cout <<endl;
	}
	return 0;
}
