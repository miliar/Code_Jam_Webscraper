#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#define	MAXN	1000001
using namespace std;
typedef long long ll;

vector<ll> fair;

bool isPal(ll a){
	vector<int> num;
	ll n=a, cf=0;
	while(n!=0LL){
		num.push_back(n%10LL);
		n/=10LL;
		cf++;
	}
	for(int i=0;i<cf/2;++i){
		if(num[i]!=num[cf-1-i]) return 0;
	}
	return 1;
}

void precalc(){
/*	for(int i=1;i<=9;++i){
		fair.push_back(i);
		fair.push_back( (ll)(( i*10+i)*(i*10+i) ) );
	}
	for(int i=1;i<=9;++i){
		for(int j=0;j<=9;++j){
			ll temp=i*100+j*10+i;
			fair.push_back(temp*temp);
		}
	}
*/	
	for(ll i=1LL;i<10000001LL;++i){
		if(isPal(i) and isPal(i*i))		fair.push_back(i*i);
	}
}

int main(){
	int t,k=0;
	cin>>t;
	precalc();
	sort(fair.begin(),fair.end());
/*
	for(int i=0;i<fair.size();++i){
		cout<<fair[i]<<" ";	
	}	
	cout<<endl;
*/	
	while(t--){
		long long a,b;
		scanf("%lld %lld\n",&a,&b);
//		cout<<a<<" "<<b<<endl;
		
		printf("Case #%d: ",++k);
		int cc=0;
		for(int i=0;i<fair.size();++i){
			if(fair[i]>=a and fair[i]<=b) cc++;
		}
		printf("%d\n",cc);
	}	
	return 0;
}
