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
    
    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    
    int cases;
    string s; getline(cin, s);
    sscanf(s.c_str(),"%d",&cases);
    REP(k, cases) {
        getline(cin, s);
        while(s[s.size() - 1] == '+') s.erase(s.end() - 1);

        int change = 0;
        for(int i = 1; i < s.size(); i++) if(s[i] != s[i-1]) change++;
        int res = change + 1;
        if(change == 0 && s.size() == 0) {
            res = 0;
        }
        printf("Case #%d: %d\n", k + 1, res);
    }
    return 0;
}
 
