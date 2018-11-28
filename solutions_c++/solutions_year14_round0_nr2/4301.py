#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

#define SET(v,i) memset(v,i,sizeof(v));
#define FOR(i,n,k) for(int i=n;i<k;++i)
#define WHILE(i,n) while(i<n)
#define RI(i) scanf("%d",&i);
#define RS(i) scanf("%s",i);
#define RF(i) scanf("%lf",&i);
#define RL(i) scanf("%lld",&i);
#define OPEN(s) freopen(s,"r",stdin);
#define CLOSE(s) freopen(s,"w",stdout);

const int INF=0x3F3F3F3F;
const int MAXN=100001;
typedef long long int i64;
typedef pair<int,int> pii;
typedef pair<string,int> psi;

double C,F,X;

double nextStep(double CPS){
	return X / (CPS+F);
}
double curStep(double CPS){
	return (X-C) / CPS;
}

int main(){
	#ifdef DM1_MACHINE
		OPEN("FILEB.in");
		CLOSE("FILEb.out");
	#endif
	int t; RI(t);
	FOR(ic,1,t+1){
		RF(C); RF(F); RF(X);
		double CPS = 2.0f;
		double TIME = 0.0f;
		while(nextStep(CPS) < curStep(CPS)){
			TIME+=(C/CPS);
			CPS+=F;
			//fprintf(stderr,"%.2lf\n",TIME);
		}
		TIME += X/CPS;
		printf("Case #%d: %.7lf\n",ic,TIME);
	}
	return 0;
}


////////////////////////////////////////////
/////////////Code by David Moran////////////
/////////////////////////////P=NP///////////
