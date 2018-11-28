#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS
typedef __int64 LL;
#ifdef TC_OFFLINE
	#define PAUSE system("pause");
#else
	#define PAUSE
#endif

class RedIsGood{

public:
	
	static double getProfit(int R, int B){

		return 0;
	};
};

void make_pd(int k,LL* io){
	int sk=k;
	int tl=0;
	int inv=0;
	int bs=1;
	while(k){
		tl++;
		int d=k%10;
		k/=10;
		inv=inv*10+d;
		bs*=10;
	};
	io[0]=(LL)sk*(LL)bs+inv;
	io[1]=((LL)sk/10L)*(LL)bs+inv;
}
		

bool judge_pd(LL n){
	char tmp[100];
	char* itmp=tmp;
	while(n){
		*itmp++='0'+n%10;
		n/=10;
	}
	int cnt=itmp-tmp;
	for(int i=0;i<cnt/2;i++)
		if(tmp[i]!=tmp[cnt-1-i])
			return false;
	return true;
}

const int RG=10000;

LL lut[RG*2];

int precalc(){
	LL* plut=lut;
	for(int t=1;t<RG;t++){
		LL tmp[2];
		make_pd(t,tmp);
		for(int xx=0;xx<2;xx++){
		if(!judge_pd(tmp[xx]))
			continue;
		LL sq=(LL)tmp[xx]*(LL)tmp[xx];
		if(!judge_pd(sq))
			continue;
		*plut++=sq;
		}
	}
	sort(lut,plut);
	return plut-lut;
}


int main(){
	int T;
	int ttl=precalc();
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		LL A,B;
		cin>>A>>B;
		int l=lower_bound(lut,lut+ttl,A)-lut;
		int r=upper_bound(lut,lut+ttl,B)-lut;
		cout<<"Case #"<<tt<<": "<<r-l<<endl;
	};
	PAUSE;
	return 0;
};

