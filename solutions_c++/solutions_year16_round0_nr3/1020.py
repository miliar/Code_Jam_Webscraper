#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <math.h>
#include <iomanip>
#include <bitset>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long LL;
typedef pair<int,int> pii;
#define CLR(x,y) memset(x,y,sizeof(x));
#define PB push_back
#define MP make_pair
#define FOR(i,x,y) for(int i = (x) ; i < (y) ; ++i)
#define ROF(i,x,y) for(int i = (y)-1 ; i >= (x); --i)
#define FORG(i,x,g) for(int i = g.head[(x)] ; ~i ; i = g.next[i])
#define INF 0x3f3f3f3f

int T,cases;


int p[10] = {2,3,5,7,11,13,17,23,29,31};
int base[12][10];
int mod[12][10];
int n,m;

void p2(LL x) {
    if(x!=0)p2(x>>1);
    else return;
    printf("%d",x&1);
}


void print(LL x) {
    //printf("%d\n",x);
    p2(x);
    printf(" ");
    for(int i = 2 ; i <= 10 ; ++i) {
        for(int j = 0 ; j < 10 ; ++j)
        if(mod[i][j] == 0) {
            printf("%d%c", p[j], " \n"[i==10]);
            break;
        }
    }
}

bool check(LL x) {
    LL tmp = x;
    for(int i = 2 ; i <= 10 ; ++i)
        for(int j = 0 ; j < 10 ; ++j) {
            base[i][j] = 1;
            mod[i][j] = 0;
        }
    for(; x ; x>>=1) {
        int t = x&1;
        for(int i = 2 ; i <= 10 ; ++i) {
            for(int j = 0 ; j < 10 ; ++j) {
                mod[i][j] += t*base[i][j];
                mod[i][j] %= p[j];
                base[i][j] *= i;
                base[i][j] %= p[j];
            }
        }
    }
    for(int i = 2 ; i <= 10 ; ++i) {
        bool flag = 0;
        for(int j = 0 ; j < 10 ; ++j) if(mod[i][j] == 0)flag = 1;
        if(!flag)return false;
    }

    print(tmp);
    --m;
    return true;
}

void solve() {
    for(LL i = (1LL<<n-1) ; i < (1LL<<n) ; ++i) {
        i|=1;
        check(i);
        if(m==0) {
            //printf("YES\n");
            break;
        }
    }
}

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&T);
    for(cases = 1 ; cases <= T ; ++cases) {
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n", cases);
        solve();
    }
}
