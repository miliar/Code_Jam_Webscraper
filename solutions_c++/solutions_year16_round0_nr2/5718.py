#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

#define pb push_back
#define mp make_pair
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define file freopen("1.txt","r",stdin)
#define llel y1
#define x MAXN


int n,m,k,l,r,ans,q;
string s;

main()
{
    freopen("B-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    cin >> q;

    for(int jj = 1; jj <= q; ++jj){
        cin >> s;

        if (s[s.size() - 1] == '+') ans = 0;
        else ans = 1;

        for(int i = 1; i < s.size(); ++i){
            if (s[i] != s[i - 1]) ans++;
        }

        cout << "Case #" << jj << ": " << ans << "\n";
    }
}
