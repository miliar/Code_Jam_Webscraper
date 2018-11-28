#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>

using std::pair;
using std::stringstream;
using std::next_permutation;
using std::sqrt;
using std::priority_queue;
using std::sort;
using std::stack;
using std::string;
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::min;
using std::max;
using std::set;
using std::swap;
using std::random_shuffle;
using std::queue;
using std::sin;
using std::cos;
using std::make_pair;
using std::cos;
using std::cerr;

typedef long long ll; 
typedef pair<ll, ll> pll;
const long double PI = 3.14159265358979323846;  
const ll N = 1000 * 1000 * 1000;
vector<ll> sqpal;
vector<ll> sqpalind;

string sum(string a, string b) {
	int c = 0;
	int n = max(a.size(), b.size());
	while(a.size() < n)
		a += '0';
	while(b.size() < n)
		b += '0';
	for (int i = 0; i < n; ++i) {
		int x = (a[i] - '0') + (b[i] - '0') + c;
		c = x / 10;
		a[i] = '0' + (x % 10);
	}
	if (c)
		a += '1';
	return a;
}


string sq(string s) {
	string res;
	string ss = s;
	for (int i = 0; i < s.size(); ++i) {
		if (i)
			ss = '0' + ss;
		for (int j = 0; j < (s[i] - '0'); ++j)
			res = sum(res, ss);
	}
	return res;
}

bool pal(string s) {
	int n = s.size();
	for (int i = 0; i < n; ++i)
		if (s[i] != s[n - i - 1])
			return false;
	return true;
}




//bool pal(ll x) {
//	stringstream s;
//	s << x;
//	string s1 = s.str();
//	int n = s1.size();
//	for (int i = 0; i < n; ++i)
//		if (s1[i] != s1[n - i - 1])
//			return false;
//	return true;
//}

//void precalc() {
//	for (ll i = 1; i <= N; ++i) {
//		if ((pal(i)) && (pal(i * i))) {
//			sqpal.push_back(i * i);
//			sqpalind.push_back(i);
//		}
//	}
//}
vector<string> pp;
bool comp(string& s1, string& s2) {
	if (s1.size() < s2.size())
		return true;
	if (s1.size() > s2.size())
		return false;
	return (s1 < s2);
}
void smartPrecalc() {
	int n = 50;
	set<string> s;
	s.insert("11");
	s.insert("22");
	s.insert("00");
	s.insert("0");
	s.insert("1");
	s.insert("2");
	s.insert("3");
	while(!s.empty()) {
		string p = *s.begin();
		//cerr << p << endl;
		s.erase(p);
		if (pal(p) && (pal(sq(p)) || (p[0] == '0'))) {
			if (p[0] != '0')
				pp.push_back(sq(p));
			if (p.size() + 2 > n)
				continue;
			s.insert('0' + p + '0');
			s.insert('1' + p + '1');
			s.insert('2' + p + '2');
		}
	}
	sort(pp.begin(), pp.end(), comp);
}

int solve() {
	string a, b;
	cin >> a >> b;
	int res = 0;
	for (int i = 0; i < pp.size(); ++i) {
		if (comp(pp[i], a))
			continue;
		if (comp(b, pp[i]))
			continue;
		++res;
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	smartPrecalc();
	////cout << sqpal.size() << endl;
	//for (int i = 0; i < sqpal.size(); ++i)
	//	cout << sqpalind[i] << "\t" << sqpal[i] << endl;
	/*cout << pp.size() << endl;
	for (int i = 0; i < pp.size(); ++i)
		cout << pp[i] << "\t" << sq(pp[i]) << endl;
	return 0;*/
	int t;
	//scanf("%d\n", &t);
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
		std::cerr << i << endl;
	}
	return 0;
}
