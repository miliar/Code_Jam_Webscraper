#include<stdio.h>
int checkcase(int temp){
	int token = 1;
	int arr[10] = {0};
	int number=temp;
	int digittemp;
	int digit=-1;
	for(int a=1;;++a){
		digittemp = number = temp*a;
		while(number>0){
			arr[number%10]=1;
			for(int i=0;i<10;++i){
				if(arr[i]==0) token=0;
			}
			if(token==1){
				digit = digittemp;
				return digit;
			}
			else token=1;
			number/=10;
		}
	}
}
int main(){
	FILE * fout;
	if(!(fout=fopen("small_output.txt","w"))){
		perror("small_output.txt");
		return 0;
	}
	freopen("A-small-attempt0.in","r",stdin);
	int test;
	scanf("%d",&test);
	int temp;
	for(int i=1;i<=test;++i){
		scanf("%d",&temp);
		if(temp==0) fprintf(fout,"Case #%d: INSOMNIA\n",i);
		else {
			fprintf(fout,"Case #%d: %d\n",i,checkcase(temp));
		}
	}
	return 0;
}