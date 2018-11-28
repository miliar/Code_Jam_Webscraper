#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,rem) memset(in,rem,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
string dp[1005];
int main()
{
    int i;
     freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    int index=1;
    while(t--){
        string s;
        cin >> s;
        dp[1]=s[0];
        for(int i=1;i<s.size();++i){
            string f=dp[i];
            string g=f;
            g=s[i]+dp[i];
            f=dp[i]+s[i];
            dp[i+1]=max(f,g);
        }
        cout << "Case #" << index++ << ": " << dp[(int)s.size()] << endl;

    }
    return 0;
}