#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
#include <map>

#define MaxLength INT_MAX
#define MaxNode 12
#define MN 1005

using namespace std;
unsigned int N,M,T;

int mem[MN][MN];
double Naomi[MN];
double Ken[MN];

int main(){
	int i,j,k,tt,a,b,r,c,s,t,n,d,x,y,A,B,C,F,X,R;
	int res1,res2;
	scanf("%d",&T);
	
	for(tt=1; tt<=T; tt++){
		res1 = 0;
		res2 = 0;
		scanf("%d",&N);
		for(i=0; i<N; i++)
			scanf("%lf",&Naomi[i]);
		for(i=0; i<N; i++)
			scanf("%lf",&Ken[i]);
		sort(Naomi,Naomi+N);
		sort(Ken,Ken+N);
		/*
		for(i=0; i<N; i++)
			printf(" %lf",Naomi[i]);
		puts("");
		for(i=0; i<N; i++)
			printf(" %lf",Ken[i]);
		puts("");
		*/

		res1 = 0;
		for(i=0,j=0; i<N; i++,j++){
			while(Ken[i] > Naomi[j] && j<N)
				j++;
			if(j==N){
				break;
			}
		}
		res1 = i;

		for(i=0,j=0; i<N; i++,j++){
			while(Naomi[i] > Ken[j] && j<N)
				j++;
			if(j==N){
				break;
			}
		}
		res2 = N-i;


		printf("Case #%d: %d %d\n",tt,res1,res2);	
	}
	return 0;
}