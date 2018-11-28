/*
Revenges of Pancakes
Tanat Jiwapornkupt
09/04/16
CodeJam 2016
*/
#include <stdio.h>
#include <string.h>

int nq;
char s[102];
int counter;

int tmp;
int len;
int i;

int main(){
	freopen("inputBL.txt","r",stdin);
	freopen("outputBL.txt","w",stdout);
	scanf("%d",&nq);
	tmp = nq;
	while(nq--){
		printf("Case #%d: ",tmp-nq);
		scanf("%s",&s);
	//	printf("String = %s\n",s);
		len = strlen(s);
		counter = 0;
		s[len] = '+';
		if(s[0]=='-'){
			if(s[1]=='+') counter++;
		}
		for(i=1;i<len;i++){
			if(s[i]=='-'){
				if(s[i-1]=='+') counter++;
				if(s[i+1]=='+') counter++;
			}
		}
		printf("%d\n",counter);
	}	
	return 0;
}
