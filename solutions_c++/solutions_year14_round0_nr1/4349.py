#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <vector>
#include <cmath>
#include <climits>
#include <queue>
#include <cassert>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
using namespace std;
#define PI 3.14159265358979323846264338327950288
vector<string> Tokenize(string s, string ch) {
	vector<string> ret;
	for (int p = 0, p2; p < s.size(); p = p2 + 1) {
		p2 = s.find_first_of(ch, p);
		if (p2 == -1)
			p2 = s.size();
		if (p2 - p > 0)
			ret.push_back(s.substr(p, p2 - p));
	}
	return ret;
}
int my_abs(int a) {
	int i = a >> 31;
	return ((a ^ i) - i);
}

vector<int> TokenizeInt(string s, string ch) {
	vector<int> ret;
	vector<string> p = Tokenize(s, ch);
	for (int i = 0; i < p.size(); i++)
		ret.push_back(atoi(p[i].c_str()));
	return ret;
}

string process(vector<vector<int>> grid1, vector<vector<int>> grid2, int ans1,
		int ans2) {
	string res;
	vector<int> v;
	v.insert(begin(v), begin(grid1[ans1-1]), end(grid1[ans1-1]));
	v.insert(begin(v), begin(grid2[ans2-1]), end(grid2[ans2-1]));
//	for(auto x:v){
//		cout<<x<<" ";
//	}
//	cout<<endl;
	map<int, int> m;
	for (auto x : v) {
		m[x]++;
	}
	sort(v.begin(), v.end());
	vector<int>::iterator it = unique(v.begin(), v.end());
	v.erase(it, v.end());
	int ans = 8 - v.size();
//	cout<<"ans:"<<ans<<endl;
	if (ans == 0) {
		res = "Volunteer cheated!";
	} else if (ans == 1) {
		int n = 0;
		for (auto x : m) {
			if (x.second == 2) {
				n = x.first;
			}
		}
//		char c[10];
//		itoa(n, c, 10);
		stringstream ss;
		ss << n;
		ss >> res;
//		res = (string) c;
	} else {
		res = "Bad magician!";
	}
	return res;
}
int main() {

	int Case = 1;
	int T;
	char tmp[10000];
	int p[100];
	string res;
	vector<string> names;
	scanf("%d", &T);
//	getchar();
	while (T--) {
		vector<vector<int>> grid1;
		vector<vector<int>> grid2;
		int ans1, ans2;
		int n1, n2, n3, n4;

		scanf("%d", &ans1);
		for (int i = 0; i < 4; i++) {
			scanf("%d%d%d%d", &n1, &n2, &n3, &n4);
			vector<int> v;
			v.push_back(n1);
			v.push_back(n2);
			v.push_back(n3);
			v.push_back(n4);
			grid1.push_back(v);
		}
		scanf("%d", &ans2);
		for (int i = 0; i < 4; i++) {
			scanf("%d%d%d%d", &n1, &n2, &n3, &n4);
			vector<int> v;
			v.push_back(n1);
			v.push_back(n2);
			v.push_back(n3);
			v.push_back(n4);
			grid2.push_back(v);
		}
//		cout << ans1 << endl;
//		for (auto x : grid1) {
//			for (auto y : x) {
//				cout << y << " ";
//			}
//			cout << endl;
//		}
//		cout << ans2 << endl;
//		for (auto x : grid2) {
//			for (auto y : x) {
//				cout << y << " ";
//			}
//			cout << endl;
//		}
		res = process(grid1, grid2, ans1, ans2);
		printf("Case #%d: %s\n", Case++, res.c_str());
	}
	return 0;
}
