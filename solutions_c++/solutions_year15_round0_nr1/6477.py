#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <utility>

using namespace std;


int solve_case() {
	int sm;
	string s;
	cin>>sm>>s;
	vector< int > v(sm + 1);
	for (int i = 0; i < v.size(); ++i) {
		v[i] = s[i] - '0';
	}
	int cl = 0;
	int add = 0;
	for (int i = 0; i < v.size(); ++i) {
		int ta = 0;
		if (i > cl) {
			ta = i - cl;
		}
		cl += ta + v[i];
		add += ta;
	}
	return add;
}

int main() {
	int tt;
	cin>>tt;
	for (int t = 1; t <= tt; ++t) {
		cout<<"Case #"<<t<<": "<<solve_case()<<endl;
	}
	return 0;
}

