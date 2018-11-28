#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>

#define pb push_back
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

int recuFind(int c, int w){
	//printf("Je to %i a %i\n",c,w);
	return c/w;
}

int solve(){
	int r,c,w;
	scanf("%i%i%i",&r,&c,&w);
	int find = 	recuFind(c,w);
	int celk = find*r + w;
	if(c%w == 0) celk--;
	return celk;
}


int main(){
	int t;
	scanf("%i",&t);
	REP(a,t){
		printf("Case #%i: %i\n",a+1,solve());
	}
	return 0;
}
