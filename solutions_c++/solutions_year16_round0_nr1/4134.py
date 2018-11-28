//
//  main.cpp
//  ProbA_CountingSheep
//
//  Created by Hossam Ghareeb on 4/9/16.
//  Copyright © 2016 Hossam Ghareeb. All rights reserved.
//

#include <cstring>
#include <string.h>
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

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define for0(i,m) for(int i=0;i<(int)(m);i++)
#define forN(i,n,m) for(int i=n;i<(int)(m);i++)
#define iterate(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define first(x) (*x).first
#define second(x) (*x).second

#define printCase(i) printf("Case #%d: ", i)
#define printEndLine cout << endl

//Code Jam

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long long ll;
typedef long double ld;

const double PI = acos(-1);
const double EPS = 1e-9;


// index = (index + 1) % n; // index++; if (index >= n) index = 0;
// index = (index + n - 1) % n; // index--; if (index < 0) index = n - 1;

inline int roundToInt(double i){
    return (int)((double)i + 0.5);
}
#define CodeJam
#define LARGE

#define SMALL_FILE_IN "A-small-attempt0.in"
#define SMALL_FILE_OUT "A-small-attempt0.out"
#define LARGE_FILE_IN "A-large.in"
#define LARGE_FILE_OUT "A-large.out"



ll solve(int N){
    ll num = N;
    int checker = 0;
    ll times = 1;
    while (true) {
        num  = N * times;
        ll temp = num;
        while (temp > 0) {
            int digit = temp % 10;
            checker |= (1 << digit);
            temp /= 10;
        }
        if (checker == 1023) {
            return num;
        }
        times++;
    }
    return num;
}

int main(int argc, const char * argv[]) {
    
#ifdef CodeJam
#ifdef SMALL
    freopen(SMALL_FILE_IN, "rt", stdin);
    freopen(SMALL_FILE_OUT, "wt", stdout);
#endif
#ifdef LARGE
    freopen(LARGE_FILE_IN, "rt", stdin);
    freopen(LARGE_FILE_OUT, "wt", stdout);
#endif
#endif
    //////
    
    
    int TC, N;
    cin >> TC;
    int tc = 1;
    while (TC-- > 0) {
        cin >> N;
        printCase(tc++);
        if (N == 0) {
            cout << "INSOMNIA";
        }
        else{
            ll sol = solve(N);
            cout << sol;
        }
        printEndLine;
    }
    
    return 0;
}
