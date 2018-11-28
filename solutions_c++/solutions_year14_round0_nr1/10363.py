#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>
#include<sstream>
#include<ctype.h>
#include<vector>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
#include<set>

#define pb push_back
#define PI acos(-1.0)
#define SZ(a) (int)a.size()
#define csprnt printf("Case %d: ", cas++);
#define EPS 1e-9
#define MAX 100010
#define ll long long
#define INF (1<<30)
#define pii pair<int, int>
#define MP make_pair
int xx[] = {1,1,0,-1,-1,-1,0,1}, yy[] = {0,1,1,1,0,-1,-1,-1}; //eight direction

ll BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;}

using namespace std;

int num[20];
int grid[5][5];

int main()
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int t, cas=1;
    scanf("%d", &t);
    while(t--)
    {
        memset(num, false, sizeof num);
        int i, j, x, y, val;
        scanf("%d", &x);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d", &val);
                if(i==x) num[val]=1;
            }
        }
        int tot=0, ans;
        scanf("%d", &y);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d", &val);
                if(i==y)
                {
                    if(num[val]==1)
                    {
                        tot++;
                        ans = val;
                    }
                }
            }
        }
        printf("Case #%d: ", cas++);
        if(tot==1) printf("%d\n", ans);
        else if(tot==0) printf("Volunteer cheated!\n");
        else if(tot>1) printf("Bad magician!\n");
    }
    return 0;
}

