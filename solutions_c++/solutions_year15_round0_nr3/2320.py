#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <fstream>
#include <queue>


using namespace std;

/*map< multiset<int>, int> me;
int go(multiset<int> s) {
	if (me.find(s) != me.end()) {
		return me[s];
	}
	cout <<"hi "<<s.size()<<endl;
	if (accumulate(s.begin(), s.end(), 0) == 0) {
		return 0;
	}
	int u = 1e9;
	for (multiset<int>::iterator it = s.begin(); it != s.end(); it++) {
		multiset<int> t;
		for (multiset<int>::iterator jt = s.begin(); jt != s.end(); jt++) {
			if (jt != it) {
				t.insert(*jt);
			}
		}
		cout << *it << endl;
		for (int i = 1; i < *it; i++) {
			multiset<int> r(t);
			t.insert(i);
			t.insert(*it - i);
			u = min(u, go(r) + 1);
		}
	}
	for (multiset<int>::iterator it = s.begin(); it != s.end(); it++) {
		int t = *it;
		s.erase(t);
		if (t > 0) {
			s.insert(t - 1);
		}
	}
	u = min(u, go(s) + 1);
	return u;
}*/

/*map< vector<int>, int> me;
int go(vector<int> v) {
	if (me.find(v) != me.end()) {
		return me[v];
	}
	if (accumulate(v.begin(), v.end(), 0) == 0) {
		return 0;
	}
	int u = 1e9;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > 1) {
			vector<int> t(v);
			int r = t[i];
			t[i] /= 2;
			t.push_back(r - t[i]);
			sort(t.begin(), t.end());
			u = min(u, go(t) + 1);
		}
	}
	vector<int> t(v);
	for (int i = t.size() - 1; i >= 0; i--) {
		t[i] = max(0, t[i] - 1);
		if (t[i] == 0) {
			t.erase(t.begin() + i);
		}
	}
	u = min(u, go(t) + 1);
	return me[v] = u;
}*/

/*
int getmaxi(vector<int> &v) {
	int t = -1;
	int n = -1;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > t) {
			t = v[i];
			n = i;
		}
	}
	return n;
}*/

/*int go(vector<int> v) {
	int n = getmaxi(v);
	if (v[n] == 1) {
		return 1;
	}
	int u = 1e9;
	u = min(u, v[n]);
	int r = v[n];
	v[n] /= 2;
	v.push_back(r - v[n]);
	u = min(u, go(v) + 1);
	return me[v] = u;
}*/

/*map< vector<int>, int> me;
int goo(vector<int> v) {
	if (me.find(v) != me.end()) {
		return me[v];
	}
	if (accumulate(v.begin(), v.end(), 0) == 0) {
		return 0;
	}
	int u = 1e9;
	int n = getmaxi(v);
	vector<int> t(v);
	for (int i = 0; i < t.size(); i++) {

	}
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > 1) {
			vector<int> t(v);
			int r = t[i];
			t[i] /= 2;
			t.push_back(r - t[i]);
			sort(t.begin(), t.end());
			u = min(u, goo(t) + 1);
		}
	}
	return me[v] = u;
}*/

/*int hi(vector<int> v) {
	int t = -1;
	int n = -1;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > t) {
			t = v[i];
			n = i;
		}
	}
	if (t == 1) {
		return 1;
	}
	int u = 1e9;
	int r = v[n];
	v[n] = (v[n] + 2 - 1) / 2;
	r -= v[n];
	v.push_back(r);
	u = min(u, hi(v) + 1);
	v.pop_back();
	v[n] = t;
	for (int i = 0; i < v.size(); i++) {
		v[i] = max(0, v[i] - 1);
	}
	u = min(u, hi(v) + 1);
	return u;
}*/

/*
void gcj_solve(int caseno, ifstream &in, ofstream &out) {
	int d;
	in >> d;
	vector<int> v(d);
	for (int i = 0; i < d; i++) {
		in >> v[i];
	}
	int w = 0;
	int n = getmaxi(v);
	int ans = v[n];
	map< vector<int>, int> dp;
	dp.insert(v, v[n]);
	while (1) {
		ans = min(ans, w + v[n]);
		if (v[n] == 1) {

			break;
		}
		int r = v[n];
		v[n] /= 2;
		r -= v[n];
		v.push_back(r);
		w++;
		n = getmaxi(v);
	}
	cout << "Case #" << caseno << ": " << ans << "\n";
	out << "Case #" << caseno << ": " << ans << "\n";
}*/

/*int d;
	in >> d;
	vector<int> v(d);
	for (int i = 0; i < d; i++) {
		in >> v[i];
	}
	int w = 0;
	int n = getmaxi(v);
	int ans = v[n];
	map< vector<int>, int> dp;
	dp.insert(v, v[n]);
	while (1) {
		for (int i = 0; i < ) {

		}
		ans = min(ans, w + v[n]);
		if (v[n] == 1) {
			
			break;
		}
		int r = v[n];
		v[n] /= 2;
		r -= v[n];
		v.push_back(r);
		w++;
		n = getmaxi(v);
	}*/


int mul(int a, int b) {
	int x = abs(a);
	int y = abs(b);
	int g[5][5] = {
		{0, 0, 0, 0, 0},
		{0, 1, 2, 3, 4},
		{0, 2, -1, 4, -3},
		{0, 3, -4, -1, 2},
		{0, 4, 3, -2, -1},
	};
	int c = g[x][y];
	if (a < 0) {
		c = -c;
	}
	if (b < 0) {
		c = -c;
	}
	return c;
}

int get(char a) {
	int m[128];
	m['1'] = 1;
	m['i'] = 2;
	m['j'] = 3;
	m['k'] = 4;
	return m[a];
}

map<string, int> me;
int go(string s) {
	if (me.find(s) != me.end()) {
		return me[s];
	}
	if (s.size() == 2) {
		return me[s] = mul(get(s[0]), get(s[1]));
	}
	if (s.size() == 1) {
		return me[s] = get(s[0]);
	}
	if (s.size() == 0) {
		return me[s] = get('1');
	}
	return me[s] = mul(go(s.substr(0, 2)), go(s.substr(2)));
}

int goo(string &s) {
	if (me.find(s) != me.end()) {
		return me[s];
	}
	if (s.size() == 2) {
		return me[s] = mul(get(s[0]), get(s[1]));
	}
	if (s.size() == 1) {
		return me[s] = get(s[0]);
	}
	if (s.size() == 0) {
		return me[s] = get('1');
	}
	return me[s] = mul(goo(s.substr(0, s.size() / 2)), goo(s.substr(s.size() / 2)));
}

int cal(string &s) {
	int t = 1;
	int i = 0;
	for (int i = 0; i < s.size(); i++) {
		t = mul(t, get(s[i]));
	}
	return t;
}

int bme[10001][6];
string ss;
bool ro(int n, int t) {
	if (bme[n][t] != -1) {
		return bme[n][t];
	}
	int &re = bme[n][t];
	if (t == 5 && n < ss.size()) {
		return re = false;
	}
	if (n == ss.size() && t == 5) {
		return re = true;
	}
	for (int i = n; i < ss.size(); i++) {
		if (cal(ss.substr(n, i - n + 1)) == t && ro(i + 1, t + 1)) {
			return re = true;
		}
	}
	/*for (int i = n; i < ss.size(); i++) {
		if (go(ss.substr(n, i - n + 1)) == t && ro(i + 1, t + 1)) {
			return re = true;
		}
	}*/
	return re = false;
}

bool no(string s) {
	/*if (me.find(s) != me.end()) {
		return me[s];
	}*/
	int n = s.size();
	if (n < 3) {
		return false;
	}
	if (n == 3) {
		if (mul(get(s[0]), mul(get(s[1]), get(s[2]))) == -1) {
			return true;
		}
		return false;
	}
	for (int i = 1; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (no(s.substr(0, i)) && no(s.substr(i, j - i)) && no(s.substr(j))) {
				return true;
			}
		}
	}
	return false;
}

void gcj_solve(int caseno, ifstream &in, ofstream &out) {
	int l;
	int x;
	string ll;
	in >> l >> x >> ll;
	string s;
	for (int i = 0; i < x; i++) {
		s += ll;
	}
	//memset(bme, -1, sizeof(bme));
	string ans = "NO";
	int n = s.size();
	/*if (goo(s) == -1) {
		ans = "YES";
	}*/
	/*ss = s;
	if (ro(0, 2)) {
		ans = "YES";
	}*/
	/*int t = 1;
	int i = 0;
	for (int i = 0; i < s.size(); i++) {
		t = mul(t, get(s[i]));
	}
	if (t == -1) {
		ans = "YES";
	}*/
	/*if (no(s)) {
		ans = "YES";
	}*/
	if (cal(s) == -1) {
		int i;
		int t = 1;
		bool boi = false;
		for (i = 0; i < s.size(); i++) {
			t = mul(t, get(s[i]));
			if (t == 2) {
				boi = true;
				break;
			}
		}
		if (boi) {
			t = 1;
			int j;
			bool bok = false;
			for (j = s.size() - 1; j > i; j--) {
				t = mul(get(s[j]), t);
				if (t == 4) {
					bok = true;
					break;
				}
			}
			if (bok) {
				ans = "YES";
			}
		}
	}
	/*for (int i = 1; i < n - 1; i++) {
		if (goo(s.substr(0, i)) == 2) {
			for (int j = i + 1; j < n; j++) {
				if (goo(s.substr(i, j - i)) == 3 && goo(s.substr(j)) == 4) {
					ans = "YES";
					goto end;
				}
			}
		}
	}*/
end:
	cout << "Case #" << caseno << ": " << ans << "\n";
	out << "Case #" << caseno << ": " << ans << "\n";
}

int google_code_jam() {
	ifstream in("input.in");
	ofstream out("output.out");
	if (!in.is_open() || in.eof() || !out.is_open()) {
		cout << "error" << endl;
		return -1;
	}
	int nc;
	in >> nc;
	for (int i = 1; i <= nc; i++) {
		if (in.eof()) {
			cout << "error 2" << endl;
			return -1;
		}
		gcj_solve(i, in, out);
	}
	in.close();
	out.close();
	return 0;
}

int main() {
	google_code_jam();
}