/*
 * cookie_clicker.cpp
 * Created on: 2014-04-13 02:06
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
using namespace std;

typedef vector< int > vi; 
typedef vector< vi > vvi;
typedef vector< string > vs;
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define For(i, a, b) for(int i = (a), _b = (b); i < _b; i++)
#define Rep(i, n) For(i, 0, n)

int main(void) {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        double c, f, x;
        cin >> c >> f >> x;
        double p = 2;
        double time = 0;
        while(x/p > (c/p) + (x/(p+f))) {
            time += c/p;
            p += f;
        }
        time += x/p;
        printf("Case #%d: %.7lf\n", t, time);
    }
    return 0;
}

