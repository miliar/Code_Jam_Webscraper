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

#undef assert
#define assert my_assert

void my_assert(bool b)
{
	if (!b) __asm__("int $3");
}

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

enum Side {
	TOP, LEFT, RIGHT, BOTTOM
};

int R, C;
vector<vector<char>> field;
vector<pair<int, int>> posn;
vector<int> loves;

bool walk(int target, int r, int c, Side s)
{
	if (r < 0 || c < 0 || r >= R || c >= C)
	{
		return (mp(r, c) == posn[target]);
	}
	if (field[r][c] == '?')
	{
		if (s == TOP || s == BOTTOM)
			field[r][c] = '\\';
		else
			field[r][c] = '/';
		if (walk(target, r, c, s))
			return true;
		else
		{
			if (field[r][c] == '\\')
				field[r][c] = '/';
			else
				field[r][c] = '\\';
			return walk(target, r, c, s);
		}
	}
	if (field[r][c] == '\\')
	{
		if (s == TOP) return walk(target, r, c+1, LEFT);
		if (s == LEFT) return walk(target, r+1, c, TOP);
		if (s == BOTTOM) return walk(target, r, c-1, RIGHT);
		if (s == RIGHT) return walk(target, r-1, c, BOTTOM);
		assert(false);
	}
	assert(field[r][c] == '/');
	if (s == TOP) return walk(target, r, c-1, RIGHT);
	if (s == LEFT) return walk(target, r-1, c, BOTTOM);
	if (s == BOTTOM) return walk(target, r, c+1, LEFT);
	if (s == RIGHT) return walk(target, r+1, c, TOP);
	assert(false);
	return false;
}

void printField()
{
	ji(R)
	{
		jj(C)
		{
			if (field[i][j] == '?')
				cout << '/';
			else
				cout << field[i][j];
		}
		cout << endl;
	}
}

bool makePath(int courtier)
{
	int x, y;
	tie(x, y) = posn[courtier];
	Side s;

	// cerr << "makePath " << courtier << " [" << x << ' ' << y << ']' << endl;

	if (x < 0) ++x, s = TOP;
	else if (y < 0) ++y, s = LEFT;
	else if (x == R) --x, s = BOTTOM;
	else if (y == C) --y, s = RIGHT;
	else assert(false);

	bool b = walk(loves[courtier], x, y, s);
	return b;

	// printField();
}

int main()
{
	int T;
	cin >> T;
	jjl(ctest, T)
	{
		cin >> R >> C;
		loves = vector<int>(2 * (R + C) + 20, -1);
		posn = vector<PII> {{-200, -200}};
		jk(R + C) {
			int a, b;
			cin >> a >> b;
			loves[a] = b;
			loves[b] = a;
		}
		ji(C) posn.pb({-1, i});
		ji(R) posn.pb({i, C});
		ji(C) posn.pb({R, C - i - 1});
		ji(R) posn.pb({R - i - 1, -1});
		field = vector<vector<char>>(R, vector<char>(C, '?'));

		VI lovers;
		for (int i = 1; i <= 2 * (R + C); i++)
			lovers.pb(i);
		bool impossible = false;

		while (!lovers.empty())
		{
			vector<char> rem(lovers.size(), 0);
			ji(lovers.size()) if (!rem[i])
			{
				int j = i+1;
				if (j == lovers.size())
					j = 0;
				if (loves[lovers[i]] == lovers[j]) {
					if (!makePath(lovers[i])) {
						impossible = true;
						break;
					}
					rem[i] = rem[j] = true;
					++i;
				}
			}
			VI nv;
			ji(lovers.size()) if (!rem[i]) nv.pb(lovers[i]);
			if (lovers == nv || impossible)
			{
				impossible = true;
				break;
			}
			lovers = nv;
		}

		cout << "Case #" << (ctest + 1) << ":" << endl;
		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			printField();
		}
	}
}
