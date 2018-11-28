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

pair<ll, ll> solve( ll N, vector<double> & naomi, vector<double> & ken )
{
	pair<ll, ll> ret;
	vector< bool > kenUse1(N, false);
	vector< bool > kenUse2(N, false);

	// sort
	sort( naomi.begin(), naomi.end() );
	sort( ken.begin(), ken.end() );

	// Deceitful War
	Rep(i, N){
		double tmpNaomi = naomi[i];
		ll kenIndex = 0;

		Rep(j, N){
			if( !kenUse1[j] ){
				kenIndex = j;
				if( tmpNaomi >= ken[j] ){
					ret.first++;
					break;
				}
			}
		}

		kenUse1[kenIndex] = true;
	}

	// War
	Rep(i, N){
		double tmpNaomi = naomi[i];
		bool isNaomiWin = true;
		ll kenIndex = N - 1;

		Rep(j, N){
			if( !kenUse2[j] ){
				if( ken[j] >= tmpNaomi ){
					isNaomiWin = false;
					break;
				}
			}
		}

		if( isNaomiWin ){
			// Naomi win
			Rep(j, N){
				if( !kenUse2[j] ){
					kenIndex = j;
					break;
				}
			}
			ret.second++;
		}
		else{
			// Ken win
			for( ll j = N - 1; j >= 0; --j ){
				if( !kenUse2[j] ){
					if( tmpNaomi >= ken[j] ){
						break;
					}
					else{
						kenIndex = j;
					}
				}
			}
		}

		kenUse2[kenIndex] = true;
	}


	return ret;
}

int main()
{
	ll T = 0;
	ll N = 0;
	vector< pair<ll, ll> > ret;
	vector< double > naomiBlock;
	vector< double > kenBlock;

	cin >> T;

	Rep(t, T){
		cin >> N;
		naomiBlock.resize(N);
		kenBlock.resize(N);

		Rep(n, N){
			cin >> naomiBlock[n];
		}
		Rep(n, N){
			cin >> kenBlock[n];
		}
		ret.push_back( solve(N, naomiBlock, kenBlock) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		cout << ret[t].first << " " << ret[t].second << endl;
	}

	return 0;
}



