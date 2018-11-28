#include <iostream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <assert.h>
#include <map>
#include <queue>
#include <cstring>
using namespace std;

#define vi vector<int>
#define vvi vector< vector<int> >
#define pi pair<int,int>
#define pb push_back
#define out(a) cout<<(a)<<'\n'
#define sz(c) (int)(c).size()
#define isBit(n,i) ( ((n) >> (i)) & 1 )
#define fill(arr, v) memset(arr, v, sizeof(arr))
template<typename t1, typename t2> ostream& operator <<(ostream& os, const pair<t1, t2>& a) {os << a.first << ' ' << a.second;return os;}
template<typename typ> void vout(vector<typ>& v){for(int vint=0;vint<sz(v);vint++){cout<<(v)[vint];if(vint==sz(v)-1) cout<<'\n';else cout<<' ';}}
template<typename typ> void arrout(typ* arr,int l){for(int i=0;i<l;i++){cout<<arr[i];if(i<l-1) cout <<' ';else cout<<'\n';}}

#ifdef DEBUG
    #define debug(args...)            {dbg,args; cerr<<'\n';}
#else
    #define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger{template<typename T> debugger& operator , (const T& v) {cerr<<v<<" ";return *this;}}dbg;

int multiply[8 * 8];

int get(int, int);
void setVal(int a, int b, int v = -1) {
    if( v >= 0 ) {
        multiply[a * 8 + b] = v;
        return;
    }
    setVal(a, b, (((a >= 4 ^ b >= 4) ? 4 : 0) + get(a % 4, b % 4)) % 8);
}

int get(int a, int b) {
    if( multiply[a * 8 + b] < 0 ) {
        setVal(a, b);
    }
    return multiply[a * 8 + b];
}

int getForMul(int a, int c) {
    for(int i = 0 ; i < 8 ; i++) {
        if( get(a, i) == c ) {
            return i;
        }
    }
}

int main() {
    fill(multiply, -1);

    setVal(0, 1, 2);
    setVal(1, 0, 6);
    setVal(0, 2, 5);
    setVal(2, 0, 1);
    setVal(1, 2, 0);
    setVal(2, 1, 4);

    setVal(3, 3, 3);
    for(int i = 0 ; i <= 2 ; i++) {
        setVal(i, i, 7);
        setVal(i, 3, i);
        setVal(3, i, i);
    }

    // for(int i = 0 ; i < 8 ; i++) {
    //     for(int j = 0 ; j < 8 ; j++) {
    //         cout << "first " << i << ' ' << j << ' ' << endl << get(i, j) << endl;
    //     }
    // }
    // return 0;

    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        int l, x;
        cin >> l >> x;
        string s;
        cin >> s;
        int v[l];
        for(int i = 0 ; i < l ; i++) {
            v[i] = s[i] - 'i';
        }

        int dp[l * x + 1];
        dp[l * x - 1] = v[l - 1];
        for(int i = l * x - 2 ; i >= 0 ; --i) {
            dp[i] = get(v[i % l], dp[i + 1]);
        }

        int first = 3;
        bool works = false;
        for(int i = 0 ; i < l * x ; i++) {
            first = get(first, v[i % l]);

            if( first == 0 ) {
                int second = 3;
                for(int j = i + 1 ; j < l * x ; j++) {
                    second = get(second, v[j % l]);

                    if( second == 1 ) {
                        if( dp[j + 1] == 2 ) {
                            works = true;
                        }
                    }
                }
            }
        }

        printf("Case #%d: %s\n", t, works ? "YES" : "NO");
    }
}