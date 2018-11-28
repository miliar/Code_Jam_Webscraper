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

typedef ModInt<long long, 1000000007> mint;
typedef long long ll;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;

double tieChance(vector<double> p)
{
	int n = p.size();
	vector<double> dp(n+1, 0);
	dp[0] = 1;
	for (double x : p)
	{
		vector<double> ndp(n+1, 0);
		ji(n)
		{
			ndp[i+1] += x * dp[i];
			ndp[i] += (1 - x) * dp[i];
		}
		dp = move(ndp);
	}
	return dp[n / 2];
}

pair<double, VI> bestChoice(vector<double> people, int K)
{
	int n = people.size();
	double best = -1;
	VI ans;
	jjl(msk, 1 << n) if (__builtin_popcount(msk) == K) {
		vector<double> nv;
		VI mems;
		ji(n) if (msk & (1 << i)) {
			nv.push_back(people[i]);
			mems.push_back(i);
		}
		double v = tieChance(nv);
		if (v > best) {
			best = v;
			ans = mems;
		}
	}
	return {best, ans};
}

int main()
{
	int T;
	cin >> T;
	jjl(ctest, T)
	{
		cout << "Case #" << (ctest + 1) << ": ";
		int N, K;
		cin >> N >> K;
		vector<double> vals(N);
		ji(N) cin >> vals[i];
		sort(vals.begin(), vals.end());
		double best = -1;
		ji(K+1) {
			vector<double> cvals;
			jj(i) cvals.push_back(vals[j]);
			jj(K-i) cvals.push_back(vals[N-j-1]);
			assert(cvals.size() == K);
			best = max(best, tieChance(cvals));
		}
		// double bval;
		// VI bchoice;
		// tie(bval, bchoice) = bestChoice(vals, K);
		// cerr << "Chosen: ";
		// for (int x : bchoice) {
		// 	cerr << x << ' ';
		// 	// cerr << vals[x] << ' ';
		// }
		// cerr << endl;
		// // cerr << "Not chosen: ";
		// // ji(N) {
		// // 	if (find(bchoice.begin(), bchoice.end(), i) == bchoice.end())
		// // 		cerr << vals[i] << ' ';
		// // }
		// // cerr << endl << endl;
		printf("%.10f\n", best);
	}
}
