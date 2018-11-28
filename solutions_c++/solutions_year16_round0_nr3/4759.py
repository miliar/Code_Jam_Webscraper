#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int isprime[1001000],prime[1001000],cnt=0;
void getprime(){
	memset(isprime,-1,sizeof(isprime));
	isprime[1]=isprime[0]=0;
	for(int i=2;i<=1000000;i++){
		if(isprime[i])prime[cnt++]=i;
		for(int j=0;j<cnt&&i*prime[j]<=1000000;j++){
			isprime[i*prime[j]]=0;
			if(i%prime[j]==0)break;
		}
	}
}
ll a[10001];
bool is_prime(ll x){
	if(x<=1000000){
		if(isprime[x])return true;
		return false;
	}
	for(int i=0;i<cnt&&prime[i]*prime[i]<=x;i++)
		if(x%prime[i]==0)return false;
	return true;
}
string str[1000];
ll b[1000][20];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
	getprime();
	ll T;
	cin>>T;
	for(int t=1;t<=T;t++){
		vector<string> hh;
		ll N,J;
		cin>>N>>J;
		printf("Case #%d:\n",t);
		ll L=(1LL<<(N-1))+1;
		ll R=1LL<<N;
		ll tot=0;
		for(ll i=L;i<=R;i++){
			if(!(i&1))continue;
			string gg="";
			for(int j=0;j<N;j++)
				gg+=((i>>j)&1)+'0';
			std::reverse(gg.begin(),gg.end());
			for(ll j=2;j<=10;j++){
				ll xx=0;
				for(auto ch:gg)
					xx=j*xx+(ch-'0');
				a[j]=xx;
			}
			bool flag=true;
			for(int j=2;j<=10;j++)
				if(is_prime(a[j])){
					flag=false;
					break;
				}
			if(flag){
				tot++;
				str[tot]=gg;
				for(int j=2;j<=10;j++)
					b[tot][j]=a[j];
				if(tot==J)break;
			}
		}
		for(int i=1;i<=tot;i++){
			cout<<str[i];
			for(int j=2;j<=10;j++){
				ll pp;
				for(int k=0;k<cnt&&prime[k]*prime[k]<=b[i][j];k++)
					if(b[i][j]%prime[k]==0){
						pp=prime[k];
						break;
					}
				printf(" %lld",pp);
			}
			puts("");
		}
	}
	return 0;
}
