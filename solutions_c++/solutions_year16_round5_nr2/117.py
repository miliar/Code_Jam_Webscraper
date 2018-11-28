#include <bits/stdc++.h>
using namespace std;

#define jjs(i, s, x) for (int i = (s); i < int(x); ++i)
#define jjl(i, x) jjs(i, 0, x)
#define ji(x) jjl(i, x)
#define jj(x) jjl(j, x)
#define jk(x) jjl(k, x)
#define jij(a, b) ji(a) jj(b)
#define jjdescent(i, s, e) for (int i = (s)-1; i >= int(e); --i)
#define jjrev(i, s) jjdescent(i, s, 0)
#define foreach(x, C) for (auto& x : (C))
#define INF ((int) 1e9+10)
#define LINF ((long long) 1e16)
#define pb push_back
#define mp make_pair

#define rint readInteger
template<typename T>
bool readInteger(T& x)
{
	char c, r = 0, n = 0;
	x = 0;
	while (true)
	{
		c = getchar();
		if (c < 0 && !r)
			return 0;
		else if (c == '-' && !r)
			n = 1;
		else if (c >= '0' && c <= '9')
			x = x * 10 + c - '0', r = 1;
		else if (r)
			break;
	}
	if (n)
		x = -x;
	return 1;
}

template<typename T>
vector<T> readIntegral(int n)
{
	vector<T> ret(n);
	for (int i = 0; i < n; i++)
		readInteger(ret[i]);
	return ret;
}

auto readInts = readIntegral<int>;
auto readLongs = readIntegral<long long>;

template <typename T, T MOD>
struct ModInt
{
	T value;
	ModInt() : value(0)
	{}
	ModInt(T x)
	{
		x %= MOD;
		if (x < 0)
			x += MOD;
		value = x;
	}

public:
	ModInt& operator += (ModInt x)
	{
		value += x.value;
		if (value >= MOD)
			value -= MOD;
		return *this;
	}
	ModInt& operator -= (ModInt x)
	{
		value -= x.value;
		if (value < 0)
			value += MOD;
		return *this;
	}
	ModInt& operator *= (ModInt x)
	{
		value *= x.value;
		value %= MOD;
		return *this;
	}
	ModInt& operator /= (ModInt x)
	{
		x.invert();
		return *this *= x;
	}

	ModInt operator + (ModInt x) const
	{
		ModInt o = *this;
		o += x;
		return o;
	}
	ModInt operator - (ModInt x) const
	{
		ModInt o = *this;
		o -= x;
		return o;
	}
	ModInt operator * (ModInt x) const
	{
		ModInt o = *this;
		o *= x;
		return o;
	}
	ModInt operator / (ModInt x) const
	{
		ModInt o = *this;
		o /= x;
		return o;
	}
	bool operator == (ModInt x) const
	{
		return value == x.value;
	}
	bool operator != (ModInt x) const
	{
		return !(*this == x);
	}

	ModInt operator - () const
	{
		return ModInt(0) - *this;
	}

	ModInt operator ^ (long long x) const
	{
		ModInt ret = 1 % MOD;
		ModInt mul = *this;
		while (x)
		{
			if (x & 1)
				ret *= mul;
			mul *= mul;
			x >>= 1;
		}
		return ret;
	}
	ModInt& operator ^= (long long x)
	{
		return *this = *this ^ x;
	}

private:
	void invert()
	{
		*this ^= MOD-2;
	}
public:
	void answer()
	{
		std::cout << value << std::endl;
	}
};

default_random_engine gen;

typedef ModInt<long long, 1000000007> mint;
typedef long long ll;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;

int randint(int a, int b)
{
	return uniform_int_distribution<int>(a, b)(gen);
}

vector<char> interleave(vector<vector<char>>& qs)
{
	vector<char> ret;
	int n = qs.size();
	while (!qs.empty())
	{
		int tot = 0;
		int idx = -1;
		ji(qs.size()) {
			assert(!qs[i].empty());
			tot += qs[i].size();
			if (randint(1, tot) <= qs[i].size()) {
				idx = i;
			}
		}
		assert(idx >= 0);
		ret.pb(qs[idx].back());
		qs[idx].pop_back();
		if (qs[idx].empty()) {
			qs.erase(qs.begin() + idx);
		}
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

VVI child;
string nameFor;

vector<char> generate(int x)
{
	vector<vector<char>> v;
	foreach(o, child[x])
		v.push_back(generate(o));
	auto q = interleave(v);
	q.push_back(nameFor[x]);
	return q;
}

int main()
{
	int T;
	cin >> T;
	int per = CLOCKS_PER_SEC * 60 / T;
	jjl(tcase, T)
	{
		int N;
		cin >> N;
		++N;
		child = VVI(N);
		jjs(i, 1, N) {
			int x;
			cin >> x;
			child[x].pb(i);
		}
		cin >> nameFor;
		nameFor = string("~" + nameFor);
		int M;
		cin >> M;
		vector<string> cool(M);
		ji(M) cin >> cool[i];
		VI matches(M);
		auto start = clock();
		int total_runs = 0;
		while (total_runs < 5000 || clock() - start < per) {
			auto gv = generate(0);
			reverse(gv.begin(), gv.end());
			string s(gv.begin(), gv.end());
			ji(M) {
				if (s.find(cool[i]) != string::npos)
					++matches[i];
			}
			++total_runs;
		}
		cout << "Case #" << (tcase + 1) << ":";
		ji(M) {
			cout << ' ' << ((double) matches[i] / total_runs);
		}
		cout << endl;
		cerr << total_runs << endl;
	}
}
