#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 



// BEGIN CUT HERE
int main(int argc, char* argv[])
{

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	int T;
	cin >> T;

	REP(t, T)
	{
		string cakes;
		int k;
		cin >> cakes >> k;

		int r = 0;
		bool possible = true;

		REP(i, cakes.size())
		{
			if (cakes[i] == '-')
			{
				if (i + k-1 < cakes.size())
				{
					r++;
					REP(j, k)
					{
						if (cakes[i + j] == '+')
							cakes[i + j] = '-';
						else if (cakes[i + j] == '-')
							cakes[i + j] = '+';
					}
				}
				else
					possible = false;
			}
		}

		if (possible)
			cout << "Case #" << (t + 1) << ": " << r << endl;
		else
			cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;

	}


}
// END CUT HERE
