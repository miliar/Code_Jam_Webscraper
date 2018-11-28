#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int flag[10];
int digit_cnt;

void checkDigit(long long num){
	int digit;
	while(num>0){
		digit = num%10;
		if(flag[digit]==0){
			digit_cnt++;
			flag[digit]=1;
		}
		num = num/10;
		//printf("*%lld\n",num);
	}
}

int main(){
	FILE* fin = fopen("CS_in.txt","r");
	FILE* fout = fopen("CS_out.txt","w");
	int T;
	long long num;
	int mul;
	fscanf(fin,"%d",&T);
	for(int i=1;i<=T;i++){
		fscanf(fin,"%lld",&num);
		//printf("%lld\n", num);
		if(num == 0){
			fprintf(fout,"Case #%d: INSOMNIA\n",i);
			continue;
		}
		for(int j=0;j<10;j++){
			flag[j]=0;
		}
		digit_cnt = 0;
		mul = 1;
		while(digit_cnt<10){
			//printf("**%lld\n",num);
			checkDigit(num*mul);
			mul++;
		}
		fprintf(fout, "Case #%d: %lld", i,(num*(mul-1)));
		if(i<T){
			fprintf(fout, "\n");
		}

	}
	fclose(fout);
	fclose(fin);
	return 0;	
}