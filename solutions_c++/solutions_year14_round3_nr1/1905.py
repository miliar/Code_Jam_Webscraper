#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <stdlib.h>

using namespace std;

FILE *f1,*f2;
	

int main(){

	int t=0;
	char c=0;
	double f=0;
	char num[30];
	
	f1=fopen("A-small-attempt1.in","r");
	f2=fopen("A-small-attempt1out.out","w");

//	f1=fopen("Bin.txt","r");
//	f2=fopen("Bout.txt","w");


	fscanf(f1,"%d",&t);


//	cin>>t;

	for(int aa=0; aa<t; aa++){
		int cnt=0, x=0;
		int a=0, b=0;

		fscanf(f1,"%s",num);



//		cin>>num;
		for(x=0; num[x]!='/'; x++){
			a*=10;
			a+=(num[x]-48);
		}
		x++;
		for(; num[x]!=0; x++){
			b*=10;
			b+=(num[x]-48);
		}
	
		double db;
		db=log10((double)b)/log10(2.0);


		if(db-(int)db!=0){
			fprintf(f2,"Case #%d: impossible\n",aa+1);
			continue;
		}

		f=(double)a/(double)b;
		
		int k=0;
		k=log10((double)a)/log10(2.0);


//		while(f<1){
//			f*=2;
//			cnt++;
//		}

//		if(f-1==0) {
//			printf("Case #%d: %d\n",aa+1,(int)db-k);
//			continue;
//		}

	
		fprintf(f2,"Case #%d: %d\n",aa+1,(int)db-k);
		
	}
	


	
    return 0;

}
