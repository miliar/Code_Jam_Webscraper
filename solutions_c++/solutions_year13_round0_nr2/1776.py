#include <cstdio>
#include <iostream>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define ss(n) scanf("%d",&n)
int ar[110][110];
int check(int n, int m, int x, int y)
{
    int temp = ar[x][y], possible_hor = 1, possible_ver = 1;
    FOR(i,0,m-1)
    {
        if(ar[x][i] > temp) {possible_hor = 0; break;}
    }
    FOR(i,0,n-1)
    {
        if(ar[i][y] > temp) {possible_ver = 0; break;}
    }
return possible_hor|possible_ver;
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int tc, n, m, ret, possible, cnt = 1;
    ss(tc);
    while(tc--)
    {   FOR(i,0,100) {FOR(j,0,100) ar[i][j] = 0;}
        possible = 1;
        ss(n); ss(m);
        FOR(i,0,n-1)
        {
            FOR(j,0,m-1)
            ss(ar[i][j]);
        }
        FOR(i,0,n-1)
        {
            FOR(j,0,m-1)
            {
               ret = check(n, m, i, j);
               if(ret == 0) {possible = 0; break;}
            }
            if(possible == 0) break;
        }
        if(possible == 1)  printf("Case #%d: YES\n",cnt);
        if(possible == 0)  printf("Case #%d: NO\n",cnt);
        cnt++;
    }
return 0;
}
