#pragma comment(linker, "/STACK:1677721600")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <algorithm>
#define pb push_back
#define mp make_pair
#define LL long long
#define lson lo,mi,rt<<1
#define rson mi+1,hi,rt<<1|1
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define mem(a,b) memset(a,b,sizeof(a))
#define FIN freopen("in.in", "r", stdin)
#define FOUT freopen("out.out", "w", stdout)
#define rep(i,a,b) for(int i=(a); i<=(b); i++)
#define dec(i,a,b) for(int i=(a); i>=(b); i--)

using namespace std;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const double ee = exp(1.0);
const int inf = 0x3f3f3f3f;
const int maxn = 1e6 + 10;
const double pi = acos(-1.0);

int readT()
{
    char c;
    int ret = 0,flg = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

LL readTL()
{
    char c;
    int flg = 0;
    LL ret = 0;
    while(c = getchar(), (c < '0' || c > '9') && c != '-');
    if(c == '-') flg = 1; else ret = c ^ 48;
    while( c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c ^ 48);
    return flg ? - ret : ret;
}

struct Node{
    char c;
    int num;
    Node(char _c, int _num){
        c = _c;
        num = _num;
    }
    bool operator < (const Node& other) const{
        return num < other.num;
    }
} ;

int main()
{
    #ifdef LOCAL
    FIN;
    FOUT;
    #endif // LOCAL
    int ncase =readT();
    int ca = 1;
    while (ncase--){
        int n = readT();
        priority_queue<Node> q;
        rep(i, 0, n - 1){
            int t = readT();
            q.push(Node('A' + i, t));
        }
        printf("Case #%d: ", ca++);
        while (!q.empty()){
            Node a = q.top();
            q.pop();
            Node b = q.top();
            q.pop();
            if (a.num == b.num && a.num != 1){
                printf("%c%c", a.c, b.c);
                q.push(Node(a.c, a.num - 1));
                q.push(Node(b.c, b.num - 1));
            }
            if (a.num != b.num)
            {
                q.push(b);
                printf("%c", a.c);
                q.push(Node(a.c, a.num - 1));
            }
            if (a.num == b.num && a.num == 1){
                if (q.size() & 1){
                    q.push(b);
                    printf("%c", a.c);
                }
                else{
                    printf("%c%c", a.c, b.c);
                }
            }
            if (q.empty()){
                printf("\n");
            }
            else{
                printf(" ");
            }
        }

    }
    return 0;
}
