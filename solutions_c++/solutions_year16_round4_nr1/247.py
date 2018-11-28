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


#define ROCK 0
#define SCISSORS 1
#define PAPER 2

int n, cnt[15][3][3];
string seq[15][3];

int loser(int x){
    return (x+1)%3;
}



int main()
{
    // ios_base::sync_with_stdio(0);

    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cnt[1][ROCK][ROCK] = 1;
    seq[1][ROCK] = "R";
    
    cnt[1][PAPER][PAPER] = 1;
    seq[1][PAPER] = "P";

    cnt[1][SCISSORS][SCISSORS] = 1;
    seq[1][SCISSORS] = "S";

    for(int lev=2;lev<=13;lev++)
        for(int winner=0;winner<3;winner++){
            int lose = loser(winner);
            for(int j=0;j<3;j++)
                cnt[lev][winner][j] = cnt[lev-1][winner][j] + cnt[lev-1][lose][j];
            if(seq[lev-1][winner] < seq[lev-1][lose])
                seq[lev][winner] = seq[lev-1][winner] + seq[lev-1][lose];
            else
                seq[lev][winner] = seq[lev-1][lose] + seq[lev-1][winner];
        }

    int t, x = 1;
    cin>>t;
// t=1;
    while(t--){

        cout<<"Case #"<<x++<<": ";
        
        int R, P, S;
        cin>>n>>R>>P>>S;

        vector<string> ans;
        for(int winner=0;winner<3;winner++){
            if(cnt[n+1][winner][ROCK] == R && cnt[n+1][winner][PAPER] == P && cnt[n+1][winner][SCISSORS] == S){
                ans.pb(seq[n+1][winner]);
            }
        }

        sort(ans.begin(), ans.end());
        if(ans.empty())
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans[0]<<endl;
    }

    return 0;
}








