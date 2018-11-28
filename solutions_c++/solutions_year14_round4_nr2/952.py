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
#define x first
#define y second
typedef long long lint;
int n , m;
pair < int , int > a[1100];

void init()
{
    scanf("%d",&n);
    rep(i,1,n) scanf("%d",&a[i].x) , a[i].y = i;
    sort( a + 1 , a + 1 + n );
}

void work()
{
    int s = 0;
    rep(i,1,n) {
        int l = 0 , r = 0;
        rep(j,i+1,n) if ( a[j].y < a[i].y ) l ++ ; else r ++;
        s += min( l , r );
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
