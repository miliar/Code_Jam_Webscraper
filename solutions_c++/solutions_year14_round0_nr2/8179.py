/* Paras Narang 
 *
 */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

#define oo 0x7F7F7F7F
#define LET(x,a)     __typeof(a) x(a)
#define EACH(it,v)   for(LET(it,v.begin());it!=v.end();++it)
#define REP(i,n)     for(__typeof(n) i(0); i<n; i++)
#define FOR(i,j,n)   for(__typeof(n) i(j); i<n; i++)
#define ALL(x)       (x).begin(), (x).end()
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back
#define mp           make_pair

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

int main() {
    int t; gint(t);
    REP(ti, t) {
    	double C, F, X;
    	cin >> C >> F >> X;
    	double min = X;
    	double sum1 = 0.0, sum2 = X/2.0;
    	int noOfFarms = 0;
    	while(sum2 < min){
    		min = sum2;
    		noOfFarms++;
    		sum1 += (C/(2+((noOfFarms-1)*F)));
    		sum2 = sum1 + (X/(2+(noOfFarms*F)));
    	}
    	printf("Case #%d: %.7lf\n", ti+1, min);
    }
    return 0;
}
