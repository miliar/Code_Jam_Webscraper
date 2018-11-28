/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
string s;
int mul(int x, int y)
{
    int cnt = 0;
    if(x < 0)
    {
        cnt++;
        x = -x;
    }
    if(y < 0)
    {
        cnt = (cnt+1)%2;
        y = -y;
    }
    int ans = 0;
    if(x == 1)
    {
        ans = y;
    }
    else if(y == 1)
    {
        ans = x;
    }
    else if(x == 2)
    {
        if(y == 2)
            ans = -1;
        else if(y == 3)
            ans = 4;
        else ans = -3;
    }
    else if(x == 3)
    {
        if(y == 2)
            ans = -4;
        else if(y == 3)
            ans = -1;
        else ans = 2;
    }
    else
    {
        if(y == 2)
            ans = 3;
        else if(y == 3)
            ans = -2;
        else ans = -1;
    }
    if(cnt&1)
        ans = -ans;
    return ans;
}
int dp[10005][10005];
int A[10005];
int l;
int memo[10005][4];
int calc(int pos, int f)
{
    //cout << pos << " " << f << endl;
    if(pos >= l)
        return 0;
    if(f == 3)
    {
        return (dp[pos][l-1] == 4);
    }
    int &ret = memo[pos][f];
    if(ret != -1)
        return ret;
    ret = 0;
    for(int i=pos;i<l;i++)
    {
        if(dp[pos][i] == f+1)
        {
            ret = max(ret, calc(i+1,f+1));
        }
    }
    return ret;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 0;
    while(t--)
    {
        memset(memo,-1,sizeof memo);
        int x;
        scanf("%d %d",&l,&x);
        string str;
        cin >> str;
        s = "";
        FOR(z,x)
        {
            s += str;
        }
        l = s.length();
        //cout<< s<< endl;
        FOR(i,l)
        {
            if(s[i] == 'i')
                A[i] = 2;
            else if(s[i] == 'j')
                A[i] = 3;
            else
                A[i] = 4;
        }
        FOR(i,l)
        {
            //int cnt = 0;
            int cur = 1;
            for(int j=i;j<l;j++)
            {
                //cout << cur << " * " << A[j] << " = " << mul(cur,A[j]) << endl;
                cur = mul(cur,A[j]);
                dp[i][j] = dp[j][i] = cur;
            }
        }
        /*FOR(i,l)
        {
            FOR(j,l)
            cout << dp[i][j] << " ";
            cout << endl;
        }*/
        int ans = calc(0,1);
        string pr = "NO";
        if(ans == 1)
            pr = "YES";
        kas++;
        printf("Case #%d: %s\n",kas,pr.c_str());
    }
return 0;
}
