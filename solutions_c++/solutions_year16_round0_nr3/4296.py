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
void input(vector<X>&a,ll N){
    X temp;
    rep(i,0,N){
        cin>>temp;
        a.push_back(temp);
    }
}
ll alpha(string num, ll base){
    reverse(all(num));
    ll result=0;
    ll cur=1;
    for(char i:num){
        if(i=='1'){
            result+=cur;
        }
        cur*=base;
    }
    return result;
}
ll isPrime(ll N) {
	if(N<2)return N;
	if(N<4)return -1;
	if((N&1)==0)return 2;
	if(N%3==0)return 3;
	ll curr=5;
	while (curr<=sqrt(N)){
		if(N%curr==0)return curr;
		curr+=2;
		if(N%curr==0)return curr;
		curr+=4;
	}
	return -1;
}
string bin(ll N){
    string ans="";
    while(N){
        ans.pb('0'+N%2);
        N/=2;
    }
    reverse(all(ans));
    return ans;
}
void solve(ll t){
    ll N;
    ll J;
    cin>>N>>J;
    cout<<"Case #"<<t<<":"<<endl;
    for(ll i=(1+(1LL<<(N-1)));i<(1LL<<N);i+=2){
        if(J==0)break;
        string p=bin(i);
        ll a[9];
        memset(a,-1,sizeof a);
        rep(j,2,11){
            ll beta=alpha(p,j);
            ll k=isPrime(beta);
            if(k!=-1)a[j-2]=k;
        }
        if(find(a,a+9,-1)==a+9){
            cout<<p<<" ";
            rep(i,0,9){
                cout<<a[i]<<" ";
            }
            cout<<endl;
            J-=1;
        }
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t;
    cin>>t;
	rep(i,0,t){
		solve(i+1);
	}
	return 0;
}
