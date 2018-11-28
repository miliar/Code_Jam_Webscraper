
#include<sstream>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<complex>
#include<cmath>
#include<iostream>
#include<iomanip>
#include<string>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<string.h>
#include<assert.h>
#include<time.h>

#define in freopen("input.txt", "r", stdin);
#define out freopen("output.txt", "w", stdout);
#define clr(arr, key) memset(arr, key, sizeof arr)
#define pb push_back
#define mp(a, b) make_pair(a, b)
#define PI acos(-1)
#define CF ios_base::sync_with_stdio(0);
#define all(v) v.begin(), v.end()
#define no_of_ones __builtin_popcount // count 1's in a numbers binary representation
#define SZ(v) (int)(v.size())
#define eps 10e-7
#define oo 1.7e306
#define N 100010
#define mod 1000000007
#define re(i,a) for(int i=0; i<a; i++)
#define ll long long
#define eps 1e-9


//int col[8] = {0, 1, 1, 1, 0, -1, -1, -1};
//int row[8] = {1, 1, 0, -1, -1, -1, 0, 1};
//int col[4] = {1, 0, -1, 0};
//int row[4] = {0, 1, 0, -1};
//int months[13] = {0, ,31,28,31,30,31,30,31,31,30,31,30,31};

using namespace std;

int dp[1000005];

int rec(int n)
{
    if(n==1) return 1;

    int &ret=dp[n];
    if(ret!=-1) return ret;

    vector<int> v;
    int t,t2;
    t=n;
    v.clear();
    while(t>0)
    {
        v.pb(t%10);
        t/=10;
    }
    if(v[0]!=0)
    {
        t2=0;
        for(int i=0; i<v.size(); i++) t2=t2*10+v[i];
    }
    else t2=n;
    if(t2>=n) t2=n-1;

    ret=1+min(rec(n-1),rec(t2));

    return ret;
}
int main()
{
    in
    out

    int T,n;


    cin>>T;
    clr(dp,-1);
    for(int cs=1; cs<=T; cs++)
    {
        cin>>n;
        printf("Case #%d: %d\n",cs,rec(n));
    }
    return 0;
}
