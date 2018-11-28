
#include <algorithm>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

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

int main(int argc, char* argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);


	int T;
	cin >> T;


	REP(t, T)
	{
		int N, M;
		cin >> N >> M;

		cout << "Case #" << (t+1) << ": ";

		VVI field(N, VI(M));

		REP(i, N)
		{
			REP(j, M)
			{
				cin >> field[i][j];
			}
		}

		bool can = true;


		REP(i, N)
		{
			REP(j, M)
			{
				if (field[i][j] == 1)
				{
					bool row = true;
					REP(k, M)
					{
						if (field[i][k] != 1)
							row = false;
					}

					bool col = true;
					REP(k, N)
					{
						if (field[k][j] != 1)
							col = false;
					}

					if (!row && !col)
						can = false;
					
				}
			}
		}


		if (can)
			cout << "YES\n";
		else
			cout << "NO\n";



	}






}