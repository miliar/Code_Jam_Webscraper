#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <limits>
#include <algorithm>
#include <functional>
#include <vector>
#include <stack>
#include <queue>
#include <set>

using namespace std;

bool check(double);
double func(double,double);

int main(){
	int tt,t;
	FILE *in=fopen("A-small-attempt0.in","r");
	FILE *out=fopen("A-small-attempt0.out","w");
	fscanf(in,"%d",&t);
	tt=t;
	while(t--){
		double p,q;
		char trash;
		double pro;
		fscanf(in,"%lf %c %lf",&p,&trash,&q);
		pro=p/q;
		q=q/func(p,q);
		if(check(q)){
			fprintf(out,"Case #%d: impossible\n",tt-t);
			continue;
		}
		int i;
		for(i=0;pro<1;i++)
			pro*=2;
		fprintf(out,"Case #%d: %d\n",tt-t,i);
	}
	return 0;
}

bool check(double a){
	while(a>=1){
		a/=2;
		if(a==1)
			return 0;
	}
	return 1;
}

double func(double a,double b){
	if(a<b)
		swap(a,b);
	if(a-b==b)
		return b;
	a=a-b;
	return func(a,b);
}