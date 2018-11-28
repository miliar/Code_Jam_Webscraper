/*
 * magic_trick.cpp
 * Created on: 2014-04-12 16:49
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
        int p1, p2;
        int a[4][4], b[4][4];
        cin >> p1;
        for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++)
            cin >> a[i][j];
        cin >> p2;
        for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++)
            cin >> b[i][j];
        int c = 0;
        int x = -1;
        p1--, p2--;
        for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++)
            if(a[p1][i] == b[p2][j]) { c++; x = a[p1][i]; }
        if(c == 1)
            printf("Case #%d: %d\n", t, x);
        else if(c > 1)
            printf("Case #%d: Bad magician!\n", t);
        else
            printf("Case #%d: Volunteer cheated!\n", t);
    }
    return 0;
}

