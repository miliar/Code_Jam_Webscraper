#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
	    int x, mask = 0;
	    cin >> x;
	    --x;
	    REP(i, 4) {
	        REP(j, 4) {
	            int a;
	            cin >> a;
	            --a;
	            if (i == x) {
	            	mask |= 1 << a;
	            }
	        }
	    }

	    cin >> x;
	    --x;
	    int num = 0, result;
	    REP(i, 4) {
	        REP(j, 4) {
	            int a;
	            cin >> a;
	            --a;
	            if (i == x) {
	                if (mask & (1 << a)) {
	                    num++;
	                    result = a;
	                }
	            }
	        }
	    }
	    cout << "Case #" << nowCase << ": ";
	    if (num == 1) {
	    	cout << result + 1 << endl;
	    } else {
	        cout << (num ? "Bad magician!" : "Volunteer cheated!") << endl;
	    }
	}

	return 0;
}