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

void solve(int num)
{
    int n, x;
    cin>>n>>x;
    vi v(n);
    for(int i=0; i<n; i++) cin>>v[i];
    sort(v.begin(), v.end());
    int last=n-1;
    int najs=0;
    for(int i=0; i<n; i++)
    {
        while(last>i && v[i]+v[last]>x) last--;
        if(last>i && v[i]+v[last]<=x)
        {
            najs++;
            last--;
        }
    }
    cout<<"Case #"<<num<<": "<<n-najs<<"\n";


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

