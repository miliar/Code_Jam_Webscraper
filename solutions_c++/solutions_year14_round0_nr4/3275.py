// war_CPP.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<stdio.h>
#include<algorithm>
using namespace std;

int T,N;
double a[1050];
double b[1050];

int _tmain(int argc, _TCHAR* argv[])
{
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		scanf("%d",&N);
		for(int j=0;j<N;j++) scanf("%lf",&a[j]);
		for(int j=0;j<N;j++) scanf("%lf",&b[j]);
		sort(a,a+N);
		sort(b,b+N);
		int nc=0;
		int id=0,jd=0;
		while(jd!=N){
			if(b[id]<a[jd]){
				nc++;
				id++,jd++;
			}
			else{
				jd++;
			}
		}
		int kc=0;
		id=0,jd=0;
		while(jd!=N){
			if(a[id]<b[jd]){
				kc++;
				id++,jd++;
			}
			else{
				jd++;
			}
		}
		printf("%d %d\n",nc,N-kc);
	}
	return 0;
}

