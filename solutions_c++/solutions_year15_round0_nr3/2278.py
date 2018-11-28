#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
using namespace std;

typedef pair<int, char> pic;
map<pair<char, char>, pic> mul;
vector<pic> power;
long long T, X, L;
string S;

void build(){
	mul[make_pair('1', '1')] = make_pair(1, '1');
	mul[make_pair('1', 'i')] = make_pair(1, 'i');
	mul[make_pair('1', 'j')] = make_pair(1, 'j');
	mul[make_pair('1', 'k')] = make_pair(1, 'k');
	mul[make_pair('i', '1')] = make_pair(1, 'i');
	mul[make_pair('i', 'i')] = make_pair(-1, '1');
	mul[make_pair('i', 'j')] = make_pair(1, 'k');
	mul[make_pair('i', 'k')] = make_pair(-1, 'j');
	mul[make_pair('j', '1')] = make_pair(1, 'j');
	mul[make_pair('j', 'i')] = make_pair(-1, 'k');
	mul[make_pair('j', 'j')] = make_pair(-1, '1');
	mul[make_pair('j', 'k')] = make_pair(1, 'i');
	mul[make_pair('k', '1')] = make_pair(1, 'k');
	mul[make_pair('k', 'i')] = make_pair(1, 'j');
	mul[make_pair('k', 'j')] = make_pair(-1, 'i');
	mul[make_pair('k', 'k')] = make_pair(-1, '1');
}

pic cmul(pic a, pic b) {
	pic c = mul[make_pair(a.second, b.second)];
	c.first *= a.first * b.first;
	return c;
}

void cal_pow(){
	pic v, c;
	power.clear();
	v = make_pair(1, '1');
	for (int i = 0; i < S.length(); i++) {
		v = cmul(v, make_pair(1, S[i]));
	}
	set<pic> hash;
	c = v;
	power.push_back(make_pair(1,'1'));
	hash.insert(make_pair(1, '1'));
	while (hash.find(c) == hash.end()) {
		hash.insert(c);
		power.push_back(c);
		c = cmul(c, v);
	}
}

long long cal_i() {
	long long ret = L * X;
	pic v = make_pair(1, '1');
	for (int i = 0; i <= S.length(); i++) {
		int j;
		pic c = make_pair(1, '1');
		for (j = 0; j < power.size(); j++) {
			c = cmul(power[j], v);
			if (c == make_pair(1, 'i')) break;
		}
		if (c == make_pair(1, 'i'))
			ret = min(ret, 1LL * j * L + i);
		if (i < S.length()) {
			v = cmul(v, make_pair(1, S[i]));
		}
	}
	return ret;
}

long long cal_k() {
	long long ret = L * X;
	pic v = make_pair(1, '1');
	for (int i = S.length(); i >= 0; i--) {
		int j;
		pic c = make_pair(1, '1');
		for (j = 0; j < power.size(); j++) {
			c = cmul(v, power[j]);
			if (c == make_pair(1, 'k')) break;
		}
		if (c == make_pair(1, 'k'))
			ret = min(ret, 1LL * j * L + S.length() - i);
		if (i > 0 ) {
			v = cmul(make_pair(1, S[i-1]), v);
		}
	}
	return ret;
}

string gao() {
	cal_pow();
	if (power[X % power.size()] != make_pair(-1, '1')) return "NO";
	long long l = cal_i();
	long long r = cal_k();
	//cout << l << ' ' << r << endl;
	if (l + r > L * X) return "NO";
	else return "YES";
}

int main(){
	build();
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> L >> X >> S;
		cout << "Case #" << C << ": " << gao() << endl;;
	}
	return 0;
}
