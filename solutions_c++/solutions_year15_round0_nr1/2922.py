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
    freopen("/Users/arkanath/Downloads/A-large.in", "r",stdin);
    freopen("/Users/arkanath/Dropbox/XCode Projects/Codeforces/Problem A/out_large.txt", "w",stdout);
    string tt;
    cin >> tt;
    ll test = getlong(tt);
    repi(ttt, 0, test)
    {
        string mm;
        cin >> mm;
        ll m = getlong(mm);
        m++;
        string aar;
        cin >> aar;
        repi(i, 0, m)
        {
            arr[i] = aar[i]-'0';
        }
        ll ans = 0;
        ll tot = 0;
        repi(i, 0, m)
        {
            if(arr[i]!=0)
            {
                if(tot<i)
                {
                    ans+= i-tot;
                    tot = i;
                }
                tot += arr[i];
            }
        }
        cout << "Case #"<<ttt+1 << ": "<< ans << endl;
    }

    return 0;
}
