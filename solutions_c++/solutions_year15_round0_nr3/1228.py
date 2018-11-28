#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

int m[5][5];

typedef vector<int>::const_iterator cit;

inline int sign(int a)
{
	return a < 0 ? -1 : 1;
}

inline int mult( int a, int b)
{
	assert( 1 <= abs(a) && abs(a) <= 4 && 1 <= abs(b) && abs(b) <= 4);
	return m[abs(a)][abs(b)] * sign(a) * sign(b);
}

int reduce(cit from, cit to)
{
	int res = 1;
	int sign = 1;
	for( auto it = from ; it != to ; ++it)
	{
		res = mult(res, *it);
		if ( res < 0 )
		{
			res = -res;
			sign = -sign;
		}
	}
	return res * sign;
}

vector<int> s2inds(string s)
{
	vector<int> inds(s.length());
	for( int i = 0; i < s.length() ; ++i)
	{
		switch ( s[i] )
		{
			case 'i' : inds[i] = 2; break;
			case 'j' : inds[i] = 3; break;
			case 'k' : inds[i] = 4; break;
			default  : throw std::exception("Unknown symbol");
		}
	}
	return inds;
}

bool testcase() {
	__int64 L, X;
	char ss[10005];
	int sz;
	cin >> L >> X;
	cin.getline(ss,1000);
	cin.getline(ss, L + 1);

	string s(ss);

	if ( L * X < 3 )
	{
		return false;
	}
	if ( L * X == 3 && s.compare("ijk") != 0 )
	{
		return false;
	}
	vector<int> is = s2inds(s);

	const int valL = reduce(is.cbegin(), is.cend());

	vector<int> s12;

	for( int i = 0 ; i < min((__int64)12,X) ; ++i)
	{
		s12.insert(s12.end(), is.cbegin(), is.cend());
	}

	cit it1 = s12.cbegin();
	cit it1end = s12.cbegin() + min( 4 * L, (__int64)(s12.cend() - s12.cbegin() - 2));
	int val1 = 1;
	while ( it1 != it1end )
	{
		val1 = mult(val1, *it1);
		
		if ( val1 == 2 )
		{
			cit it2 = it1 + 1;
			cit it2end = it1 + min( 4 * L, (__int64)(s12.cend() - it1 - 1));
			int val2 = 1;
			while ( it2 != it2end )
			{
				val2 = mult(val2, *it2);

				if ( val2 == 3 )
				{
					cit it3 = it2 + 1;
					int val3 = 1;

					while ( (it3 - s12.cbegin()) % L != 0)
					{
						val3 = mult(val3, *it3);
						it3++;
					}
					
					int togo = (X - (int)((it3 - s12.cbegin()) / L)) % 4;

					while (togo--)
					{
						val3 = mult(val3, valL);
					}
					if ( val3 == 4)
						return true;
					else
						return false;
				}
				it2++;
			}
			
		}
		it1++;
	}

	return false;
}

int main() {
	m[1][1] =  1; m[1][2] =  2; m[1][3] =  3; m[1][4] =  4;
	m[2][1] =  2; m[2][2] = -1; m[2][3] =  4; m[2][4] = -3;
	m[3][1] =  3; m[3][2] = -4; m[3][3] = -1; m[3][4] =  2;
	m[4][1] =  4; m[4][2] =  3; m[4][3] = -2; m[4][4] = -1;


 int n;
 cin >> n;
 for( int i = 0 ; i < n ; i++ )
	 cout << "CASE #" << i + 1 << ": " << (testcase() ? "YES" : "NO") << std::endl;
 return 0;
}