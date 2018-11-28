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
    int d;
    cin >> d;
    vi v(d);
    for(int i=0; i<d; i++) cin >> v[i];

    int ans = 4242;

    for(int i=1; i<=1000; i++) // max plate after specials
    {
        int specials = 0;
        for(int j=0; j<d; j++) specials += (v[j]-1)/i;
        ans = min(ans, specials+i);
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

