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

int main(){
	int t,g=1;
	cin>>t;
	while(t--){
		string s;
		int i,j,ans=0,n;
		cin>>s;
		n=s.length();
		int l=n;
		for(i=n-1;i>=0;i--){
			if(s[i] != '+') break;
			l = i;
		}
		if(l==0){
			cout<<"Case #"<<g<<": "<<0<<endl;
			g++;
			continue;
		}
		string tmp = "";
		for(i=0;i<l;i++){
			tmp = tmp + s[i];
		}
		int flip = 0;
		char last = s[0];
		for(i=1;i<l;i++){
			if(s[i] == last){
				continue;
			}
			else{
				flip ++;
				last=s[i];
			}
		}	
		cout<<"Case #"<<g<<": "<<flip+1<<endl;
		g++;
	}
	return  0;
}