#include <bits/stdc++.h>
#define fr freopen("input.in","r",stdin)
#define fw freopen("output.out","w",stdout)
#define iOs ios_base::sync_with_stdio(false);
#define INF 111313131
#define all(x) (x).begin(), (x).end()
#define debug cout<<"here\n"
#define debugin cout<<"inhere\n"
#define debugname cout<<"dharmang\n";
using namespace std;
#define pb push_back
#define mp make_pair
#define sc second
#define fir first
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
int main()
{
    #ifndef ONLINE_JUDGE
        fr;fw;
    #endif
    iOs;
    int t; cin>>t;
    for(int i=1;i<=t;i++)
    {
        int ans=0; string s; cin>>s; char c=s[0];
        for(int j=1;j<s.size();j++)
        {
            if(s[j]!=c) {ans++; c=s[j];}
        }
        if(s[s.size()-1]=='-') ans++;
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

