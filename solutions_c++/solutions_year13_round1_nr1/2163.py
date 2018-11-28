#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <vector>
#include <algorithm>
#include <map>

#define _USE_MATH_DEFINES
#define	M_PI   3.14159265358979323846

using namespace std;

typedef unsigned long long ull;

bool func(vector<int> arr,vector<int> arr2){
	return (arr[0]<arr2[1]);
}

int main(int argc,char **argv){
	FILE *fin,*fout;
	int cases=0;
	int N=0;
	ull r=0,t=0;
	int i=0,j=0,k=0;
	clock_t t0;
	t0=clock();
	char tmp=0;
	double pi=3.14159265358979323846;
	double v=0.0;
	long double a=0.0,b=0.0,c=0.0,n=0.0;
	double delta=0.0000000000001;
	ull num=0;


	fin =fopen("A-small-attempt0.in","rt");
	fout=fopen("A-small-attempt0.out","wt");
	
	fscanf(fin,"%d\n",&cases);
	for(i=1;i<=cases;i++){
		fprintf(fout,"Case #%d: ",i);
		fscanf(fin,"%llu %llu", &r,&t);
		printf("%llu %llu\n",r,t);
		//n=((double)t)/(pi*2.0*((double)(r+1))*();
		a=1.0;
		b=((double)(2.0*((double)r)-1.0))/(2.0);
		c=-((double)t)/(2.0);
		printf("a = %lf\n",a);
		printf("b = %lf\n",b);
		printf("c = %lf\n",c);
		n=(-b+sqrt(b*b-4*a*c))/(2*a);
		//n=sqrt(c+b*b)-b;
		//n=sqrt((((double)t)/2.0)+((2.0*((double)r)-1.0)/4.0))-((2.0*((double)r)-1.0)/4.0);
		//num=((ull)floor(n-delta))-1;
		num=((ull)floor(n));
		printf("n = %lf = %llu\n\n",n,num);
		fprintf(fout," %llu\n",num);
	}
	
	
	fclose(fin);
	fclose(fout);

	printf("Time taken = %lf\n",(double)(clock()-t0)/(double)CLOCKS_PER_SEC);
	return 0;
}