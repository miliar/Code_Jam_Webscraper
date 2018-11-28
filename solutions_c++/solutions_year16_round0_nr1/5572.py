#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

vector<int> cif;

void pridej(int cis){
	REP(a,cif.size()){
		if(cis == cif[a]) return;
	}
	cif.pb(cis);
}

void over(ll cis){
	while(cis > 0){
		pridej(cis%10);
		cis/=10;
	}
}

void solve(int test){
	ll cis;
	cif.clear();
	scanf("%lli",&cis);
	if(cis == 0){
		printf("Case #%i: INSOMNIA\n",test);
		return;
	}
	ll akt = cis;
	over(akt);
	while(cif.size()<10){
		akt+=cis;
		over(akt);
	}
	printf("Case #%i: %lli\n",test,akt);
}



int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	return 0;
}
