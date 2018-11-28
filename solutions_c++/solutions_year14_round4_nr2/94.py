#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1 << 30;
const double EPS = 1e-8;

int mini(vi& v, int st, int kon)
{
    int mm=v[st], ans=st;
    for(int i=st; i<=kon; i++)
    {
        if(v[i]<mm)
        {
            mm=v[i];
            ans=i;
        }
    }
    return ans;
}

void solve(int num)
{
    int n;
    int ans=0;
    cin>>n;
    vi v(n);
    for(int i=0; i<n; i++) cin>>v[i];
    int st=0, kon=n-1;
    for(int i=0; i+1<n; i++)
    {
        int pos=mini(v,st,kon);
        if(pos-st<=kon-pos)
        {
            for(int j=pos; j>st; j--)
            {
                v[j]=v[j-1];
                ans++;
            }
            st++;
        }
        else
        {
            for(int j=pos; j<kon; j++)
            {
                v[j]=v[j+1];
                ans++;
            }
            kon--;
        }
    }
    cout<<"Case #"<<num<<": "<<ans<<"\n";


}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

