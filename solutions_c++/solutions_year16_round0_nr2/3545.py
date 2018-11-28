#include <stdio.h>
#include <string.h>
int main(){
	FILE *f = fopen("outB.txt","wt");
	int T,i;
	char S[200];
	scanf("%d",&T);
	for(i=0;i<T;i++){
		scanf("%s",S);
		int count=0;
		while(true){
			int check=0,leng=strlen(S);
			for(int j=0;j<leng;j++){
				if(S[j]=='-') check=1;
			}
			if(check==0) break;
			if(S[0]=='-'){
				int x=0;
				while(x<leng && S[x]=='-'){
					S[x]='+';
					x+=1;
				}
				count+=1;
			}
			else{
				int x=0;
				while(x<leng && S[x]=='+'){
					S[x]='-';
					x+=1;
				}
				count+=1;
			}
		}
		fprintf(f, "Case #%d: %d\n",i+1,count);
	}
	fclose(f);
}