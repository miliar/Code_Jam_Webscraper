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

int b;
ll m;
int graf[100][100];

ll moc(ll vys, int b){
	if(b == 0) return 1;
	if(b == 1) return vys;
	if(b%2 == 0) return moc(vys*vys, b/2);
	else return moc(vys*vys,b/2)*vys;
}

bool over(){
	return m <= moc(2,b-2);
}

void solve(int test){
	cerr<<test<<endl;
	cin>>b>>m;
	printf("Case #%i: ",test);
	if(!over()){
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("POSSIBLE\n");
	REP(a,b){
		REP(c,b) graf[a][c] = 0;
	}
	REP(a,b-1){
		graf[a][a+1] = 1;
	}
	ll vys = 1;
	int kde = b-2;
	while(vys < m){
		vys*=2;
		kde--;
		for(int a = kde+1; a < b; a++){
			graf[kde][a] = 1;
		}
	}
	ll roz = vys-m;
	for(int a = b-2; a > kde; a--){
		if(roz % 2 == 1){
			graf[kde][a] = 0;
		}
		roz/=2;
	}

	REP(a,b){
		REP(c,b) cout<<graf[a][c];
		printf("\n");
	}
	
}

int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	return 0;
}
