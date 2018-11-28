#include <bits/stdc++.h>
#define REP(i,a,b) for(i=a;i<=b;i++)
using namespace std;
typedef long long ll;
bool h[10];
ll cnt;
void chck(ll x){
	while(x){
		if(!h[x%10]){
			h[x%10]=1;
			cnt++;
		}
		x/=10;
	}
}
int main(){
	freopen("in.txt","r",stdin);
	ios::sync_with_stdio(false);
	int t,c=0;
	cin>>t;
	chck(123);
	while(t--){
		c++;
		cnt=0;
		memset(h,0,sizeof(h));
		ll i,n;
		cin>>n;
		cout<<"Case #"<<c<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		REP(i,1,1000010){
			chck(n*i);
			//cout<<i<<" "<<cnt<<endl;
			if(cnt==10){
				cout<<n*i;
				break;
			}
		}
		if(cnt!=10)
			cout<<"INSOMNIA";
		cout<<endl;
	}
}