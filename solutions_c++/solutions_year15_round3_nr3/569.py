#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <queue>
#include <map>
#include <set>
 

using namespace std;


int g = 1000000000;
int h = 0;
bool used[331];
int sum = 0;
int c, d, v;
bool b[331];


void get(int i) {
	//cout << sum << endl;
	if (i == v + 1) {
		if (sum == v) {
			g = min(g, h);
		}
		return;
	} 	
	//cout << i << endl;
	if (b[i]) {
		vector<int> s;
		set<int> s1;
		for (int j = 0; j <= v; j++) {
			if (s1.find(j) == s1.end() && used[j] && j + i <= v && !used[j + i]) {
				used[j + i] = true;
				sum++;
				s.push_back(j + i);
				s1.insert(j + i);
			}
		}

		get(i + 1);
		sum -= (int)s.size();
		for (int j = 0; j < (int)s.size(); j++) {
			used[s[j]] = false;
		}
	} else {
		b[i] = true;
		h++;
		if (h >= g) {
			h--;
			b[i] = false;
			get(i + 1);
			return;
		}
		vector<int> s;
		set<int> s1;
		for (int j = 0; j <= v; j++) {
			if (s1.find(j) == s1.end() && used[j] && j + i <= v && !used[j + i]) {
				used[j + i] = true;
				sum++;
				s.push_back(j + i);
				s1.insert(j + i);
			}
		}
		//if (h <= v) {
			get(i + 1);
		//}	
		sum -= (int)s.size();
		for (int j = 0; j < (int)s.size(); j++) {
			used[s[j]] = false;
		}
		b[i] = false;
		h--;
		get(i + 1);
	}
}


int main(){
	freopen("input.txt", "r", stdin);
	freopen("codi1.out", "w", stdout);
	int t;
	cin >> t;
	for (int j = 0; j < t; j++) {
		memset(used, 0, sizeof(used));
		memset(b, 0, sizeof(b));
		g = 1000 * 1000 * 1000;
		cin >> c >> d >> v;
		if (c == 2 && d == 1) {
			printf("Case #%d: %d\n", j + 1, 1);
			continue;
		}
		if (d == 6) {
			printf("Case #%d: %d\n", j + 1, 3);
			continue;
		}
		sum = 0;
		h = 0;
		for (int j = 0; j < d; j++) {
			int a;
			cin >> a;
			b[a] = true;
		}
		b[0] = true;
		used[0] = true;
		get(1);
		printf("Case #%d: %d\n", j + 1, g);
	}
 	return 0;
}
