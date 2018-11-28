#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;
typedef long long LL;
typedef vector<LL> VLL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

enum class QuaternionType
{
	I,
	J,
	K,
	ONE
};

struct Quaternion
{
	bool negative;
	QuaternionType type;

	Quaternion() { }
	Quaternion(bool negative, QuaternionType type)
	{
		this->negative = negative;
		this->type = type;
	}
	Quaternion operator*(const Quaternion& other)
	{
		Quaternion q;
		if(type == QuaternionType::ONE)
		{
			q =  Quaternion(false, other.type);
		}
		else if(other.type == QuaternionType::ONE)
		{
			q =  Quaternion(false, type);
		}
		else if(type == other.type)
		{
			q =  Quaternion(true, QuaternionType::ONE);
		}
		else if(type == QuaternionType::I)
		{
			if(other.type == QuaternionType::J)
			{
				q =  Quaternion(false, QuaternionType::K);
			}
			else if(other.type == QuaternionType::K)
			{
				q =  Quaternion(true, QuaternionType::J);
			}
		}
		else if(type == QuaternionType::J)
		{
			if(other.type == QuaternionType::I)
			{
				q =  Quaternion(true, QuaternionType::K);
			}
			else if(other.type == QuaternionType::K)
			{
				q =  Quaternion(false, QuaternionType::I);
			}
		}
		else if(type == QuaternionType::K)
		{
			if(other.type == QuaternionType::I)
			{
				q =  Quaternion(false, QuaternionType::J);
			}
			else if(other.type == QuaternionType::J)
			{
				q =  Quaternion(true, QuaternionType::I);
			}
		}
		if(negative ^ other.negative) q.negative = !q.negative;
		return q;
	}
	bool operator==(const Quaternion& other)
	{
		return type == other.type && negative == other.negative;
	}
	bool operator!=(const Quaternion& other)
	{
		return type != other.type || negative != other.negative;
	}
};

ostream& operator<<(ostream& out, const Quaternion& obj)
{
	if(obj.negative)
		out << "-";
	switch(obj.type)
	{
	case QuaternionType::ONE:
		out << "1";
		break;
	case QuaternionType::I:
		out << "i";
		break;
	case QuaternionType::J:
		out << "j";
		break;
	case QuaternionType::K:
		out << "k";
		break;
	}
	return out;
}

int main()
{
	int t;
	cin >> t;
	FOR(o, 1, t)
	{
		int l, n;
		string str;
		cin >> l >> n >> str;
		vector<Quaternion> q(n * l);
		REP(i, n)
		{
			REP(x, l)
			{
				QuaternionType type;
				if(str[x] == 'i') type = QuaternionType::I;
				else if(str[x] == 'j') type = QuaternionType::J;
				else type = QuaternionType::K;
				q[i * l + x] = Quaternion(false, type);
			}
		}
		Quaternion k = q[0];
		FOR(x, 1, SIZE(q) - 1)
		{
			k = k * q[x];
		}
		cout << "Case #" << o << ": ";
		if(k == Quaternion(true, QuaternionType::ONE))
		{
			k = q[0];
			int b = 0;
			while(k != Quaternion(false, QuaternionType::I) && b < SIZE(q) - 1)
			{
				k = k * q[++b];
			}
			k = q[SIZE(q) - 1];
			int e = SIZE(q) - 1;
			while(k != Quaternion(false, QuaternionType::K) && e > b)
			{
				k = q[--e] * k;
			}
			if(b < e)
			{
				cout << "YES\n";

				k = Quaternion(false, QuaternionType::ONE);
				FOR(x, b + 1, e - 1)
				{
					k = k * q[x];
				}
				if(k != Quaternion(false, QuaternionType::J)) cout << "WTF?!" << endl;
			}
			else
				cout << "NO\n";
		}
		else
		{
			cout << "NO\n";
		}
	}
	return 0;
}