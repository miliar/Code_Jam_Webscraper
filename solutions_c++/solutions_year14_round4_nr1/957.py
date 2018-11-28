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
#define sqr(x) ((x) * (x))
typedef long long lint;
int n , m , a[11000];

void init()
{
    scanf("%d%d",&n,&m);
    rep(i,1,n) scanf("%d",&a[i]);
    sort( a + 1 , a + n + 1 );
}

void work()
{
    int s = 0 , l = 1;
    red(i,n,1) if ( i >= l ) {
        if ( i > l && a[i] + a[l] <= m ) l ++;
        s ++;
    } 
    cout << s << endl;
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
