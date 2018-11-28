#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#define _USE_MATH_DEFINES
#include <math.h>
#include <assert.h>
#include <cstdlib>
#include <algorithm>
#include <list>

#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define LL long long
#define S(n) scanf("%d", &n)
#define Sa(n,i) scanf("%d", n+i)
#define N 2001
#define MOD 1000000007

using namespace std;



int main(){
#ifndef ONLINE_JUDGE
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    
    int T;
    S(T);
    
    for(int _t=1; _t <= T; ++_t){
        int a, b;
        int c[4][4];
        S(a);
        forn(i, 4) forn(j, 4) scanf("%d", &(c[i][j]));
        set<int> possible;
        forn(i, 4) possible.insert(c[a-1][i]);
        S(b);
        forn(i, 4) forn(j, 4) scanf("%d", &(c[i][j]));
        int count = 0, val = -1;
        forn(i, 4) if(possible.count(c[b-1][i])) count += 1, val = c[b-1][i];
        if(count == 0)
            printf("Case #%d: Volunteer cheated!\n", _t);
        else if(count == 1)
            printf("Case #%d: %d\n", _t, val);
        else
            printf("Case #%d: Bad magician!\n", _t);
            
    }
    
    
    return 0;
}

