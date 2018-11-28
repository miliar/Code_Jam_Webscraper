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
    LL c;
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
    LL len=0,buf[20];
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
    LL len=0,buf[20];
    while(x) {
        buf[len++]=x%10;
        x/=10;
    }
    if(!len)
        buf[len++]=0;
    while(len--)
        putchar(buf[len]+'0');
}
const LL N = 1e6+10;
LL n;


LL rev(LL x) {
    LL res = 0;
    while(x) {
        res =res * 10 + x % 10;
        x /= 10;
    }
    return res;
}

LL ten(LL x) {
    LL cnt = 0;
    while(x) {
        ++cnt;
        x/=10;
    }
    cnt = cnt/2 + cnt%2;
    LL res = 1;
    FOR(i,0,cnt)res *= 10;
    return res;
}

int main() {
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    LL T = getint();
//    for(LL cas = 1 ; cas <= T ; ++cas) {
//        n = getint();
//        answer = 0;
//        while(n) {
//            if(rev(n)>=n || n % 10 == 0) {
//                ++answer;
//                --n;
//            }
//            else
//                n = rev(n);
//        }
//        printf("Case #%d: %d\n",cas,F[n]);
//    }
    FOR(cas,1,T+1) {
        n = getint();
        LL answer = 0;

        while(n) {
            LL k = ten(n);
            LL target = n/k*k+1;
            if(target<=n) {
                answer += n-target;
                n = target;
                target = rev(target);
                if(target < n) {
                    n = target;
                    ++answer;
                } else {
                    --n;
                    ++answer;
                }
            } else {
                --n;
                ++answer;
            }
        }
        printf("Case #");
        write(cas);
        printf(": ");
        writeln(answer);
    }
}

