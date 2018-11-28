#include      <algorithm>
#include      <sstream>
#include      <cmath>
#include      <cstdarg>
#include      <cstdio>
#include      <cstdlib>
#include      <iomanip>
#include      <iostream>
#include      <iterator>
#include      <limits>
#include      <list>
#include      <map>
#include      <set>
#include      <vector>
#define endl '\n'
#define each(c, e) for (typeof(c.begin()) e = c.begin(); e != c.end(); ++e)
typedef long long ll;
using namespace std;

vector<ll> g_vectGood;

string toStrig(ll n) { stringstream ss; ss << n; return ss.str(); }
ll toNum(const string &s) { ll r; stringstream ss; ss << s; ss >> r; return r; }
template<typename T1, typename T2> ostream& operator<<(ostream &o, const pair<T1, T2> &p) {return o << '(' << p.first << ", " << p.second << ')';}
template<typename I> ostream& print(ostream &o, I s, I e, int w = 5, int prec = 2, const string &sep = ", ", const string &lhs = "", const string &rhs = "") {
	o << lhs;
	if (s != e) o << setw(w) << setprecision(prec) << *(s++);
	for (; s != e; ++s) o << sep << setw(w) << setprecision(prec) << *s;
	return o << rhs;
}
template<typename T, template<typename E, typename A=std::allocator<E> > class C>
ostream& operator<<(ostream &o, const C<T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "[", "]");}
template<typename T, template<typename E, typename Compare = less<E>, typename Alloc = allocator<E> > class C>
ostream& operator<<(ostream &o, const C<T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "{", "}");}
template<typename K, typename T, template<typename E1, typename E2, typename Compare = std::less<E1>, class Allocator = std::allocator<std::pair<const E1, E2> > > class C>
ostream& operator<<(ostream &o, const C<K, T>& c) {return print(o, c.begin(), c.end(), 0, 2, ", ", "{", "}");}

#define PUSH_IF_SMAL(v, n, s) { ll nn = n; if (nn < (s)) (v).push_back(nn); }
void generatePalin(ll nUpTo, vector<ll> &vectRes) {
	vectRes.clear();
	string strTmp;
	ll nUpToSQ = sqrt(nUpTo);

	for (ll i = 1; i <= 9; i += 1) PUSH_IF_SMAL(vectRes, i, nUpTo);
	for (ll i = 1; i <= nUpToSQ; i += 1) {
		strTmp = toStrig(i);
		PUSH_IF_SMAL(vectRes, toNum(strTmp + strTmp), nUpTo);
		for (int j = 0; j <= 9; j += 1) PUSH_IF_SMAL(vectRes, toNum(strTmp + char('0' + j) + strTmp), nUpTo);
	}

	sort(vectRes.begin(), vectRes.end());
}

bool isPalin(ll n) {
	string s = toStrig(n);
	for (size_t i = 0; i < s.length() / 2; i += 1) {
		if (s[i] != s[s.length() - i - 1]) return false;
	}
	return true;
}

void generateSQPalin(ll nUpTo, vector<ll> &vectRes) {
	vectRes.clear();
	ll nUpToSQ = sqrt(nUpTo);
	vector<ll> vectTmp;

	generatePalin(nUpToSQ, vectTmp);

	each(vectTmp, it) {
		const ll tmpSQPalin = *it * *it;
		if (isPalin(tmpSQPalin)) PUSH_IF_SMAL(vectRes, tmpSQPalin, nUpTo);
	}
}

int main(int argc, char **argv) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	generateSQPalin(1000000000000000ll, g_vectGood);
	int T;
	cin >> T;
	ll A, B, r;
	for (int t = 1; t <= T; t += 1) {
		cin >> A >> B;
		r = 0;
		each(g_vectGood, it) r += A <= *it && *it <= B;
		cout << "Case #" << t << ": " << r << endl;
	}

	return 0;
}
