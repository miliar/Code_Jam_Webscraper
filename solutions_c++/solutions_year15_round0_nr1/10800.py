#include <stdio.h>

int e(int a){
	int i,p=1;
	for(i=0;i<a;i++) p*=10;
	return p;	
}

int main(){
	int i,Si,Sm,t,emp=0,j=0;
	char a[1005];
	FILE *arq1 = fopen("A-small-attempt2.in", "r");
	FILE *arq2 = fopen("output.txt", "w");	
	
	fscanf(arq1, "%i",&t);
	int resp[t];
	for(i=0;i<t;i++){
		fscanf(arq1, "%i %s",&Sm,a);
		for(Si=0;Si<Sm+1;Si++){
			while(emp<Si) emp++;
			emp+=a[Si]-'0';
			j+=a[Si]-'0';
		}
		resp[i]=emp-j;
		emp=0;
		j=0;
	}
	for(i=1;i<=t;i++) fprintf(arq2, "Case #%i: %i\n",i,resp[i-1]);
	return 0;
}
