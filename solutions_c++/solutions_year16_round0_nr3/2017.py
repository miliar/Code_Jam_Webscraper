#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define pb push_back
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%I64d",&x)
#define F first
#define S second
#define maxn 100005

int p[maxn],mod;
vector<int>v;
void sieve(){
	p[0]=p[1]=1;
	for(int i=2;i*i<maxn;i++){
		if(!p[i]){
			for(int j=i*i;j<maxn;j+=i){
				p[j]=1;
			}
		}
	}
	for(int i=2;i<maxn;i++)if(!p[i])v.pb(i);
}


ll power(ll n,ll p){
	if(p==0)return 1;
	if(p==1)return n%mod;
	ll y=power(n,p/2);
	y*=y;
	y%=mod;
	if(p%2){
		y*=n;
		y%=mod;
	}
	return y; 
}
map<string,int>mem;
int main(){
	cout<<"Case #1:\n";
	sieve();
	srand(time(NULL));
	int t,n,j;
	cin>>t>>n>>j;
	rep(tc,j){
		string s="1";
		rep(i,n-2){
			int x=rand()%2;
			if(x==0)s=s+"0";
			else s=s+"1";
		}
		s+='1';
		if(mem[s]){
			tc--;
			continue;
		}
		mem[s]=1;
		vector<int>vec;
		for(ll i=2;i<=10;i++){
			for(int j=0;j<120;j++){
				ll num=0;
				mod=v[j];
				for(ll k=0;k<n;k++){
					if(s[k]=='1'){
						num+=power(i,k);
						num%=mod;
					}
				}
				if(num==0){
					vec.pb(v[j]);
					break;
				}
			}
		}
		if(vec.size()==9){
			reverse(s.begin(), s.end());
			cout<<s<<" ";
			for(auto i:vec)cout<<i<<" ";cout<<endl;
		}
		else tc--;
	}

	return 0;
}