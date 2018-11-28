/*
 * Author:  vawait
 * Created Time:  2016/4/9 10:01:27
 * Problem: test.cpp
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
#include<ctime>
using namespace std;
#define rep(i, a, b) for (lint i = (a); i <= (b); ++i)
#define red(i, a, b) for (lint i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sqr(x) ((x) * (x))
typedef long long lint;
int n , m;

void init()
{
    scanf("%d",&n);
    m = 0;
}

void calc(lint t)
{
    while ( t ) {
        m |= 1 << ( t % 10 );
        t /= 10;
    }
}

void work()
{
    if ( !n) {
        puts("INSOMNIA");
        return;
    }
    rep(i,1,10000000) {
        calc( i * n );
        if ( m == 1023 ) {
            printf("%lld\n",i*n);
            return;
        }
    }
}

int main()
{
    //freopen("a.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}
