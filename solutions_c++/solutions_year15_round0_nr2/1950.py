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
#include <set>
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

int main () {
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        int d;
        cin >> d;
        int pancakes[d];
        for(int i = 0 ; i < d ; i++) {
            cin >> pancakes[i];
        }

        int ans = (1 << 30);
        for(int mx = *max_element(pancakes, pancakes + d) ; mx >= 1 ; mx--) {
            int tans = mx;
            for(int i = 0 ; i < d ; i++) {
                tans += (pancakes[i] - 1) / mx;
            }
            ans = min(ans, tans);
        }
        printf("Case #%d: %d\n", t, ans);
    }
}