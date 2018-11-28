//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//defines-general
typedef long long ll;
typedef long double ld;
#define to(a) __typeof(a)
#define fill(a,val)  memset(a,val,sizeof(a))
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)

//defines-vector
typedef vector<int> vi;
typedef vector<long long> vll;
#define all(vec)  vec.begin(),vec.end()
#define pb push_back
#define sz size()
#define contains(vec,x) (find(vec.begin(),vec.end(),x)!=vec.end())

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)

//defines-pair
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define ff first
#define ss second
#define mp make_pair

string getstring(ll in)
{
    stringstream ss;
    ss << in;
    string ans;
    ss >> ans;
    return ans;
}

ll getlong(string in)
{
    stringstream ss;
    ss << in;
    ll ans;
    ss >> ans;
    return ans;
}
ll arr[1005];
int main()
{
    freopen("/Users/arkanath/Downloads/B-large.in", "r",stdin);
    freopen("/Users/arkanath/Dropbox/XCode Projects/Codeforces/Problem B/out_large.txt", "w",stdout);
    int test;
    cin >> test;
    repi(ttt, 0, test)
    {
        ll d;
        cin >> d;
        repi(i, 0, d)
        {
            cin >> arr[i];
        }
        ll ansmin = 10000000;
        repi(mmm, 1, 1001)
        {
            ll ans=mmm;
            repi(j, 0, d)
            {
                if(arr[j]>mmm)
                {
                    ans += (arr[j]-mmm)/mmm;
                    if((arr[j]-mmm)%mmm!=0) ans ++;
                }
            }
            ansmin = min(ansmin,ans);
        }
        cout << "Case #"<<ttt+1 << ": "<< ansmin << endl;
    }

    return 0;
}
