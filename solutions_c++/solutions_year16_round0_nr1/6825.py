#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <fstream>
using namespace std;
 
#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back
 
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}


set<int> getNumbers(int n, set<int> st) {
    while(n) {
        st.insert(n%10);
        n /= 10;
    }
    return st;
}

int main()
{
    
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    
    int cases;
    scanf("%d", &cases);
    REP(k, cases) {
        int n;
        set<int> st;
        bool INSOMNIA = false;
        int res = -1;
        scanf("%d", &n);
        if(n == 0) INSOMNIA = true;
        else {
            for(int i=1;;i++) {
                st = getNumbers(n*i, st);
                if(st.size() == 10) {
                    res = n * i;
                    break;
                }
            }
        }

        printf("Case #%d: ", k + 1);
        if(INSOMNIA) printf("INSOMNIA");
        else printf("%d", res);
        printf("\n");

    }
    return 0;
}
 
