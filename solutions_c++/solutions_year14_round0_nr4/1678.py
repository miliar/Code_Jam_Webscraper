#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define pb push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
typedef long long LL;
typedef pair<int,int> PII;
vector<double>a,b;



int solve1(int n){
    int l1=0,r1=n-1;
    int l2=0,r2=n-1;
    int ans=0;

    /*REP(i,n)    printf("%.3lf ",a[i]);
    puts("");
    REP(i,n)    printf("%.3lf ",b[i]);
    puts("");*/

    REP(i,n){
        if(a[l1] > b[l2] ){
            ans++;
            l1++;
            l2++;
        }else {
            l1++;
            r2--;
        }
    }
    return ans;
}
int solve2(int n){
    int l1=0,r1=n-1;
    int l2=0,r2=n-1;
    int ans=0;
    REP(i,n){
        if(a[r1] > b[r2])   {
            r1--;
            l2++;
            ans++;
        }else {
            r1--;
            r2--;
        }
    }
    return ans;
}


int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int casnum;
    cin>>casnum;
    int n;
    double x;
    FOR(cas,1,casnum){
        a.clear(),b.clear();
        cin>>n;
        REP(i,n)    {
            scanf("%lf",&x);
            a.pb(x);
        }
        REP(j,n){
            scanf("%lf",&x);
            b.pb(x);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        printf("Case #%d: %d %d\n",cas,solve1(n),solve2(n));
    }

    return 0;
}
