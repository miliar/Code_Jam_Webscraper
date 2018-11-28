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

string solve( vector<int> & selected, vector<int> & selected2 )
{
	string ret = "";
	stringstream ss("");
	ll cnt = 0;
	ll match = 0;

	Rep( i, selected.size() ){
		Rep( j, selected2.size() ){
			if( selected[i] == selected2[j] ){
				cnt++;
				ss << selected[i];
				break;
			}
		}
	}

	if( cnt == 1 ){
		ss >> ret;
	}
	else if( cnt == 0 ){
		ret = "Volunteer cheated!";
	}
	else{
		ret = "Bad magician!";
	}

	return ret;
}

int main()
{
	ll T = 0;
	ll first = 0, second = 0;
	vector<int> tmp(4, 0);
	vector<int> selected(4, 0);
	vector<int> selected2(4, 0);
	vector<string> ret;

	cin >> T;

	Rep(t, T){
		cin >> first;
		Rep(i, 4){
			cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];
			if( i + 1 == first ){
				selected = tmp;
			}
		}

		cin >> second;
		Rep(i, 4){
			cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];
			if( i + 1 == second ){
				selected2 = tmp;
			}
		}
		ret.push_back( solve(selected, selected2) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		cout << ret[t] << endl;
	}

	return 0;
}



