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
        char ans[1007];
        cin>>s;
        ans[0] = s[0];
        for(int j = 1 ; j < s.length() ; j++)
        {
            if(s[j]>=ans[0])
            {
                for(int i = j ; i >0 ;i-- )
                {
                        ans[i] = ans[i-1];
                }
                ans[0] = s[j];
                //cout<<ans[0];
            }
            else
            {
                ans[j] = s[j];
                //cout<<ans[j];

            }
        }
        cout<<"Case #"<<i<<": ";
        for(int k = 0 ; k < s.length();k++)
            cout<<ans[k];
        //string str(ans);
        cout<<endl;
    }
    return 0;
}
