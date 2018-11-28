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
#define MN 20

using namespace std;
unsigned int N,M,T;

int mem[MN];


int main(){
	int i,j,k,tt,a,b,c,s,t,n,d,x,y,A,B;
	double res,C,F,X;
	scanf("%d",&T);
	
	for(tt=1; tt<=T; tt++){
		scanf("%lf %lf %lf",&C,&F,&X);
		res = X/2;
		double curTime = 0;
		double curGain = 2;
		while (curTime < res){
			double wait = C / curGain;
			curGain += F;
			curTime += wait;

			res = min(curTime + X / curGain,res);
		}
		
		printf("Case #%d: %.9lf\n",tt,res);
	}
	return 0;
}