#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


string to_s(long long n,int d) {
	string s;
	rep(i,d) { s += n % 10 + '0'; n /= 10; };
	reverse(s.begin(), s.end());
	return s;
}


long long to_i(const string &s) {
	long long res = 0;
	for (int i = 0; i<s.size(); i++)res = res * 10 + s[i] - '0';
	return res;
}

long long maxv(string s) {
	rep(i, s.size()) {
		if (s[i] == '?')s[i] = '9';
	}
	return to_i(s);
}
long long minv(string s) {
	rep(i, s.size()) {
		if (s[i] == '?')s[i] = '0';
	}
	return to_i(s);
}


tuple<long long, long long, long long> calc(string s1,string s2,int d) {
	long long a,b;
	if (d==s1.size()) {
		a = to_i(s1);
		b = to_i(s2);
		return make_tuple(abs(a-b),a,b);
	}
	tuple<long long, long long, long long> res(1LL<<60,0,0);

	if (s1[d] == '?') {
		if (s2[d] == '?') {
			s1[d] = '0';
			s2[d] = '0';
			res = min(res, calc(s1, s2, d + 1));
			s1[d] = '0';
			s2[d] = '1';
			a = maxv(s1);
			b = minv(s2);
			res = min(res, make_tuple(abs(a - b), a, b));
			s1[d] = '1';
			s2[d] = '0';
			a = minv(s1);
			b = maxv(s2);
			res = min(res, make_tuple(abs(a - b), a, b));
		}
		else {
			s1[d] = s2[d];
			res = min(res, calc(s1, s2, d + 1));
			if (s2[d] > '0') {
				s1[d] = s2[d] - 1;
				a = maxv(s1);
				b = minv(s2);
				res = min(res, make_tuple(abs(a - b), a, b));
			}
			if (s2[d] < '9') {
				s1[d] = s2[d] + 1;
				a = minv(s1);
				b = maxv(s2);
				res = min(res, make_tuple(abs(a - b), a, b));
			}
		}
	}
	else {
		if (s2[d] == '?') {
			s2[d] = s1[d];
			res = min(res, calc(s1, s2, d + 1));
			if (s1[d] > '0') {
				s2[d] = s1[d] - 1;
				a = minv(s1);
				b = maxv(s2);
				res = min(res, make_tuple(abs(a - b), a, b));
			}
			if (s1[d] < '9') {
				s2[d] = s1[d] + 1;
				a = maxv(s1);
				b = minv(s2);
				res = min(res, make_tuple(abs(a - b), a, b));
			}
		}
		else if(s1[d]==s2[d]){
			return calc(s1, s2, d + 1);
		}
		else if(s1[d] < s2[d]){
			a = maxv(s1);
			b = minv(s2);
			res = min(res, make_tuple(abs(a - b), a, b));
		}
		else {
			a = minv(s1);
			b = maxv(s2);
			res = min(res, make_tuple(abs(a - b), a, b));
		}
	}
	return res;
}



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	rep(icase, T) {
		string s1, s2;
		cin >> s1 >> s2;


		auto a=calc(s1, s2, 0);
		cout << "Case #" << icase + 1 << ": " << to_s(get<1>(a),s1.size())<<' '<<to_s(get<2>(a),s1.size()) << endl;
	}


	return 0;
}