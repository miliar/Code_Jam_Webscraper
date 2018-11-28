#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vvi vector<vi>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define rep(i,a,b) for(ll i=a;i<b;i++)
#define all(a) a.begin(),a.end()
#define sum(a) accumulate(all(a),0)
#define endl '\n'
#define hell 1000000007

using namespace std;
template <class X>
void input(vector<X>&a,int N){
    X temp;
    rep(i,0,N){
        cin>>temp;
        a.push_back(temp);
    }
}
void solve(int t){
    bool x[10]={false};
    ll N;
    cin>>N;
    if(N==0){
        cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        return;
    }
    ll ans=1;
    while(true){
        ll cur=ans*N;
        while(cur){
            int dig=cur%10;
            x[dig]=true;
            cur/=10;
        }
        if(find(x,x+10,false)==x+10)break;
        ans++;
    }
    cout<<"Case #"<<t<<": "<<ans*N<<endl;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	int t;
	cin>>t;
	rep(i,0,t){
		solve(i+1);
	}
	return 0;
}
