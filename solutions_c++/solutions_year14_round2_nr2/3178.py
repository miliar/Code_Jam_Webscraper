/*
 * A.cpp
 *
 *  Created on: Apr 26, 2014
 *      Author: ecaiyan
 */

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
void helper(vector<string>&initflow, vector<string>&requiredflow, int j,
		int &cnt, bool& found) {
	for (auto &x : initflow) {
		if (x[j] == '0') {
			x[j] = '1';
		} else {
			x[j] = '0';
		}
	}
//	for (auto x : requiredflow) {
//		if (x[j] == '0') {
//			x[j] = '1';
//		} else {
//			x[j] = '0';
//		}
//	}
	sort(begin(initflow), end(initflow));
	sort(begin(requiredflow), end(requiredflow));

	if (initflow == requiredflow) {
		found = true;
		return;
	}
	for (int i = 0; i <= j; i++) {
		vector<char> v1;
		vector<char> v2;
		for (auto x : initflow) {
			v1.push_back(x[i]);
		}
		for (auto x : requiredflow) {
			v2.push_back(x[i]);
		}
		if (v1 != v2) {
			return;
		}
	}
	cnt++;
	int L = initflow[0].size();
	for (int i = j + 1; (i < L) && (!found); i++) {
		vector<char> v1;
		vector<char> v2;
		for (auto x : initflow) {
			v1.push_back(x[i]);
		}
		for (auto x : requiredflow) {
			v2.push_back(x[i]);
		}
		if (v1 == v2) {
			continue;
		} else {
			helper(initflow, requiredflow, i, cnt, found);
			break;
		}
	}
}
int EditDistance(const std::string& source, const std::string& target) {
	std::string::size_type i, j;
	int d[101][101] = { 0 };

	for (i = 0; i <= source.length(); i++)
		d[i][0] = i;
	for (j = 0; j <= target.length(); j++)
		d[0][j] = j;

	for (i = 1; i <= source.length(); i++) {
		for (j = 1; j <= target.length(); j++) {
			if ((source[i - 1] == target[j - 1])) {
				d[i][j] = d[i - 1][j - 1]; //²»ÐèÒª±à¼­²Ù×÷
			} else {
				int edIns = d[i][j - 1] + 1; //source ²åÈë×Ö·û
				int edDel = d[i - 1][j] + 1; //source É¾³ý×Ö·û
//                 int edRep = d[i - 1][j - 1] + 1; //source
				d[i][j] = std::min(edIns, edDel);
//                 d[i][j] = std::min(std::min(edIns, edDel), edRep);
			}
		}
	}

	return d[source.length()][target.length()];
}
int helper(string src, string dst) {
	int res = 0;
	int i = 0, j = 0;
	while ((j < src.size()) || (i < dst.size())) {
		if (src[j] == dst[i]) {
			i++;
			j++;
		} else if (dst[i] == dst[i - 1]) {
			while (dst[i] == dst[i - 1]) {
				i++;
				res++;
			}
		} else {
			while (src[j] == src[j - 1]) {
				j++;
				res++;
			}
		}
	}

	return res;
}
string process2(vector<string> &inputString) {
	map<string, int> m;
	vector<string> v = inputString;
	for (auto &x : v) {
		x.erase(unique(begin(x), end(x)), end(x));
		m[x] = x.size();
	}
	if (m.size() > 1) {
		return "Fegla Won";
	}
	int res = INT_MAX;
	string q = inputString[0];
	q.erase(unique(begin(q), end(q)), end(q));
	if (find(begin(inputString), end(inputString), q) == end(inputString)) {
		inputString.push_back(q);
	}
//	for(auto x:inputString){
//		cout<<x<<" "<<endl;
//	}

	for (int i = 0; i < inputString.size(); i++) {
		int sum = 0;
		for (int j = 0; j < inputString.size(); j++) {
			if (j == i) {
				continue;
			}
			sum += helper(inputString[j], inputString[i]);
		}
		res = min(res, sum);
	}
	stringstream ss;
	string s;
	ss << res;
	ss >> s;
	return s;
}
int process(int A, int B, int K) {
	int res = 0;
	for (int i = 0; i < A; i++) {
		for (int j = 0; j < B; j++) {
			if ((i & j) < K) {
				res++;
			}
		}
	}
	return res;
}
int main() {
//	float a = 1999.19990;
//cout<<"a"<<a<<endl;
	int Case = 1;
	int T;
//	char tmp[10000];
//	int p[100];
	int res;
//	vector<string> names;
	scanf("%d", &T);
//	getchar();
	while (T--) {
		int A, B, K;
		scanf("%d%d%d", &A, &B, &K);
//		vector<string> inputString;
//		printf("%d %d\n", N, L);
//		for (int i = 0; i < N; i++) {
//			char tmp[101];
//			scanf("%s", tmp);
//			inputString.push_back(tmp);
//		}

		res = process(A, B, K);
		printf("Case #%d: %d\n", Case++, res);
	}
	return 0;
}

