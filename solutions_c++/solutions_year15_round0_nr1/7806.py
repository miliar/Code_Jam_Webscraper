#include<stdio.h>

int t;
int a;
int arr[1002];
int sum=0;
int result=0;
int old=0;


int main(){

	
	FILE *txt;
	txt = fopen("A-large.in","r");
	FILE *out;
	out = fopen("out.txt","w");

	while(fscanf(txt,"%d",&t)!=EOF){

	for(int i=0;i<t;i++){
		fscanf(txt,"%d",&a);

		for(int j=0;j<=a;j++){
			fscanf(txt,"%1d",&arr[j]);
			sum = sum + arr[j];	
			if(sum < j+1){
				old = result;
				result = result + (j+1-sum);
				sum = sum+(result-old);
			}
		}

		
		fprintf(out,"Case #%d: %d\n",i+1,result);

		sum = 0;
		result = 0;
		old = 0;

	}

	}

	return 0;

}