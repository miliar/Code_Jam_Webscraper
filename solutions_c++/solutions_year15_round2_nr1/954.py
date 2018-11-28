#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 0

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}


lint p10(int n) {
	lint res = 1;
	For(i, 0, n) {
		res *= 10;
	}
	return res;
}

int solution(int nTest) {
	string ns;
	cin >> ns;
	lint res = 1;
	lint flag = 0;
	if (ns.back() == '0') {
		lint n = stoll(ns);
		flag ++;
		n--;
		ns = to_string(n);
	}
	int nd = ns.size();
	string st = "1";
	while (st.size() < nd) {
		cerr << st << " " << res << endl;
		int al = st.size() / 2;
		int bl = st.size() - al;
		string as = st.substr(0, al);
		string bs = st.substr(al, bl);
		lint b = stoll(bs);
		lint bTo = p10(bl) - 1;
		res += bTo - b;
		cerr << "B" << bTo - b << endl;
		bs = to_string(bTo);
		if (al) {
			reverse(all(as));
			lint a = stoll(as);
			lint aTo = p10(al) - 1;
			res += aTo - a;
			as = to_string(aTo);
			cerr << "A" << aTo - a << endl;
			res++;
			cerr << "Swap" << endl;
		}
		st = bs + as;
		lint t = stoll(st);
		res++;
		t++;
		st = to_string(t);
	}
	cerr << "!" << st << " " << res << endl;

	{
		int al = st.size() / 2;
		int bl = st.size() - al;
		string as = st.substr(0, al);
		string bs = st.substr(al, bl);
		lint m1 = stoll(ns) - stoll(st);
		cerr << "m1" << m1 << endl;

		string rns = ns;
		reverse(all(rns));
		lint m3 = stoll(rns) - stoll(st);
		if (m3 >= 0) {
			m1 = min(m1, m3 + 1);
		}
		if (al) {
			lint m2 = 1;
			string asTo = ns.substr(0, al);
			reverse(all(asTo));
			string bsTo = ns.substr(al, bl);

			string as = st.substr(0, al);
			string bs = st.substr(al, bl);
			reverse(all(as));
			cerr << asTo << " " << bsTo << endl;

			lint b = stoll(bs);
			lint a = stoll(as);
			lint bTo = stoll(bsTo);
			lint aTo = stoll(asTo);

			m2 += bTo - b;
			cerr << "bTo" << bTo << "-b" << b << "=" << bTo - b << endl;;
			m2 += aTo - a;
			cerr << "aTo" << aTo << "-a" << a << "=" << aTo - a << endl;;
			res += min(m2, m1);
		} else {
			res += m1;
		}
	}
	res += flag;

	cout << res << endl;


		

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
