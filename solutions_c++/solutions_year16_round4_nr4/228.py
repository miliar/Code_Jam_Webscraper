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


int n;
char arr[20][20];

bool valid(int mask){
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(arr[i][j] == '1' && (mask & (1<<(n*i+j))) == 0)
                return false;
    return true;
}

int cost(int mask){
    int ans = 0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(arr[i][j] == '0')
                if((mask>>(n*i+j)) & 1)
                    ans++;
    return ans;
}

bool possible(int mask, int ppl, int machines){
    if(ppl == ((1<<n)-1)){
// cout<<"yolo ";
// cout<<mask<<" "<<ppl<<" "<<machines<<" returns true\n";
        return true;
    }
    for(int next=0;next<n;next++){
        if((ppl>>next) & 1) continue;
        bool atleast_one_free = false;
        for(int m=0;m<n;m++){
            if((machines>>m) & 1)   continue;
            if((mask >> (n*next+m)) & 1){
                atleast_one_free = true;
                if(!possible(mask, ppl|(1<<next), machines|(1<<m))){
// cout<<mask<<" "<<ppl<<" "<<machines<<" returns false\n";
                    return false;
                }
            }
        }
        if(!atleast_one_free)   return false;
    }
// cout<<mask<<" "<<ppl<<" "<<machines<<" returns true\n";
    return true;
}



int main()
{
    ios_base::sync_with_stdio(0);

    freopen("D-small-attempt0 (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, x = 1;
    cin>>t;
// t=1;
    while(t--){

        cout<<"Case #"<<x++<<": ";
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>arr[i];

// cout<<possible(6, 0, 0)<<endl;
// cout<<valid(6)<<endl;

        int ans = n*n+5;
        for(int mask=0;mask<(1<<(n*n));mask++)
            if(possible(mask, 0, 0) && valid(mask)){
        // cout<<mask<<" gives cost = "<<cost(mask)<<endl;
                ans = min(ans, cost(mask));
            }
        cout<<ans<<endl;
    }

    return 0;
}








