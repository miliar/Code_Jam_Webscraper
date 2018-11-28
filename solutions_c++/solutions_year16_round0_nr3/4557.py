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

ll cis[16];

ll zak(ll kol){
	ll ccis = 0;
	REP(a,16){
		ccis*=kol;
		ccis+=cis[a];
	}
	return ccis;
}

ll prv(ll c){
	for(ll a = 2; a<sqrt(c)+20; a++){
		if(c%a == 0){
			return a;
		}
	}
	return c;
}

void pric(){
	ll i = 14;
	while(cis[i] == 1){
		cis[i] = 0;
		i--;
	}
	cis[i] = 1;
}

int main(){
	cout<<"Case #1:\n";
	REP(a,16) cis[a] = 0;
	cis[0] = 1;
	cis[15] = 1;
	ll kol = 0;
	vector<ll> del;
	while(kol < 50){
		bool nasel = false;
		while(!nasel){
			del.clear();
			for(ll a = 2; a<= 10; a++){
				ll akt = zak(a);
				del.pb(prv(akt));
				if(del.back() == akt) del.pop_back();
			}
			if(del.size() == 9){
				nasel = true;
				REP(a,16) printf("%lli",cis[a]);
				printf(" ");
				REP(a,del.size()){
					if( a < del.size()-1) cout<<del[a]<<" ";
					else cout<<del[a];
				}
				cout<<endl;
			}
			pric();
			
		}
		kol++;
	}
		

	
	return 0;
}
