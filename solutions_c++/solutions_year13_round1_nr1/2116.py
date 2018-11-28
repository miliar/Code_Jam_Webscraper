#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<list>
#include<cmath>

#define PI 3.14159265359
#define EPS -0.00000000001

using namespace std;


int r,t,ans;


void calcAns(){


	int i,cR,tR;
	int cP,cT;

	double lT;

	lT=PI;

	ans=0;

	cR=r;
	cP=t;

	
	tR=cR+1;
	while(true){
		
		cT=(((tR*tR))-((cR*cR)));

		//cT=cT/lT;

	//	printf("pi  %lf  lt  %lf     tR   %d    cR   %d    cP   %d    cT  %d\n",PI,lT,tR,cR,cP,cT);

		if(cP-cT>=0){
			cP=cP-cT;
			tR=tR+2;
			cR=tR-1;
			ans++;
		}else{
			break;
		}

	}



}

int main(){


	//freopen("in.txt","r",stdin);
	freopen("q.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,cases;

	scanf("%d",&cases);

	for(i=1;i<=cases;i++){
		scanf("%d%d",&r,&t);
		calcAns();
		printf("Case #%d: %d\n",i,ans);
	}


	return 0;
}