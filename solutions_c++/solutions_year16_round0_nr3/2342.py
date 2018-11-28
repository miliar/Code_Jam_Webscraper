/*
 * Author:  vawait
 * Created Time:  2016/4/9 12:00:29
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
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define clr( x , y ) memset(x,y,sizeof(x))
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sqr(x) ((x) * (x))
typedef long long lint;
int n , m , a[60];

void init()
{
    cin >> n;
    cin >> n >> m;
    a[1] = a[n] = 1;
}

void work()
{
    puts("Case #1:");
    int k = n - 2 >> 1;
    rep(i,0,100000) {
        rep(j,1,k) a[j<<1] = a[j<<1|1] = i >> ( j - 1 ) & 1;
        red(j,n,1) printf("%d",a[j]);
        rep(j,3,11) printf(" %d",j);
        puts("");
        m --;
        if ( !m ) break;
    }
}

int main()
{
    //freopen("a.out","w",stdout);
    init();
    work();
    return 0;
}
