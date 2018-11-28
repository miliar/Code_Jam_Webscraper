/* Author: vishparekh */

#include<bits/stdc++.h>
using namespace std;

#define FOR(i,start,stop,step) for(ll i=start; i<stop; i+=step)
#define fore(it,v) for(it=v.begin(); it!=v.end(); it++)
#define SZ(V) (int)V.size()
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define fi first
#define se second
#define Pi 3.14159265358979

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> V;
typedef pair<int, int> PII;

const int INF_MAX = 2147483647;
const int INF_MIN = -2147483647;
const int MOD =  1000000007;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    FOR(i,1,t+1,1)
    {
        string s;
        ll ans = 0;
        cin>>s;
        if(s.length() == 1)
        {
            if(s[0] == '-')
                cout<<"Case #"<<i<<": "<<"1"<<endl;
            else
                cout<<"Case #"<<i<<": "<<"0"<<endl;

        }
        else
        {
            if(s[0] == '-')
                ans++;
            for(int j = 0 ; j < s.length(); j++)
            {
                if(s[j]=='+')
                {

                    if(s[j+1]=='-')
                        ans+= 2;

                }

            }
            cout<<"Case #"<<i<<": "<<ans<<endl;

            }
        }
    return 0;
}

