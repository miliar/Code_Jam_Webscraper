//
//  main.cpp
//  ProbC_CoinJam
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
typedef vector<ll> vll;

const int oo = (int) 1e9;
const double PI = acos(-1);
const double EPS = 1e-9;


// index = (index + 1) % n; // index++; if (index >= n) index = 0;
// index = (index + n - 1) % n; // index--; if (index < 0) index = n - 1;

inline int roundToInt(double i){
    return (int)((double)i + 0.5);
}
#define CodeJam
#define SMALL

#define SMALL_FILE_IN "C-small-attempt1.in"
#define SMALL_FILE_OUT "C-small-attempt1.out"
#define LARGE_FILE_IN "C-large-practice.in"
#define LARGE_FILE_OUT "C-large-practice.out"

bool descComp(int i, int j){return i > j;};

ll isPrime(ll num){
    ll  i;

    for(i=2;i<=sqrt(num);++i)
    {
        if(num%i==0)
        {
            return i;
        }
    }
    return 0;
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
    
    
    int TC, N, J;
    cin >> TC >> N >> J;
    int tc = 1;
    
    while (TC-- > 0) {
        printCase(tc++);
        printEndLine;
        
            for (ll i = pow(2, N-1) + 1; (i < (pow(2, N) - 1)); i++) {
                if(!(i & 1)) continue;
                if (J == 0) {
                    break;
                }
                ll d = isPrime(i);
                vll divs;
                if (d) {
                    divs.pb(d);
                }
                bitset<128> bits(i);
                forN(j, 3, 11){
                    ll sum = 0;
                    int com = 0;
                    for0(x, N){
                        if (bits[x]) {
                            sum += pow(j, x);
                        }
                        com++;
                    }
                    d = isPrime(sum);
                    if (d) {
                        divs.pb(d);
                        continue;
                    }
                    else
                        break;
                }
                if (divs.size() == 9) {
                    // we have solution
                    J--;
                    for(int b = N - 1; b >=0; b--){
                        cout << (bits[b]);
                    }
                    iterate(it, divs){
                        cout << " " << *it;
                    }
                    printEndLine;
                }
                
            }
    }
    
    
    return 0;
}
