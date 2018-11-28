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
using namespace std;

#pragma comment(linker, "/STACK:102400000,102400000")

typedef long long LL;
typedef pair<int ,int > pii;

#define CLR(x,y) memset(x,y,sizeof(x));
#define PB push_back
#define MP make_pair
#define FOR(i,x,y) for(int i = (x) ; i < (y) ; ++i)
#define ROF(i,x,y) for(int i = (y)-1 ; i >= (x); --i)
#define FORG(i,x,g) for(int i = g.head[(x)] ; ~i ; i = g.next[i])
#define INF 0x3f3f3f3f

inline LL getint() {
    int c;
    while(c=getchar(),(c<'0'||c>'9')&&(c!='-')&&(c!=EOF));
    if(c==EOF)return -1;
    bool flag=(c=='-');
    if(flag)
        c=getchar();
    LL x=0;
    while(c>='0'&&c<='9') {
        x = (x<<3)+x+x+c-'0';
        c=getchar();
    }
    return flag?-x:x;
}

inline void writeln(LL x) {
    if(x<0) {
        putchar('-');
        x=-x;
    }
    int len=0,buf[20];
    while(x) {
        buf[len++]=x%10;
        x/=10;
    }
    if(!len)
        buf[len++]=0;
    while(len--)
        putchar(buf[len]+'0');
    putchar('\n');
}

inline void write(LL x) {
    if(x<0) {
        putchar('-');
        x=-x;
    }
    int len=0,buf[20];
    while(x) {
        buf[len++]=x%10;
        x/=10;
    }
    if(!len)
        buf[len++]=0;
    while(len--)
        putchar(buf[len]+'0');
}
const int N = 20;
int r,c,n,s,S;
bool apart[N][N];
int answer;
int binary_count(int x) {
    int res = 0;
    while(x) {
        ++res;
        x -= x&(-x);
    }
    return res;
}

void paint(int s) {
    FOR(i,0,r) {
        FOR(j,0,c) {
            apart[i][j] = s>>(i*c+j)&1;
        }
    }
}

int check() {
    int res = 0;
    FOR(i,0,r) {
        FOR(j,0,c) {
            if(apart[i][j]) {
                if(i>0 && apart[i-1][j])++res;
                if(j>0 && apart[i][j-1])++res;
            }
        }
    }
    return res;
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T = getint();
    for(int cas = 1 ; cas <= T ; ++cas) {
        r = getint();
        c = getint();
        n = getint();
        S = r*c;
        answer = INT_MAX;
        for(int s = 0; s < (1<<S) ; ++s) {
            if(binary_count(s) != n) continue;
            paint(s);
            answer = min(answer,check());
        }
        printf("Case #%d: %d\n",cas,answer);
    }
}

