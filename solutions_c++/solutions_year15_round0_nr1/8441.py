#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <ctype.h>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <set>

using namespace std;

#define ll long long int
#define mem(a, b) memset(a,b,sizeof(a))
#define eps 1e-10
#define PI acos(-1)
#define pb(n) push_back(n)
#define MAX 1000009

int dirx[8]= {-1, 0, 1, -1, 1, -1, 0, 1};
int diry[8]= {-1, -1, -1, 0, 0, 1, 1, 1};

int dx[4]= {-1, 0, 1, 0};
int dy[4]= {0, -1, 0, 1};

int min(int x, int y)
{
    if( x<y) return x;
    else return y;
}

int max(int x, int y)
{
    if( x>y) return x;
    else return y;
}

char a[1005];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tCase, s, cnt, i, t=1, sum, x;
    scanf("%d", &tCase);
    while(tCase--) {
        scanf("%d %s", &s, a);
        cnt = 0;
        sum = 0;
        for(i=0 ; i <= s ; i++) {
            x = 0;
            if(i > sum) {
                x = i-sum;
            }
            cnt += x;
            sum += a[i] - '0' +x;
            //printf("x=%d cnt=%d sum=%d\n", x, cnt, sum);
        }
        printf("Case #%d: %d\n", t++, cnt);
    }
    return 0;
}
