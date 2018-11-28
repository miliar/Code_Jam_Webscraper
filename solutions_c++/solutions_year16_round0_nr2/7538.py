/* https://code.google.com/codejam/contest/6254486/dashboard#s=p1 */

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
  freopen("B-large.in","r",stdin);
  freopen("1_large_revenge_of_pancakes.out","w",stdout);
    int t;
    cin>> t;
    repe(_case_, 1, t)
    {
        string s;
        cin >> s;
        int answer;
        answer = (s[0] == '-' ? 1: 0);
        rep(i, 1, s.size()){
            if(s[i] == '-' and s[i-1] == '+')
                answer += 2;
        }

        cout << "Case #" <<  _case_ << ": " << answer <<"\n";

    }
    return 0;
}
