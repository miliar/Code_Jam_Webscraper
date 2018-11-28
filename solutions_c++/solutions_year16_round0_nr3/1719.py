#include <bits/stdc++.h>
using namespace std;

typedef __int128 lll;

#define n 32

int t,tc=1,j;

lll u = 1000000;
bitset<1000001> bs;
vector<lll> primes;

void sieve() {
	u++;
	bs.set();
	bs[0] = bs[1] = 0;
	for (lll i = 2; i < u; i++) {
		if (bs[i]) {
			for (lll j = i * i; j < u; j += i) {
				bs[j] = 0;
			}
			primes.push_back(i);
		}
	}
}

lll f(lll mask, lll base){
	lll ans=0;
	lll k=1;
	for(int i=0;i<n;i++){
		if(mask&1){
			ans+=k;
		}
		k*=base;
		mask>>=1;
	}
	return ans;
}

int main(){
	sieve();
	cin>>t;
	int asdf;
	for(;tc<=t;tc++){
		cin>>asdf>>j;
		lll x=(1ll<<(n-1))+3ll;
		
		vector<int> ans(j,0);
		vector<vector<int> > ansd(j,vector<int>(9,0));
		
		int ci=0;
		while(1){//cout<<(int)f(x,2)<<"="<<bitset<32>(x)<<endl;
			if(ci==j)break;
			for(int i=0;i<=8;i++){
				lll a=f(x,i+2ll);
				lll cp;
				for(lll p:primes){
					if(a%p==0&&a!=p){cp=p;goto composite;}
				}
				goto prime;
				composite:;
				ansd[ci][i]=cp;
			}
			
			ans[ci]=x;
			ci++;
			
			prime:;
			x+=2;
		}
		cout<<"Case #"<<tc<<":\n";
		for(int i=0;i<j;i++){
			cout<<bitset<n>(ans[i]);
			for(int k=0;k<=8;k++){
				cout<<' '<<ansd[i][k];
			}
			cout<<endl;
		}
		
	}
}
