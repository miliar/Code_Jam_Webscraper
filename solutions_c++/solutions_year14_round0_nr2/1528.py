#include "iostream"
#include "stdio.h"
#include "cmath"
#include "cstring"
using namespace std;

#define pi 	3.14159265359
#define e 	2.71828

#define FOR(max) for(int i=0;i<max;i++)
#define FORi(i,max) for(int i=0;i<max;i++)
#define FOR2(min,max) for(int i=min;i<=max;i++)
#define FOR2i(i,min,max) for(int i=min;i<=max;i++)
#define SQR(n) ((n)*(n))
#define CUBE(n) ((n)*(n)*(n))



int main(){
	#ifdef CODEJAM_INPUT
		freopen("in.txt","r",stdin);
		freopen("B-large.out","w",stdout);
	#endif

	int T,ans,ch1,ch2,exists;
	cin>>T;

	double C,F,X,R;

	double t0=0;//t1,t2;
	double last,cur;

	// cout<<T;
	// return 0;

	//T=2;
	FORi(tt,T){
		R=2;
		t0=0;

		cin>>C>>F>>X;

		last=(X/R);
		while(true){
			cur=t0+(C/R)+(X/(R+F));
			if(cur>last)
				break;
			//printf("%f %f\n",t1,t2);
			last=cur;
			t0+=C/R;
			R+=F;
		}


		printf("Case #%d: %.7f\n",tt+1,last);
		
	}

	return 0;
}