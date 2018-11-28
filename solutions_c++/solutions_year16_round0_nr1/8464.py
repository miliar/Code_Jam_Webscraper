#include <bits/stdc++.h>
using namespace std;
#define ll          long long int
#define mem(a,x)    memset(a,x,sizeof(a))
#define vi          vector<int>
#define vii         vector<vi>
#define pi          pair<int,int>
#define pii         pair<int,pi>
#define si(x)       scanf("%lld",&x)
#define sl(x)       scanf("%I64d",&x)
#define ss(s)       scanf("%s",s)
#define rep(i,a,b)  for(i=a;i<b;i++)
#define f(i,n)      rep(i,0,n)
#define tr(it,container) for(auto it=container.begin();it!=container.end();++it)
#define F           first
#define gc          getchar_unlocked
#define pb          push_back
#define mp          make_pair
#define all(a)      a.begin(),a.end()
#define sortall(a)  sort(all(a))
#define M         1000000007
#define mod(a,b) (a%b+b)%b;
#define N           100005
#define S 			400000
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
int a[10];
ll ans;
void check(ll n){
	int cnt = 1;
	int y = 10;
	while(cnt<10000 ){
		ll tmp = cnt*n;
		while(tmp){
			if(a[tmp%10] == 0){
				a[tmp%10] = 1;
				y--;
			}
			tmp /= 10;
		}
		if(y ==0 ){
			ans = cnt*n;
			break;
		}
		cnt ++;
	}
	return;
}

int main(){
	ll t,g=1;
	fstream f1("in.txt",std::fstream::in);
	fstream f2("out.txt",std::fstream::out);
	f1>>t;
	while(t--){
		
		ll n;
		f1>>n;
		bool ok=false;
		for(int i=0;i<10;i++) a[i]=0;
		if(n==0){
			f2<<"Case #"<<g<<": INSOMNIA"<<endl;
		}
		else{
			check(n);
			f2<<"Case #"<<g<<": "<<ans<<endl;
		}
		g++;
	}
	f1.close();
	f2.close();
	return  0;
}