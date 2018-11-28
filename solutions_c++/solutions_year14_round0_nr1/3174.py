#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include<stack>
#include<queue>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n)  for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)    a.begin(),a.end()
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
int main()
{
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0.out","wt",stdout);
    int T;
    si(T);
    for(int t=1;t<=T;t++)
    {
        int N,c=0;
        si(N);
        int ma[4][4];
        set<int> se;
        vector<int> v;
        se.clear();
        rep(i,4)
            rep(j,4)
                si(ma[i][j]);
        rep(i,4)
            se.insert(ma[N-1][i]);
        si(N);
        rep(i,4)
            rep(j,4)
                si(ma[i][j]);
        rep(i,4)
        {
            if(se.find(ma[N-1][i])!=se.end())
            {
                c++;
                v.pb(ma[N-1][i]);
            }
        }
        if(c==1)
            printf("Case #%d: %d\n",t,v[0]);
        else if(c==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else
            printf("Case #%d: Bad magician!\n",t);

    }
    return 0;
}
