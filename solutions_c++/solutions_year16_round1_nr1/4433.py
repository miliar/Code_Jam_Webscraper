#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>

//type definitions
#define rep(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define in(n) scanf("%d",&n)

///STL
#define vi vector<int>
#define vvi vector< vector<int> >
#define pb push_back
#define mp make_pair
#define mii map<int,int>
#define pii pair<int,int>
#define f first
#define s second

//Iterator!
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

/// Constants
#define ll long long
#define mod 1000000007
#define EPS 1e-7
#define sqr(x) ((x)*(x))
#define sqrt(x) sqrt(1.0*(x))
/// Files.
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;


int main()
{
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>t;
    rep(0,t-1)
    {
        string s;
        cin>>s;
        string q;
        q.pb(s[0]);
        vector<string> res;
        for(int j=1; j<s.length(); j++)
        {
            if(s[j]>=q[0])
            {
                string tmp;
                tmp.pb(s[j]);
                tmp.append(q);
                q = tmp;
            }
            else
            {
                q.pb(s[j]);
            }
        }
        cout<<"Case #"<<i+1<<": "<<q<<endl;
    }
    return 0;
}
