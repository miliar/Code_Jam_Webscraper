
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <cmath>
#include <array>
#include <functional>
#include <memory>
using namespace std;
// template code
typedef unsigned char byte;
namespace std {
	istream& operator>>(istream& is, unsigned char& v) {
		int intval = v;
		is >> intval;
		v = (unsigned char)intval;
		return is;
	}
	template<typename T, size_t N>
	istream& operator>>(istream& is, array<T, N>& v) {
		for (size_t i = 0; i < N; ++i) {
			is >> v[i];
		}
		return is;
	}
	ostream& operator<<(ostream& os, const unsigned char& v) {
		os << (int)v;
		return os;
	}
	template<typename T>
	ostream& operator<<(ostream& os, const vector<T>& v) {
		if (v.size() == 0) {
			throw "printing an empty vector";
		}
		for (size_t i = 0; i < v.size(); ++i) {
			if (i >= 1) {
				os << " ";
			}
			os << v[i];
		}
		return os;
	}
	template<typename T, size_t N>
	ostream& operator<<(ostream& os, const array<T, N>& v) {
		for (size_t i = 0; i < v.size(); ++i) {
			if (i >= 1) {
				os << " ";
			}
			os << v[i];
		}
		return os;
	}
	template<typename T1, typename T2>
	ostream& operator<<(ostream& os, const pair<T1, T2>& v) {
		return os << v.first << " " << v.second;
	}
	template<size_t N, typename TupleType>
	struct tupleprinter {
		static void print(ostream& os, const TupleType& v) {
			tupleprinter<N - 1, TupleType>::print(os, v);
			os << " " << get<N>(v);
		}
	};
	template<typename TupleType>
	struct tupleprinter<0, TupleType> {
		static void print(ostream& os, const TupleType& v) {
			os << get<0>(v);
		}
	};
	template<typename T, typename... Rest>
	ostream& operator<<(ostream& os, const tuple<T, Rest...>& v) {
		tupleprinter<sizeof...(Rest), tuple<T, Rest...>>::print(os, v);
		return os;
	}
	template<typename T1, typename T2>
	struct hash<pair<T1, T2>> {
	public:
		size_t operator()(const pair<T1, T2>& v) const
		{
			size_t prime = 16777619U;
			size_t val = 0;
			val = (val * prime) ^ (hash<T1>()(v.first) + sizeof(T1));
			val = (val * prime) ^ (hash<T2>()(v.second) + sizeof(T2));
			return val;
		}
	};
	template<size_t N, typename TupleType>
	struct tuplehasher {
		static size_t compute(const TupleType& v) {
			size_t prime = 16777619U;
			size_t val = tuplehasher<N - 1, TupleType>::compute(v);
			val = (val * prime) ^ (hash<tuple_element<N, TupleType>::type>()(get<N>(v)) +
				sizeof(tuple_element<N, TupleType>::type));
			return val;
		}
	};
	template<typename TupleType>
	struct tuplehasher<0, TupleType> {
		static size_t compute(const TupleType& v) {
			return hash<tuple_element<0, TupleType>::type>()(get<0>(v)) +
				sizeof(tuple_element<0, TupleType>::type);
		}
	};
	template<typename T, typename... Rest>
	struct hash<tuple<T, Rest...>> {
	public:
		size_t operator()(const tuple<T, Rest...>& v) const
		{
			return tuplehasher<sizeof...(Rest), tuple<T, Rest...>>::compute(v);
		}
	};
	template<typename T>
	struct hash<vector<T>> {
	public:
		size_t operator()(const vector<T>& v) const
		{
			size_t prime = 16777619U;
			size_t val = 0;
			for (size_t i = 0; i < v.size(); ++i) {
				val = (val * prime) ^ (hash<T>()(v[i]) + sizeof(T));
			}
			return val;
		}
	};
	template<typename T, size_t N>
	struct hash<array<T, N>> {
	public:
		size_t operator()(const array<T, N>& v) const
		{
			size_t prime = 16777619U;
			size_t val = 0;
			for (size_t i = 0; i < v.size(); ++i) {
				val = (val * prime) ^ (hash<T>()(v[i]) + sizeof(T));
			}
			return val;
		}
	};
}
class ostreamstring : public ostringstream {
public:
	template<typename T>
	ostreamstring& operator<<(const T& v) {
		ostream::operator<<(v);
		return *this;
	}
};
template<typename T, typename... Rest>
class mytup : public tuple<T, Rest...> {
public:
	mytup() {
	}
	mytup(T first, Rest... rest) : tuple(first, rest...) {
	}
};
namespace std {
	template<typename T, typename... Rest>
	ostream& operator<<(ostream& os, const mytup<T, Rest...>& v) {
		return os << static_cast<tuple<T, Rest...>>(v);
	}
	template<typename T, typename... Rest>
	struct hash<mytup<T, Rest...>> : public hash<tuple<T, Rest...>> {
	};
}
template<typename T, size_t N>
class vec : public array<T, N> {
	static_assert(N >= 1, "size cannot be zero");
public:
	static const vec zero;
	static const vec one;
	vec() {
	}
	explicit vec(T element) {
		fill(element);
	}
	template<typename... Rest>
	vec(T element, T element2, Rest... rest) : array{element, element2, rest...} {
		static_assert(sizeof...(Rest) == N - 2, "wrong number of initial values");
	}
	template<typename = std::enable_if_t<(N > 0)>>
	T& x() {
		return _Elems[0];
	}
	template<typename = std::enable_if_t<(N > 0)>>
	const T& x() const {
		return _Elems[0];
	}
	template<typename = std::enable_if_t<(N > 1)>>
	T& y() {
		return _Elems[1];
	}
	template<typename = std::enable_if_t<(N > 1)>>
	const T& y() const {
		return _Elems[1];
	}
	template<typename = std::enable_if_t<(N > 2)>>
	T& z() {
		return _Elems[2];
	}
	template<typename = std::enable_if_t<(N > 2)>>
	const T& z() const {
		return _Elems[2];
	}
	T bound() const {
		T v(0);
		for (size_t i = 0; i < N; ++i) {
			v = max(v, abs(_Elems[i]));
		}
		return v;
	}
	double length() const {
		double v = 0.;
		for (size_t i = 0; i < N; ++i) {
			v += _Elems[i] * _Elems[i];
		}
		return sqrt(v);
	}
	T dot(const vec& b) const {
		T v(0);
		for (size_t i = 0; i < N; ++i) {
			v += _Elems[i] * b._Elems[i];
		}
		return v;
	}
	template<typename = std::enable_if_t<(N == 3)>>
	vec cross(const vec& b) const {
		vec c;
		c._Elems[0] = _Elems[1] * b._Elems[2] - _Elems[2] * b._Elems[1];
		c._Elems[1] = _Elems[2] * b._Elems[0] - _Elems[0] * b._Elems[2];
		c._Elems[2] = _Elems[0] * b._Elems[1] - _Elems[1] * b._Elems[0];
		return c;
	}
	vec takemax(const vec& b) const {
		vec c;
		for (size_t i = 0; i < N; ++i) {
			c._Elems[i] = max(_Elems[i], b._Elems[i]);
		}
		return c;
	}
	vec takemin(const vec& other) const {
		vec c;
		for (size_t i = 0; i < N; ++i) {
			c._Elems[i] = min(_Elems[i], b._Elems[i]);
		}
		return c;
	}
	vec operator-() const {
		vec c;
		for (size_t i = 0; i < N; ++i) {
			c._Elems[i] = -_Elems[i];
		}
		return c;
	}
	vec& operator+=(const vec& b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] += b._Elems[i];
		}
		return *this;
	}
	vec& operator+=(T b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] += b;
		}
		return *this;
	}
	vec& operator-=(const vec& b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] -= b._Elems[i];
		}
		return *this;
	}
	vec& operator-=(T b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] -= b;
		}
		return *this;
	}
	vec& operator*=(const vec& b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] *= b._Elems[i];
		}
		return *this;
	}
	vec& operator*=(T b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] *= b;
		}
		return *this;
	}
	vec& operator/=(const vec& b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] /= b._Elems[i];
		}
		return *this;
	}
	vec& operator/=(T b) {
		for (size_t i = 0; i < N; ++i) {
			_Elems[i] /= b;
		}
		return *this;
	}
};
template<typename T, size_t N>
vec<T, N> operator+(const vec<T, N>& a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] + b._Elems[i];
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator+(const vec<T, N>& a, T2 b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] + b;
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator+(T2 a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a + b._Elems[i];
	}
	return c;
}
template<typename T, size_t N>
vec<T, N> operator-(const vec<T, N>& a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] - b._Elems[i];
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator-(const vec<T, N>& a, T2 b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] - b;
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator-(T2 a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a - b._Elems[i];
	}
	return c;
}
template<typename T, size_t N>
vec<T, N> operator*(const vec<T, N>& a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] * b._Elems[i];
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator*(const vec<T, N>& a, T2 b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] * b;
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator*(T2 a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a * b._Elems[i];
	}
	return c;
}
template<typename T, size_t N>
vec<T, N> operator/(const vec<T, N>& a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] / b._Elems[i];
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator/(const vec<T, N>& a, T2 b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a._Elems[i] / b;
	}
	return c;
}
template<typename T, size_t N, typename T2>
vec<T, N> operator/(T2 a, const vec<T, N>& b) {
	vec<T, N> c;
	for (size_t i = 0; i < N; ++i) {
		c._Elems[i] = a / b._Elems[i];
	}
	return c;
}
template<typename T, size_t N>
const vec<T, N> vec<T, N>::zero(0);
namespace std {
	template<typename T, size_t N>
	istream& operator>>(istream& is, vec<T, N>& v) {
		return is >> static_cast<array<T, N>>(v);
	}
	template<typename T, size_t N>
	ostream& operator<<(ostream& os, const vec<T, N>& v) {
		return os << static_cast<array<T, N>>(v);
	}
	template<typename T, size_t N>
	struct hash<vec<T, N>> : public hash<array<T, N>> {
	};
}
typedef vec<double, 2> double2;
typedef vec<double, 3> double3;
typedef vec<int, 2> int2;
typedef vec<int, 3> int3;
namespace std {
	template<typename T>
	enable_if_t<is_integral<T>::value, long long> pow(long long base, T iexp) {
		if (iexp == 0) {
			return 1;
		}
		long long val = pow(base, iexp / 2);
		return val * val * (iexp % 2 ? base : 1);
	}
	template<typename T>
	enable_if_t<is_integral<T>::value, unsigned long long> pow(unsigned long long base, T iexp) {
		if (iexp == 0) {
			return 1;
		}
		long long val = pow(base, iexp / 2);
		return val * val * (iexp % 2 ? base : 1);
	}
}
class digitstring {
public:
	static const string base10;
	digitstring(const string& digitmap = base10) : digitmap_(digitmap.begin(), digitmap.end()) {
	}
	digitstring(const string& s, const string& digitmap = base10) : digitmap_(digitmap.begin(), digitmap.end()) {
		reset(s);
	}
	digitstring(long long val, size_t size, const string& digitmap = base10) : digitmap_(digitmap.begin(), digitmap.end()) {
		int base = (int)digitmap_.size();
		if (val < 0) {
			throw "digitstring: val < 0 : " + to_string(val);
		}
		digits_.resize(size);
		for (size_t i = 0; i < digits_.size(); ++i) {
			digits_[digits_.size() - 1 - i] = val % base;
			val /= base;
		}
		if (val != 0) {
			throw "digitstring: val is not exhausted: " + to_string(val) + " size: " + to_string(size);
		}
	}
	void reset(const string& s) {
		map<char, int> invmap;
		for (size_t i = 0; i < digitmap_.size(); ++i) {
			invmap[digitmap_[i]] = (int)i;
		}
		digits_.resize(s.size());
		for (size_t i = 0; i < digits_.size(); ++i) {
			if (invmap.count(s[i]) == 0) {
				throw "digitstring: invalid character from string: " + s;
			}
			digits_[i] = invmap[s[i]];
		}
	}
	size_t size() const {
		return digits_.size();
	}
	int at(size_t pos) const {
		return digits_[pos];
	}
	string str() const {
		ostringstream sb;
		for (int digit : digits_) {
			sb << digitmap_[digit];
		}
		return sb.str();
	}
	long long value() const {
		int base = (int)digitmap_.size();
		long long v = 0;
		for (int digit : digits_) {
			v = digit + base * v;
		}
		return v;
	}
private:
	vector<char> digitmap_;
	vector<int> digits_;
};
const string digitstring::base10("0123456789");
namespace std {
	istream& operator>>(istream& is, digitstring& v) {
		string s;
		is >> s;
		v.reset(s);
		return is;
	}
	ostream& operator<<(ostream& os, const digitstring& v) {
		return os << v.str();
	}
}

char cmap[3] = {'R','P','S'};

class Comb {
public:
	int n;
	int t;
	int order;
	Comb* left;
	Comb* right;
	Comb() {
		order = -1;
	}
	bool operator<(const Comb& o) const {
		if (order >= 0) {
			return order < o.order;
		}
		if (this == &o) {
			return false;
		}
		if (n == 0) {
			return cmap[t] < cmap[o.t];
		}
		if (*left < *o.left) {
			return true;
		}
		if (*o.left < *left) {
			return false;
		}
		return *right < *o.right;
	}
	void print(ostream& os) const {
		if (n == 0) {
			os << cmap[t];
		}
		else {
			left->print(os);
			right->print(os);
		}
	}
};

typedef pair<vec<int, 3>, int> Key;

const int nmax = 12;
typedef map<Key, Comb> Sol;
Sol sols[nmax];

bool Compute(int n, Key k, Comb& c) {
	int m = (1 << (n - 1));
	bool found = false;
	Sol& sol = sols[n - 1];
	for (int r = 0; r <= m; ++r) {
		for (int p = 0; p <= m - r; ++p) {
			int s = m - r - p;
			vec<int, 3> l{r,p,s};
			vec<int, 3> rv = k.first - l;
			if (rv[0] < 0 || rv[1] < 0 || rv[2] < 0) {
				continue;
			}
			for (int d = 0; d < 2; ++d) {
				Key lk{ l, k.second };
				Key rk{ rv, k.second};
				if (d == 0) {
					lk.second = (lk.second + 2) % 3;
				}
				else {
					rk.second = (rk.second + 2) % 3;
				}
				if (sol.count(lk) == 0 || sol.count(rk) == 0) {
					continue;
				}
				Comb c2;
				c2.n = n;
				c2.left = &sol[lk];
				c2.right = &sol[rk];
				if (!found || c2 < c) {
					c = c2;
					found = true;
				}
			}
		}
	}
	return found;
}

void Preprocess() {
	for (int i = 0; i < 3; ++i) {
		Comb c;
		Key k;
		c.n = 0;
		c.t = i;
		k.first = vec<int, 3>{ 0, 0, 0 };
		k.first[i] = 1;
		k.second = i;
		sols[0][k] = c;
	}
	for (int n = 1; n < nmax; ++n) {
		cerr << n << endl;
		int m = (1 << n);

		for (int r = m / 3; r <= m / 3 + 1; ++r) {
			for (int p = m / 3; p <= m / 3 + 1; ++p) {
				int s = m - r - p;
				vec<int, 3> l{ r,p,s };
				for (int t = 0; t < 3; ++t) {
					Key k{ l,t };
					Comb c;
					if (Compute(n, k, c)) {
						sols[n][k] = c;
					}
				}
			}
		}

		vector<pair<Comb, Key>> vks;
		for (auto& pr : sols[n]) {
			vks.push_back({pr.second, pr.first});
		}
		sort(vks.begin(), vks.end());
		for (int ind = 0; ind < vks.size(); ++ind) {
			sols[n][vks[ind].second].order = ind;
		}
		cerr << sols[n].size() << endl;
		for (auto& pr : sols[n]) {
			cerr << pr.first << endl;
		}
	}
}

void Solve(istream& is, ostream& os) {
	int n, r, p, s;
	is >> n >> r >> p >> s;
	vector<Comb> cs;
	vec<int, 3> l{ r,p,s };
	for (int t = 0; t < 3; ++t) {
		Key k{ l,t };
		Comb c;
		if (Compute(n, k, c)) {
			cs.push_back(c);
		}
	}
	if (cs.size() == 0) {
		os << "IMPOSSIBLE";
	}
	else {
		min_element(cs.begin(), cs.end())->print(os);
	}
}

int main(int argc, char** argv) {
	Preprocess();
	istream& is = cin;
	ostream& os = cout;
	int casecount = 0;
	is >> casecount;
	for (int i = 0; i < casecount; ++i) {
		try {
#if 0 // multiline output
			os << "Case #" << (i + 1) << ":" << endl;
			Solve(is, os);
#else
			os << "Case #" << (i + 1) << ": ";
			Solve(is, os);
			os << endl;
#endif
		}
		catch (const char* message) {
			cerr << "Error in Case #" << (i + 1) << ": " << message << endl;
			throw message;
		}
		catch (const string& message) {
			cerr << "Error in Case #" << (i + 1) << ": " << message << endl;
			throw message;
		}
	}
	if (is.fail()) {
		return 1;
	}
	return 0;
}
