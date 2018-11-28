#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>
#include <algorithm>
#define LL long long
//#define LL __int64
#define ULL unsigned long long

#define abs(x) ((x)>0?(x):-(x))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define max3(a, b, c) (a>b?max(a, c):max(b, c))
#define min3(a, b, c) (a<b?min(a, c):min(b, c))
#define max4(a, b, c, d) max(max(a, b), max(c, d))
#define min4(a, b, c, d) min(min(a, b), min(c, d))
#define zero(x) (((x)>0?(x):-(x))<eps)

#define Ee 2.718281828459045
#define pi acos(-1.0)
#define eps 1e-8
#define INF 1 << 30
using namespace std;

int T;
int n, m;
bool Hash[20];
int a[20][20], b[20][20];

void Solve()
{
    scanf("%d", &T);
    int tt = 1;
    while(T--)
    {
        memset(Hash, false, sizeof(Hash));
        scanf("%d", &n);
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                scanf("%d", &a[i][j]);
                if(i+1 == n)
                {
                    Hash[a[i][j]] = true;
                }
            }
        }
        int cnt = 0;
        int Ans;
        scanf("%d", &m);
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                scanf("%d", &b[i][j]);
                if(i+1 == m)
                {
                    if(Hash[b[i][j]] == true)
                    {
                        Ans = b[i][j];
                        cnt++;
                    }
                }
            }
        }
        //printf("cnt = %d\n", cnt);
        printf("Case #%d: ", tt++);
        if(cnt == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(cnt == 1)
        {
            printf("%d\n", Ans);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
}

int main()
{
    freopen("A-small-attempt6.in", "r",stdin);
    freopen("data.out", "w", stdout);
    Solve();

    return 0;
}
