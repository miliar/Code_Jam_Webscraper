/*
 * Author:  vawait
 * Created Time:  2015/4/11 10:47:20
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
int n;
char a[100000];

void init()
{
    int sum = 0 , ans = 0;
    scanf("%d%s",&n,a);
    rep(i,0,n) {
        int x = a[i] - '0';
        if ( sum < i ) ans += i - sum , sum = i;
        sum += x;
    }
    printf("%d\n",ans);
}

void work()
{
}

int main()
{
    freopen("1.out","w",stdout);
    int t;
    cin >> t;
    rep(i,1,t) {
        printf("Case #%d: ",i);
        init();
        work();
    }
    return 0;
}
