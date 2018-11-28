#include <cstdlib>
#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <list>
#include <queue>
#include <stack>

using namespace std;

bool in(const string& s, const string& d) {
	//vector<bool> (s.size());
	for (auto i: d) {
		if (s.find(i) == string::npos) {
			return false;
		}
	}
	return true;
}

struct node {
	string s;
	string r;
};

/*bool operator<(const node& a, const node& b) {
	return stoi(a)<stoi(b);
}*/

int main(int argc, char** argv) {
	int Tmax;
	scanf("%d", &Tmax);
	const string key[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};	
	for (int T=1; T<=Tmax; T++) {
		stack<node> st;
		string s;
		cin >> s;
		string res;
		st.push({s,res});
		while (!st.empty()) {
			auto curr = st.top();
			st.pop();
			vector<int> possible;
			const int start = curr.r.size() == 0 ? 0 : curr.r.back() - '0';
			for (int i=start; i<10; i++) {
				if (in(curr.s, key[i])) {
					possible.push_back(i);
				}
			}
			for (auto i: possible) {
				auto tmp = curr;
				for (auto j: key[i]) {
					tmp.s.erase(tmp.s.begin()+tmp.s.find(j));
				}
				tmp.r.append(to_string(i));
				if (tmp.s.size() == 0) {
					printf("Case #%d: %s\n", T, tmp.r.c_str());
					goto next;
				} else {
					st.push(tmp);
				}
			}
		}
		next:;
	}
	
	return 0;
}

