////////////////////////////////////////////////////////////////////
// This source code is for Visual C++ 2010 Express
////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <stack>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <deque>
#include <math.h>
#include "UnionFind.h"

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;
struct Point{
	ll x;
	ll y;
	Point() {};
	Point( ll xx, ll yy ) : x(xx), y(yy) {};
};

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

string solve( vector< vector<int> > & field, const int N, const int M )
{
	set<int> heights;
	set<int>::iterator itr;
	Rep(i, N){
		Rep(j, M){
			heights.insert(field[i][j]);
		}
	}

	for( itr = heights.begin(); itr != heights.end(); ++itr ){
		int num = *itr;

		Rep(i, N){
			Rep(j, M){
				if( field[i][j] != num ) continue;

				// check field[i][j]
				bool ok = false;
				Rep(k, N){
					if( field[k][j] > field[i][j] ){
						break;
					}

					if(k == N - 1){
						ok = true;
					}
				}
				Rep(k, M){
					if( field[i][k] > field[i][j] ){
						break;
					}

					if(k == M - 1){
						ok = true;
					}
				}

				if( ok == false ){
					return "NO";
				}
			}
		}
	}

	return "YES";
}

int main()
{
	int T = 0;
	int N = 0, M = 0;
	vector< string > ans;

	cin >> T;

	Rep(t, T){
		cin >> N >> M;
		vector< vector<int> > field(N, vector<int>(M, INF) );
		Rep(i, N){
			Rep(j, M){
				cin >> field[i][j];
			}
		}
		ans.push_back( solve(field, N, M) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		cout << ans[t] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



