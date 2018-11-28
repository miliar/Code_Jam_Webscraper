#include <bits/stdc++.h>
#define PI                3.14159265358979323846264338327950
#define pb                push_back
#define mp                make_pair
#define all(a)            (a).begin(), (a).end()
#define clr(a,h)          memset(a, (h), sizeof(a))
#define rep(i, n)         for(int i = 0; i < int(n); ++i)
#define revRep(i, n)      for(int i = int(n); i >=0; --i)
#define repE(i, a, b)     for(int i = int(a); i < int(b); ++i)
#define foreach(it, a)    for(typeof((a).begin()) it=(a).begin(); it != (a).end(); ++it)
#define revForeach(it, a) for(typeof((a).rbegin()) it=(a).rbegin(); it != (a).rend(); ++it)
#define F first
#define S second

using namespace std;

const int INF = int(1e9+7);
typedef pair<int,int>   ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       ll;
typedef vector<ll>      vll;

int main()
{
    std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    rep(T, t)
    {
        string s;
        cin>>s;
        deque<char> dq;
        dq.push_back(s[0]);
        repE(i, 1, s.length())
        {
            if (s[i] >= dq.back()) dq.push_back(s[i]);
            else dq.push_front(s[i]);
        }
        cout<<"Case #"<<T+1<<": ";
        while (!dq.empty())
        {
            cout<<dq.back();
            dq.pop_back();
        }
        cout<<endl;
    }
    return 0;
}
