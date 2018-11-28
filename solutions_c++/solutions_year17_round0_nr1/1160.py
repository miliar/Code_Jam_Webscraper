/*
 * Author:  vawait
 * Created Time:  六  4/ 8 16:53:12 2017
 * File Name: a.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
using namespace std;
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define sqr(x) ((x) * (x))
#define mp make_pair
#define pb push_back
#define db pop_back
typedef long long lint;
const int maxn = 10000;
int n , k , a[maxn];
char s[maxn];

void init()
{
    scanf("%s",s+1);
    n = strlen( s + 1 );
    rep(i,1,n) a[i] = s[i] == '+' ? 0 : 1;
    cin >> k;
}

void work()
{
    int ans = 0;
    rep(i,1,n-k+1) if ( a[i] ) {
        ans ++;
        rep(j,i,i+k-1) a[j] ^= 1;
    }
    rep(i,1,n) if ( a[i] ) {
        puts("IMPOSSIBLE");
        return;
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}
