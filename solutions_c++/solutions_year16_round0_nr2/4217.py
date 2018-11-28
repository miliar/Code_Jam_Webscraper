//
//  main.cpp
//  ProbB_RevengeThePancakes
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

const int oo = (int) 1e9;
const double PI = acos(-1);
const double EPS = 1e-9;


// index = (index + 1) % n; // index++; if (index >= n) index = 0;
// index = (index + n - 1) % n; // index--; if (index < 0) index = n - 1;

inline int roundToInt(double i){
    return (int)((double)i + 0.5);
}
#define CodeJam
#define LARGE

#define SMALL_FILE_IN "B-small-attempt0.in"
#define SMALL_FILE_OUT "B-small-attempt0.out"
#define LARGE_FILE_IN "B-large.in"
#define LARGE_FILE_OUT "B-large.out"

bool descComp(int i, int j){return i > j;};

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
    
    
    int TC;
    cin >> TC;
    int tc = 1;
    string line;
    getline(cin, line);
    vector<bool> bits;
    while (TC-- > 0) {
        getline(cin, line);
        for0(i, line.length()){
            bits.push_back(line[i] == '-'? false : true);
        }
        int flips = 0;
        while (!bits.empty()) {
            // remove all + from the end first
            auto tempIt = bits.end();
            for(__typeof(bits.begin()) it = bits.end() - 1; it >= bits.begin();--it){
                if (*it == true) {
                    tempIt--;
                }
                else
                    break;
            }
            bits.erase(tempIt, bits.end());
            if (!bits.empty()) {
                // we still have bits
                if (!bits[0]) {
                    // if the first is -, reverse and flip immediately
                    reverse(all(bits));
                    bits.flip();
                    flips++;
                }
                else{
                    // if the first is +, flip it and all + afterwards
                    auto it = bits.begin();
                    while (*it) {
                        *it = false;
                        it++;
                    }
                    flips++;
                }
            }
            
        }
        printCase(tc++);
        cout << flips << endl;
    }
    
    
    return 0;
}
