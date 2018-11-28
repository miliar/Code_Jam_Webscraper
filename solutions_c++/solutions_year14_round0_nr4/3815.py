/*
 * war.cpp
 * Created on: 2014-04-13 02:40
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

int solve(int n, double a[], double b[]) {
    int war = n-1;
    for(int i = n-1; i >= 0; i--) {
        if(a[i] < b[war])
            war--;
    }

    return war+1;
}

int main(void) {
    int T;
    cin >> T;
    for(int t = 1 ; t <= T; t++) {
        int n;
        cin >> n;
        double a[n], b[n];
        for(int i = 0; i < n; i++)
            cin >> a[i];
        for(int i = 0; i < n; i++)
            cin >> b[i];
        sort(a, a+n);
        sort(b, b+n);
        int war = solve(n, a, b);
        int dwar = solve(n, b, a);
        printf("Case #%d: %d %d\n", t, n - dwar, war);
    }
    return 0;
}

