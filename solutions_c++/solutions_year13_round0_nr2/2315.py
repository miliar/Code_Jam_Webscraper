#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXN = 120;

int mat[MAXN][MAXN];
int n,m;

bool lineCheck(int i,int h) {
    for(int a=0;a<m;++a) if(mat[i][a] > h) return 0;
    return 1;
}

bool columnCheck(int i,int h) {
    for(int a=0;a<n;++a) if(mat[a][i] > h) return 0;
    return 1;
}

int main() {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        scanf("%d%d",&n,&m);
        for(int a=0;a<n;++a)
            for(int b=0;b<m;++b)
                scanf("%d",&mat[a][b]);
        bool ok = 1;
        for(int h=1;h<=100;++h) {
            for(int a=0;a<n;++a)
                for(int b=0;b<m;++b) 
                    if(mat[a][b] == h && !lineCheck(a,h) && !columnCheck(b,h)) ok = 0;
        }
        printf("Case #%d: %s\n",t, ok ? "YES" : "NO");
    }          
    return 0;
}
