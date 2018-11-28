#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define LL long long
#define sd(x) scanf("%d", &x)
#define sld(x) scanf("%lld", &x)
#define MOD 1000000007
#define SQ 112345
#define N 1123456
#define SZ(X) ((LL)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, A, B) for (LL I = A; I <= B; ++I)
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define PII pair<LL,LL>

long double MO(long double x){
    if(x < 0.0){
        x *= -1.0;
    }
    return x;
}

long double EPS = 1e-10;

int solve(){
    int n;
    long double v, x, ans = 0, y, c1, c0, r0, r1, v0, v1;
    cout<<setprecision(10)<<fixed;
    cin>>n;
    cin>>v>>x;
    cin>>r0>>c0;
    if(n == 1){
        if(MO(c0 - x) <= EPS){
            cout<<v / r0<<endl;
        }
        else{
            cout<<"IMPOSSIBLE"<<endl;
        }
        return 0;
    }
    else{
        ans = MOD;
        cin>>r1>>c1;
        if(MO(c1 - c0) <= EPS){
            if(MO(c0 - x) <= EPS){
                //cout<<(v / (r0 +  r1))<<endl;
                //cout<<"YES";
                y = 0.0;
                while(y <= v){
                    ans = min(ans, max(y / r0, (v - y) / r1));
                    y += 0.0001;
                }
                cout<<ans<<endl;
            }
            else{
                cout<<"IMPOSSIBLE"<<endl;
            }
            return 0;
        }
        if(MO(c0 - x) <= EPS){
            cout<<v / r0<<endl;
            return 0;
        }
        if(MO(c1 - x) <= EPS){
            cout<<v / r1<<endl;
            return 0;
        }
        v1 = v * (x - c0) / (c1 - c0);
        v0 = (v - v1);
        //cout<<(x - c0)<<" "<<(c1 - c0)<<endl;

        if( ((x - c0) / (c1 - c0) > 1.0) || (((x - c0) / (c1 - c0)) < 0.0) ){
            //cout<<v0<<" "<<v1<<endl;
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<max(v0 / r0, v1 / r1)<<endl;
        }
    }
}

int main(){
    freopen("in.txt", "r", stdin);
    //cout<<EPS<<endl;
    freopen("out.txt", "w", stdout);
    LL t = 1;
    int o = 1;
    cin>>t;
    while(t--){
        printf("Case #%d: ", o++);
        solve();
    }
    return 0;
}
