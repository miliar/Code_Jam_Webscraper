//satyaki3794
#include <bits/stdc++.h>
#include <iomanip>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}


int n, k;
#define OFFSET 202
double DP[205][406];
vector<double> arr(205);

double dp(int rem, int balance){

    if(rem < abs(balance-OFFSET))   return 0;
    if(rem == 0){
        return (balance == OFFSET);
    }
    double &ans = DP[rem][balance];
    if(ans == ans)  return ans;

    ans = 0;
    //take this as YES
    ans += arr[rem-1] * dp(rem-1, balance-1);
    //take this as NO
    ans += (1-arr[rem-1]) * dp(rem-1, balance+1);
    return ans;
}


int main()
{
    ios_base::sync_with_stdio(0);

    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, x = 1;
    cin>>t;
// t=1;
    while(t--){

        cout<<"Case #"<<x++<<": ";
        vector<double> v;
        cin>>n>>k;
        for(int i=0;i<n;i++){
            double p;
            cin>>p;
            v.pb(p);
        }
        sort(v.begin(), v.end());

// for(auto i : v) cout<<i<<" ";cout<<endl;

        // for(int i=0;i<k/2;i++)
        //     arr[i] = v[i];
        // int next = k/2;
        // for(int i=n-k/2;i<n;i++,next++)
        //     arr[next] = v[i];

        double ans = 0;
        for(int first=0;first<=k;first++){
            int next = 0;
            for(int i=0;i<first;i++,next++)
                arr[next] = v[i];
            int rem = k - first;
            for(int i=n-rem;i<n;i++,next++)
                arr[next] = v[i];
            memset(DP, -1, sizeof(DP));
            ans = max(ans, dp(k, OFFSET+0));
    // cout<<"first = "<<first<<": ";for(int i=0;i<k;i++) cout<<arr[i]<<" ";cout<<" gives "<<dp(k, OFFSET+0)<<endl;
        }

        cout<<fixed<<setprecision(7)<<ans<<endl;
    }

    return 0;
}








