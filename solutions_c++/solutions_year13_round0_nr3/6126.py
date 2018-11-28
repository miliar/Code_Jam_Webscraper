#include <stdio.h>
#include <iostream>

using namespace std;

bool ePalindrome(int X){

	char num[10];
	int pos =0;
	bool resp=false;

	do{
		int resto = X%10;
		num[pos] = resto+48;
		X=X/10;
		pos++;
	}while(X>0);

	if(pos==1){
		resp = true;
	}else if(pos==3){
		if(num[0] == num[2])
		resp = true;
	}else if(pos==2){
		if(num[0] == num[1])
		resp = true;
	}	

	return resp;
}

int main(){

int N;
scanf("%d\n", &N);
int caso =1;
while(caso <= N){

int min, max;
scanf("%d %d", &min, &max);
//printf("%d %d\n",min,max);
int qnt=0;
int pos;

for(int i=1; i*i <= max; i++){
	int square = i*i;	
	if(square>=min){
		if(ePalindrome(square) && ePalindrome(i))
			qnt++;	
	}
}

printf("Case #%d: %d\n",caso,qnt);

caso++;
}

return 0;
}
