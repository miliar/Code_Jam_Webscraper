

	
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <deque>
	//#include <time.h>
	//#include <fstream>
	//#include <windows.h>
	//#include <stdint.h>
	using namespace std;
#define FIX 0.000000000001
#define INF 2000000000
#define PI (2.0 * acos ( 0.0 ))
#define forn(i,s,n) i = (s); for( int _n = (int)(n), _di = (i > _n)?-1:1; i != _n; i += _di)
#define foreach(it,c) for ( auto it = (c).begin(); it!=(c).end(); it++)
#define sz(x) (int)((x).size())
#define pb(x) push_back((x))

#define BIN__N(x) (x) | x>>3 | x>>6 | x>>9
#define BIN__B(x) (x) & 0xf | (x)>>12 & 0xf0
#define BIN8(v) (BIN__B(BIN__N(0x##v)))

	struct sxz
	{
		int Pi;
		int del;
		int res;
	};

	int main()
	{
		FILE *slovar;
		FILE *out;
		freopen_s(&slovar, "7.in", "r", stdin);
		freopen_s(&out, "2.txt", "w", stdout);
		int T, D;
		sxz	x[1001];
		int ti, i, j, k;
		int summ, minsumm;
		cin >> T;
		forn(ti, 0, T)
		{
			cin >> D;
			//memset(x, 0, sizeof(sxz) * 1001);
			forn(i, 0, D)
			{
				cin >> x[i].Pi;
				x[i].res = x[i].Pi;
				x[i].del = 1;
			}

			sort(x, x + D, [](sxz &a, sxz &b){ return a.Pi > b.Pi; });
			minsumm = summ = x[0].res;

			forn(k, 1, 500)
			{
				x[0].del++;
				x[0].res = ceil(x[0].Pi / ((float)x[0].del));
				forn(i, 0, D - 1)
				{
					if (x[i].res < x[i + 1].res)
						swap(x[i], x[i + 1]);
					else
						break;
				}

				summ = k + x[0].res;
				minsumm = min(summ, minsumm);
			}
			cout << "Case #" << ti+1 << ": " << minsumm << endl;
		}

		return 0;
	}