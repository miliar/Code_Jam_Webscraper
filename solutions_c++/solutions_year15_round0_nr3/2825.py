/* https://code.google.com/codejam/contest/6224486/dashboard */

#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
#define rep(i,a,n) for(__typeof(n) i = a; i < n; ++i)
#define repe(i,a,n) for(__typeof(n) i = a; i <= n; ++i)
#define mfill(a,b) memset(a, b, sizeof(a))
#define all(a) a.begin(), a.end()
#define pb(a) push_back(a)
#define dbg(x) {cout<<__LINE__ <<"::" << #x << ": " << (x) << endl; }


int main()
{
    ios_base::sync_with_stdio(false);
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
    int t;
    cin>> t;
    repe(_case,1,t)
    {

        int q;
        cin >> q;
        string s;
        cin >> s;
        int count = (s[0] - '0');
        int req = 0;
        //dbg(count);
        int len = q + 1;
        rep(i, 1, len)
        {
            if(count < i)
                {
                    req += i - count;
                    count = i;

                }
            count += (s[i] - '0');
        }
        cout << "Case #" << _case <<": ";
        cout << req << "\n";
    }
    return 0;
}
