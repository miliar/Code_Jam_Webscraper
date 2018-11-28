#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll prime_check(ll n) {
	ll div=-1;
	while(n && n%2==0) {
		n=n/2;
		div=2;
	}
	for(ll i=3;i*i<=n;i+=2) {
		while(n && n%i==0) {
			n=n/i;
			div=i;
		}
	}
	return div;
}
	
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int n=16;
	int t,g;
	scanf("%d %d %d",&t,&n,&g);
	ll a[11];
	ll val=0;
	string res="";
	int cnt=0;
	bool flag=false;
	cout << "Case #1:" << endl;
	for(int i=0;i<(2<<n) && cnt<50;i++) {
		if((i&(1<<0))==0 || (i&(1<<15))==0)
			continue;
		for(int j=2;j<=10;j++) 
			a[j]=pow(j,0)+ pow(j,15);
		res="";
		res+="1";
		vector<ll> v;
		for(int j=1;j<=14;j++) {
			if((i&(1<<j))!=0) {
				res+="1";
				for(int l=2;l<=10;l++)
					a[l]+=pow(l,15-j);
			}
			else {
				res+="0";
			}
		}
		flag=false;
		for(int l=2;l<=10;l++) {
			ll p = a[l];
			ll div = prime_check(p);
			if(div==-1) {
				flag=true;
				break;
			}
			v.push_back(div);
		
		}
		if(!flag) {
			res+="1";
			cout << res << " ";
			for(int l=0;l<v.size();l++) {
				printf("%lld ",v[l]);
			}
			printf("\n");
			cnt++;
		}
	}
	return 0;
	//fclose(stdout);
}
	
				
