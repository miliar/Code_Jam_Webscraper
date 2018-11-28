/* Author: Sandeep */

/* 1. Did u interpret the qns correctly ?
   2. Is your i/o correct ?
   3. Int overflow, double precesion
   4. Array size correct ?
   5. Clearing/resetting vector, map etc.
   6. Stack ovrflow
   7. Global/local conflict
   8. Check for obvious typo(most imp)
   9. Think about edge cases
*/

#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define ford(i, a, b, c)        for(int i=(a); i<(b); i+=(c))
#define fori(i, a, b)           ford(i,a,b,1)
#define rep(i, n)               fori(i,0,n)
#define ifor(i, a, b)           for(int i=(a); i>=(b); i--)
#define iter(i, a)              for(typeof((a).begin()) i=(a).begin(); i!=(a).end(); i++)
#define si(x)                   ((int)x.size())
#define SS                      ({int x;scanf("%d",&x);x;})
#define pb                      push_back
#define mp                      make_pair
#define all(a)                  a.begin(),a.end()
#define fill(a, v)              memset(a, v, sizeof(a))
#define inf                     (int)1e9
#define linf                    (long long)1e18
#define V                       vector
#define S                       string
#define XX                      first
#define YY                      second
#define P(v)                    rep(i, si(v)) cout<<v[i]<<" "; puts("")

typedef V<int> vi;
typedef V<S> vs;
typedef long long ll;
typedef pair<int,int> pii;

ll powModN(ll a, ll b, ll c) {
    ll res = 1;
    while (b){
        if (b%2) res= (res*(ll)a)%c;
        b/=2;
        a=(a*(ll)a)%c;
    }
    return res;
}

/* Program Body starts here */
int getMinVal (int **array, int row, int col) {
	int minVal = 1001;
	rep(i,row) {
		rep(j,col) {
			if(array[i][j] != -1 && array[i][j]<minVal) {
				minVal = array[i][j];
			}
		}
	}
	if(minVal == 1001) {
		return -1;
	}
	return minVal;
}

int getMinRow (int **array, int row, int col, int minVal) {
	rep(i,row) {
		bool containsMinVal = false;
		bool allMinVal = true;
		rep(j,col) {
			if(array[i][j] != -1 && array[i][j] != minVal) {
				allMinVal = false;
				break;
			} else if(array[i][j] == minVal) {
				containsMinVal = true;
			}
		}
		if(allMinVal == false) {
			continue;
		} else {
			if(containsMinVal) {
				return i;
			}
		}
	}
	return -1;
}

int getMinCol (int **array, int row, int col, int minVal) {
	rep(j,col) {
		bool containsMinVal = false;
		bool allMinVal = true;
		rep(i,row) {
			if(array[i][j] != -1 && array[i][j] != minVal) {
				allMinVal = false;
				break;
			} else if(array[i][j] == minVal) {
				containsMinVal = true;
			}
		}
		if(allMinVal == false) {
			continue;
		} else {
			if(containsMinVal) {
				return j;
			}
		}
	}
	return -1;
}

void updateRow(int **array, int col, int minRow) {
	rep(i,col) {
		array[minRow][i] = -1;
	}
}

void updateCol(int **array,int row, int minCol) {
	rep(i,row) {
		array[i][minCol] = -1;
	}
}

bool solve (int **array, int row, int col) {
	//cout<<"Inside Solve"<<endl;
	int minVal;
	while ((minVal = getMinVal(array,row,col)) != -1) {
		int rowMin = getMinRow(array,row,col,minVal);
		int colMin = getMinCol(array,row,col,minVal);
		//cout<<"Min Val is "<< minVal<<" rowMin "<<rowMin<<" colMin "<<colMin<<endl;
		//cin.get();
		if (rowMin == -1 && colMin == -1) {
			return false;
		} else if(rowMin != -1) {
			updateRow(array,col,rowMin);
		} else {
			updateCol(array,row,colMin);
		}
	}
	return true;
}

string main2 () {
	int numRow, numCol;
	cin>>numRow>>numCol;
	int **array = new int* [numRow];
	rep(i,numRow) {
		array[i] = new int [numCol];
	}
	rep(i,numRow) {
		rep(j,numCol) {
			cin>>array[i][j];
		}
	}
	return (solve(array,numRow,numCol) ? "YES" : "NO");
}

int main () {
	int T;
	cin >> T;
	rep (i,T) {
		cout<<"Case #"<<i+1<<": "<<main2()<<endl;
	}
}
