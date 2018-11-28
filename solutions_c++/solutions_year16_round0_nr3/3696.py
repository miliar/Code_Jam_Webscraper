#include<cstdio>

void print8Div(){
	int i=2;
	while(i<=10){
		int res = 1;
		int adder = 1;
		int adderCnt = 0;
		while(adderCnt < 8){
			adder *= i;
			adderCnt++;
		}
		if(i != 10) printf("%d ",res+adder);
		else printf("%d\n",res+adder);
		i++;
	}
}

void print8Num(int counter){
	printf("1");
	int digits[6];
	int i=5;
	while(i>=0){
		digits[i] = counter % 2;
		counter /= 2;
		i--;
	}
	for(int j=0; j<6; j++){
		printf("%d",digits[j]);
	}
	printf("11");
	for(int j=0; j<6; j++){
		printf("%d",digits[j]);
	}
	printf("1 ");
}


int main(){
	int T;
	scanf("%d",&T);
	int N;
	scanf("%d",&N);
	int J;
	scanf("%d",&J);
	int i=0;
	while(i<J){
		printf("Case #%d:\n",i+1);
		print8Num(i);
		print8Div();
		i++;
	}
}
