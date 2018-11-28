/*
Author : SRIRAM S
*/
// Libs 
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
#include <cassert>
#include <cstring>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,A,n) for(int i=A;i<n;i++)
#define sz(c) (signed int) c.size()
#define pb(c) push_back(c)
#define INF (int) 1e9
#define all(c) c.begin(),c.end()
#define GI(t) scanf("%d",&t)
#define VI vector<int>
#define PII pair <int,int>
typedef long long LL;

using namespace std;

int main() {
    int t,a,b;
    GI(t);
    int first[4][4], second[4][4];
    REP(te,t) {
        GI(a);
        REP(i,4) REP(j,4) GI(first[i][j]); 
        GI(b);
        REP(i,4) REP(j,4) GI(second[i][j]); 
        VI possible(4);
        VI answer;
        REP(j,4) possible.pb(first[a-1][j]);
        int idx = 0;
        while(idx < sz(possible)) {
            int num = possible[idx];
            bool flag = false;
            REP(j,4) if(second[b-1][j] == num) flag = true;
            if(flag) answer.pb(num);
            idx++;
        }
        printf("Case #%d: ",te+1);
        if(sz(answer) == 0) cout<<"Volunteer cheated!\n";
        else if(sz(answer) > 1) cout<<"Bad Magician!\n";
        else cout<<answer[0]<<endl;
    }
    return 0;
}
