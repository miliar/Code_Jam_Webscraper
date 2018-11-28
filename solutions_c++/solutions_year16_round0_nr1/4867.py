#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define si(x) scanf("%d",&x)
#define sc(ch) scanf(" %c",&ch);
#define sl(x) scanf("%I64d",&x)
#define pi(x) cout << x <<" "
#define nl cout << '\n'
#define mp make_pair
#define pb push_back
#define f first
#define se second
#define pii pair<int,int>
#define RESET(a) memset(a,-1,sizeof(a))
#define CLEAR(a) memset(a,0,sizeof(a))
#define all(v)   v.begin(),v.end()
#define trv(it,v) for(it=v.begin();it!=v.end();it++)
#define rep(i,a,b) for(int i=a;i<b;i++)
#define mod 1000000007
#define MIN INT_MIN
#define MAX INT_MAX
#define INF 10e8
//freopen("out", "w", stdout);

int check(int n)
{
    if(n==0)
        return -1;
    set<int> S;
    int k=1;
    while(k<1e5){
        ll x = (ll)k*n;
        while(x){
            S.insert(x%10);
            x /= 10;
        }
        if(S.size()==10)
            return k*n;
        k++;
    }
    return -1;
}

int main()
{
    std::ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("2.txt", "r", stdin);
       freopen("out2.txt", "w", stdout);
    #endif

    int t;
    cin >> t;
    int j=1;
    while(j<=t){
        int n;
        cin >> n;
        int ans = check(n);
        if(ans!=-1){
            cout << "Case #"<<j<<": "<<ans;
        }
        else{
            cout <<"Case #"<<j<<": INSOMNIA";
        }
        j++;
        nl;
    }


   return 0;
}
