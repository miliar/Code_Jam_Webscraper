#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)
#define sfd(x) scanf("%d",&x)
#define pf printf

#define LL long long
#define ll long long
#define LD long double
#define ld long double
#define PB push_back
#define pb push_back
#define MP make_pair
#define mp make_pair
#define F first
#define S second

typedef pair<int,int> PII;
typedef vector<int> VI;

#define pii pair<int,int>
#define vi vector<int>
#define fr(i,n) for( int i=0; i<=n; i++)
#define frm(i,m,n) for(int i=m; i<=n; i++)

void in()
{

}
long double c,f,x;
long double ans,bns;
int arr[1000000];
void solve()
{
    cin>>c>>f>>x;
   long double r = 2.0,bns = c;
    int cnt = 0;
   long  double ans = 0.0,cns = x/2.0;
    while(bns<=x)
    {
        bns = (c*(r+f))/f;
        cnt ++;
        ans += c/r;
        r = r+f;
        cns = min(cns,ans+ (x*1.0)/r);
    }
    printf("%.8f\n",float(cns));
}

int main()
{
    freopen("a.txt","r",stdin);
    freopen("sola.txt","w",stdout);
    int t,q=1;
    cin>>t;
    while(t--){
        printf("Case #%d: ",q++);
        // in();
    solve();
    }
}
