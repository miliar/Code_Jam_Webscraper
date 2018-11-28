#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;
int ktmaji[500];
bool jde[500];


void novaVypln(int hodnota, int maxi, int kolik){
	for(int a = maxi; a>=0; a--){
		if(jde[a] == true || a==0){
	//		printf("%i\n",hodnota);
			REP(b,kolik) jde[a+hodnota*(b+1)] = true;
		}
	}
}

int solve(){
	int kolik, maji, maxi;
	scanf("%i%i%i",&kolik,&maji,&maxi);
	REP(a,maxi+100) jde[a] = false;
	REP(a,maji) scanf("%i",&ktmaji[a]);
	for(int a = maji-1; a>=0; a--) novaVypln(ktmaji[a],maxi,kolik);
	int vysl = 0;
	for(int a = 1; a<= maxi;a++){
		if(jde[a] == false){
			vysl++;
			novaVypln(a,maxi,kolik);
		}
	}
	return vysl;
}


int main(){
	int t;
	scanf("%i",&t);
	REP(a,t){
		printf("Case #%i: %i\n",a+1,solve());
	}
	return 0;
}
