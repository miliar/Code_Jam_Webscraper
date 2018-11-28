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

void sortarr(vector<int> &a, string &alpha) {
    REP(i, a.size()) {
        FOR(j, i + 1, a.size()) {
            if(a[i] < a[j]) {
                swap(a[i], a[j]);
                swap(alpha[i], alpha[j]);
            }
        }
    }
}

int count1(vector<int> a) {
    int c = 0;
    REP(i, a.size()) if(a[i]==1) c++;
    return c;
}

bool valid(vector<int> a) {
    sort(rALL(a));
    int max = a[0];
    int c = 0;
    REP(i,a.size()) c+=a[i];
    c-=max;
    if(max > c) return false;
    return true; 
}

int main()
{
    
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    
    int cases;
    scanf("%d", &cases);
    REP(k, cases) {
        int n; scanf("%d",&n);
        vector<int> a;
        vector<string> plan;
        REP(i,n) {
            int tmp; scanf("%d",&tmp);
            a.PB(tmp);
        }
        string alpha = "";
        REP(i,a.size()) alpha.PB('A' + i);
        printf("Case #%d:", k + 1);
        while(true) {
            sortarr(a, alpha);
            if(a[0] == 0) break;
            string tmpPlan;
            tmpPlan.PB(alpha[0]);
            a[0]--;
            if(!valid(a)) { tmpPlan.PB(alpha[1]); a[1]--; }
            cout<<" "<<tmpPlan;
        }
        
        
        printf("\n");
    }
    return 0;
}
 
