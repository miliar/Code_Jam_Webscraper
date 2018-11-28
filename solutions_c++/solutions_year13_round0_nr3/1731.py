#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
using namespace std;

bool isPalin(long long int val){
	long long int inv=0,dig,var=val;
	while(var>0){
		dig=var%10;
		inv=inv*10+dig;
		var/=10;
	}
	if(val==inv)
		return true;
	return false;
}


class solver{
	//constants
	long long int UPPINT,*psarr;
	int UPPSIZE,size;
	//variables

	public:
	solver();
	void setup();
	int solve(long long int low, long long int high);
	void print(long long int high);
};

solver::solver(){
	//set up constants
	UPPINT=pow(10,14);
	UPPSIZE=pow(10,7);
	psarr=new long long int[UPPSIZE];
	size=0;//size of psarr
	setup();
}

void
solver::setup(){
	//set up fixed vars
	long long int val;
	for(long long int i=1;i<UPPSIZE;i++){
		if(isPalin(i)){
			val=i*i;
			if(isPalin(val)){
				psarr[size++]=val;
			}
		}
	}
}

int 
solver::solve(long long int low, long long int high){
	int total=0;
	for(int i=0;i<size;i++){
		if(psarr[i]>=low && psarr[i]<=high){total++;}
		else if(psarr[i]>high){break;}
	}
	return total;
}

void 
solver::print(long long int high){
	for(int i=0;i<size;i++){
		if(psarr[i]<=high){printf("%lld ",psarr[i]);}
		else if(psarr[i]>high){break;}
	}
	cout<<endl;
}

int main(){
	int casenum;
    long long int low,high;

    scanf("%d\n",&casenum);

    solver meg;
    //meg.print(1000);
    for(int k=0;k<casenum;k++){

        scanf("%lld %lld\n",&low,&high);
        int res=meg.solve(low,high);
        printf("Case #%d: %d\n",k+1,res);
    }


	return 0;
}