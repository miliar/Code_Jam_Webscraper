#include <stdio.h>
#include <iostream>	

void cookies(FILE *p,int n,FILE *q){
	double c,f,x;
	double rate = 2;
	double timeBuy,timeToX,totTime;
	fscanf(p,"%lf",&c);
	fscanf(p,"%lf",&f);
	fscanf(p,"%lf",&x);
	totTime=0;
	for(;;){
		timeToX = x/(rate);
		timeBuy = c/rate;
		if(totTime + timeToX < (totTime + timeBuy + x/(rate+f))){
			break;
		}
		rate = rate + f;
		totTime = totTime + timeBuy;
	}
	totTime=totTime + x/rate;
	printf("Case #%d: %.7lf\n\n",n,totTime);
	fprintf(q,"Case #%d: %.7lf\n",n,totTime);
}


int main(){
	char c;
	int t,n=1;
	FILE *p,*q;
	q = fopen("output.txt","w");
	if (q==NULL){ 
		printf( "erro\n\n");
	};
	p = fopen("B-large.in","r");
	if (p==NULL){ 
		printf( "erro\n\n");
	}
	fscanf(p,"%d",&t);
	//printf("%d\n",t);
	
	while (!feof(p)){
		cookies(p,n,q);
		n++;
	}
	system("PAUSE");
	return 0;
}

/**/