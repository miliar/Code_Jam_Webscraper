#include<bits/stdc++.h>
#define ll long long

using namespace std;
ll solve(ll n, bool seen[]){
	int c = 0;
	if(n == 0) return -1;
	int i = 1;
	//cout<<"n "<<n<<endl;
	ll ans = 0;

	while(c < 10){

	//	cout<<"c "<<c<<endl;
		ll temp = n*i;
		ans = temp;
	//	cout<<"i "<<i<<endl;
		while(temp){
	//		cout<<"temp "<<temp<<endl;
			ll d = temp%10;
			temp/=10;
			
	//		cout<<"d "<<d<<endl;
			if(!seen[d]){
	//			cout<<"seen "<<d<<endl;
				seen[d] = true;
				c++;
			}
		}
		i++;

	}
	//out<<"ans "<<n*i<<endl;
	return ans;
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int t = 1; t<=T; t++){
		ll n;
		cin>>n;
		bool seen[10];
		memset(seen, false, sizeof(seen));
		printf("case #%d: ",t);
		ll ans = solve(n, seen);
		ans == -1? printf("INSOMNIA\n"): printf("%lld\n",ans);
	}
}
