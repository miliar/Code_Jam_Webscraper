// google-code-jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>



using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

#define SMALL

int N,nx;


int _tmain(int argc, _TCHAR* argv[])
{
#ifdef TEST
	freopen("./data/2013/B-small.in", "rt", stdin);
	freopen("./data/2013/B-small.out", "wt", stdout);
#endif
#ifdef SMALL
	freopen("./data/2013/B-small-attempt1.in", "rt", stdin);
	freopen("./data/2013/B-small-attempt1.out", "wt", stdout);
#endif

#ifdef LARGE
	freopen("./data/2013/B-large.in", "rt", stdin);
	freopen("./data/2013/B-large.out", "wt", stdout);
#endif
	cin >> N;
	for (int nn=1; nn<=N; nn++){
		
		char playgroung[100][100];
		int x = 0;
		int y = 0;
		cin >> y;
		cin >> x;
		for (int row=0; row<y; row++) {
			for (int col=0; col<x; col++) {
				cin >> playgroung[row][col];
				//cout << playgroung[row][col];
			}
			//cout << endl;
		}
		cout << "Case #" << nn << ": ";
		bool pased = true;
		for (int row=0; row<y; row++) {
			for (int col=0; col<x; col++) {
				bool pased_row = true;
				bool pased_col = true;
				// for each point check row posibility
				for (int checkedrow_col = 0; checkedrow_col<x; checkedrow_col++){
					if (playgroung[row][col] < playgroung[row][checkedrow_col]) {
						pased_row = false;
					}
				}

				if (pased_row) {
					continue;
				}

				// for each point check row posibility
				for (int checkedcol_row = 0; checkedcol_row<y; checkedcol_row++){
					if (playgroung[row][col] < playgroung[checkedcol_row][col]) {
						pased_col = false;
					}
				}

				if ((pased_row) || (pased_col)) {
					// posible to cut this field
					continue;
				}
				else {
					// imposible to cut
					pased = false;
					break;
				}
			}
			if (!pased) {
				break;
			}
		}


		// write results
		if (pased) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}
	return 0;
}

