#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <ostream>
#include <istream>
#include <typeinfo>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <limits>
#include <fstream>
#include <array>
#include <list>
#include <functional>


#define print cout,
#define scan cin,
#define x first
#define y second
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define mp make_pair
#define umap unordered_map
#define uset unordered_set
#define rt return 0;
#define elif else if
#define len(v) ((int)v.size())


using namespace std;

// I/O Stream Manager
namespace Smart_IO_Stream {

	template <class T_First, class T_Second>
	ostream& operator<<(ostream& os, const pair<T_First, T_Second> &p) {
		os << p.first << " " << p.second;
		return os;
	}

	template <class T>
	ostream& operator<<(ostream& os, const vector<T> &v) {
		if (v.empty()) return os;
		for (int i = 0; i < len(v) - 1; i++) {
			os << v[i] << " ";
		}
		os << v[len(v) - 1];
		return os;
	}

	template <class T>
	ostream& operator<<(ostream& os, const vector<vector<T>> &v) {
		if (v.empty()) return os;
		for (int i = 0; i < len(v) - 1; i++) {
			os << v[i];
			os << endl;
		}
		os << v[len(v) - 1];
		return os;
	}


	template <class T_First, class T_Second>
	istream& operator>>(istream& is, pair<T_First, T_Second> &p) {
		is >> p.first >> p.second;
		return is;
	}

	template <class T>
	istream& operator>>(istream& is, vector<T> &v) {
		for (auto &x : v) {
			is >> x;
		}
		return is;
	}

	template<class T>
	istream &operator,(istream &is, T &obj) {
		is >> obj;
		return is;
	}

	template<class T>
	ostream &operator,(ostream &os, const T &obj) {
		return (os << obj << " ");
	}
	

	enum OutSymb {
		nl, ptr, ptr2, cma, 
	};

	ostream &operator,(ostream &os, OutSymb s) {
		switch (s) {
			case nl:
				os << endl;
				break;
			case ptr:
				os << "-> ";
				break;
			case ptr2:
				os << "--> ";
				break;
			case cma:
				os << ", ";
				break;
			default:
				break;
		}
		return os;
	}
}// namespace Smart_IO_Stream


void set_accuracy(int accure) {
	cout << setprecision(accure) << fixed;
}

namespace defython {
	// vector<xrange> xrange::xranges = vector<xrange>();
	template <class T, class T_Rez>
	T_Rez sum(vector<T> &v) {
		T_Rez rez = (T_Rez)0;
		for (auto &x : v) {
			rez += x;
		}
		return rez;
	}

	template <class T>
	long long sum(vector<T> &v) {
		return sum<T, long long>(v);
	}

	template <class T>
	T max(vector<T> &v) {
		if (v.empty())
			assert(false);
		T assume_max = v[0];
		for (auto &x : v) {
			if (assume_max < x) {
				assume_max = x;
			}
		}
		return assume_max;
	}

	template <class T>
	T min(vector<T> &v) {
		if (v.empty())
			assert(false);
		T assume_min = v[0];
		for (auto &x : v) {
			if (assume_min > x) {
				assume_min = x;
			}
		}
		return assume_min;
	}

	template<class T_Map, class T_Key, class T_Value>
	T_Value get(const T_Map &m, const T_Key &key, const T_Value &default_value) {
		auto x = m.find(key);
		if (x == m.end())
			return default_value;
		return x->second;
	}

}// namespace defython

namespace typedefs {
	typedef long long ll;
	typedef unsigned long long ull;
	typedef vector<int> vi;
	typedef pair<int, int> pii;
	typedef vector<vector<pair<int, int>>> vvpii;
	typedef vector<vector<pair<bool, int>>> vvpbi;
}

using namespace Smart_IO_Stream;
using namespace typedefs;
using namespace defython;


#define int long long
int transfer_num_sys(string n, int from_ss, int to_ss) {
	// def to_10(n, p):
	int rez = 0;
	// string s = to_string(n);
	string s = n;
	for (auto c : s) {
		int x = c - '0';
		rez = (rez * from_ss) + x;
	}

	int n_pref = rez;
	vector<int> num;
	while (n_pref >= to_ss) {
		num.push_back(n_pref % to_ss);
		n_pref /= to_ss;
	}
	num.push_back(n_pref);
	reverse(num.begin(), num.end());
	rez = 0;
	for (auto x: num) {
		rez *= 10;
		rez += x;
		
	}
	return rez;
}

int find_del(int x) {
	if (x == 2) return -1;
	for (int i = 2; i < sqrt(x) + 1; i++) {
		if (x % i == 0) {
			return i;
		}
	}
	return -1;
}


vector<int> check(string s) {
	vector<int> rez;
	for (int base = 2; base < 11; base++) {
		// print transfer_num_sys(s, base, 10), nl;
		int d = find_del(transfer_num_sys(s, base, 10));
		if (d == -1) return vector<int>();
		rez.pb(d);
	}
	return rez;
}

string bin_str(int x) {
	string bin_str = bitset<sizeof(x) * 8>(x).to_string();
	string rez = "";
	int first_one = 0;
	while (first_one < len(bin_str) && bin_str[first_one] != '1') {
		first_one++;
	}
	if (first_one == len(bin_str)) {
		first_one--;
	}
	for (; first_one < len(bin_str); first_one++) {
		rez += bin_str[first_one];
	}
	return rez;
}

int cnt_q, need_len;

string cur_gen;

void gen() {
	if (len(cur_gen) == 0 || len(cur_gen) == need_len - 1) {
		cur_gen.pb('1');
		gen();
		cur_gen.ppb();
		return;
	}
	if (len(cur_gen) == need_len) {
		// generated
		auto x = check(cur_gen);
		if (!x.empty()) {
			print cur_gen;
			print x, nl;
			cnt_q--;
			if (cnt_q == 0) {
				exit(0);
			}
		}
		return;
	}

	cur_gen.pb('0');
	gen();
	cur_gen.ppb();
	cur_gen.pb('1');
	gen();
	cur_gen.ppb();
}
#undef int
int main(int argc, char *argv[]) {
#define int long long
	freopen("BigNums.in", "r", stdin);
	freopen("BigNums.out", "w", stdout);
	// print transfer_num_sys("100011", 2, 10);
	scan cnt_q;

	scan need_len, cnt_q;
	cout << "Case #1:\n";
	gen();
	// for (int i = 0; i < (1 << (need_len - 2)); i++) {
	// 	string bstr = bin_str(i);
	// 	// print bstr, nl;
	// 	string s = "1" + bstr + "1";
	// 	auto x = check(s);
	// 	if (!x.empty()) {
	// 		print s;
	// 		print x, nl;
	// 		cnt_q--;
	// 		if (cnt_q == 0) {
	// 			exit(0);
	// 		}
	// 	}
	// }
}