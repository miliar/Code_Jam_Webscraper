#include<cstdio>

unsigned int answer;
unsigned int a,b,k;

unsigned int Calc(unsigned int curDigit, unsigned int num1, unsigned int num2, unsigned int targetNum){
	if(curDigit == 0){
//		printf("<%u,%u> = %u\n",num1,num2,num1&num2);
		return 1;
	}
	if((int)(curDigit & targetNum) != 0){
		return Calc(curDigit/2, num1, num2, targetNum);
	}
	unsigned int count = 0;
	//0 0
	count += Calc(curDigit/2, num1, num2, targetNum);
	//1 0
	if(num1+curDigit < a){
		count += Calc(curDigit/2, num1+curDigit, num2, targetNum);
	}
	//0 1
	if(num2+curDigit < b){
		count += Calc(curDigit/2, num1, num2+curDigit, targetNum);
	}
	return count;
}

int main(){

	unsigned int i,j;
	unsigned int testcaseCount,testcase;
	unsigned int temp;
	
	scanf("%u",&testcaseCount);
	for(testcase = 1; testcase <= testcaseCount; testcase++){
		scanf("%u %u %u",&a,&b,&k);
		answer = 0;
		temp = 1;
		while(temp < a || temp < b) temp <<= 1;
//		printf("<<<<<%u>>>>>>>>\n",temp);
		for(i=0;i<k && i<a && i<b;i++){
			answer += Calc(temp,i,i,i);
		}
		
		printf("Case #%u: %u\n",testcase,answer);
	}
	
	return 0;
}
