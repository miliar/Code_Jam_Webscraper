#include<stdio.h>
#include<stdlib.h>

int main(){
FILE *pt=fopen("in1.txt","r");
FILE *po = fopen("out1.txt","w");
int t,i=0,j;
double c,f,x,time,time1,time2;

fscanf(pt,"%d",&t);

while(t--){
	i++;
	fscanf(pt,"%lf %lf %lf",&c,&f,&x);
	
	time= 0.0;
	for(j=1;;j++){
		time1 = (c/(2+f*(j-1))) + x/(2+f*j);
		time2 = x/(2+f*(j-1));
		
		if(time1<time2){
			time += (c/(2+f*(j-1)));
		}
		else{
			time += time2;
			break;
		}
	}
	
	fprintf(po,"Case #%d: %.7lf\n",i,time);
	
}


}
