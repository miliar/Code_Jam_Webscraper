
//Problem C. Fair and Square

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;
#define mytype __int64

int n;
mytype a,b;

mytype pslist[100000];
int pslistsize;

int compute(){
	int i;
	int res=0;

	for (i=0;i<pslistsize;i++){
		if (pslist[i]>=a && pslist[i]<=b) {
			//cout<<res<<" "<<pslist[i]<<endl;
			res++;
		}
	}
	
	return res;
}

int ispali(mytype v){
	int res=1;
	mytype d=1;
	mytype val=v;
	while (val>=10) {
		val/=10;
		d*=10;
	}
	val=v;
	while (d>1){
		if (val%10 != val/d) return 0;
		val%=d; val/=10;
		d/=100;
	}
	return 1;
}

int main(){
	int t;
	int i,j,k;
	
	pslistsize=0;
	for (a=1;a<10000000;a++){
		if (ispali(a) && ispali(a*a)) {
			pslist[pslistsize]=a*a;
			pslistsize++;
			//cout<<a*a<<endl;
		}
	}


	//return 0;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>a>>b;

		k=compute();
		cout<<"Case #"<<(i+1)<<": ";
		cout<<k;
		cout<<endl;
	}
}
