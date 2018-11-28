#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bitset<1000001> V;
vector<int> P;
void S(){
	ll N=1000000;
	V.set(); V.reset(0); V.reset(1); V.reset(2);
	P.push_back(2);
	for(ll i=3; i<=N; i+=2){
		if(V[i]){
			P.push_back(i);
			for(ll j=i*i; j<=N; j+=i){
				V[j]=0;
			}
		}
	}
}

ll F(ll M, ll B){
	ll m=0;
	ll b=B;
	for(int i=0; i<100; i++){
		m=0; b=1;
		ll Mod=P[i];
		for(ll i=0; i<32; i++, b=(b*B)%Mod){
			if(M&(1LL<<i)){
				m+=b;
				if(m>Mod) m-=Mod;
			}
		}
		m%=Mod;
		if(m==0) return Mod;
	}	
	return -1;
}
int main(){
	S();
	ll N, J;
	int Test;
	scanf("%d", &Test);
	scanf("%lld %lld", &N, &J);
	ll M=1;
	M|=(1LL<<(N-1LL));
	ll i;
	ll Cnt=0;
	printf("Case #1:\n");
	for(i=M; i<(1LL<<N), Cnt<J; i++){
		if(!(i&1)) continue;
		vector<ll> D;
		for(ll j=2; j<=10; j++){
			ll d=F(i, j);
			if(d!=-1) D.push_back(d);
		}
		if(D.size()==9){
			for(ll j=N-1LL; j>=0LL; j--) printf("%d", ( (i&(1LL<<j))?1:0) );
			printf(" ");
			for(int j=0; j<9; j++){
				if(j) printf(" ");
				printf("%lld", D[j]);
			}printf("\n");
			Cnt++;
		}
	}
	return 0;
}

