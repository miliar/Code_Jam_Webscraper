#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

#define MAXN
#define LSON(x) x << 1
#define INF 0x7fffffff
#define RSON(x) x << 1 | 1
using namespace std;

typedef long long LL;
int num[2000];
priority_queue<int> que;
int main()
{
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("hehe.txt", "w", stdout);
    int t; scanf("%d", &t);
    for(int curCase = 1; curCase <= t; curCase ++) {
        int x, r, c; scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: ", curCase);
        if(x == 1)
            printf("GABRIEL\n");
        else if(x == 4) {
            if(r < c) swap(r,c);
            if(r == 4 && c >= 3)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
        else if(x == 2)
        {
            if(r*c % 2 == 0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
        else
        {
            if(r*c % 3 == 0 && r*c != 3)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
    }
    return 0;
}


