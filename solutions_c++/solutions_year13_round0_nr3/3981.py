#include<cstdio>
#include<cstring>

#define MaxLen 210

char strNum[MaxLen+1];
char newNum[MaxLen+1];
char inputFrom[MaxLen+1],inputTo[MaxLen+1];
int inputFromLen,inputToLen;
int squareTemp[MaxLen+1];

void Square(){
	int i,j,remainder = 0;
	int strNumLen = strlen(strNum);
	int temp;

	newNum[MaxLen] = '\0';
	squareTemp[MaxLen] = 0;
	for(i=0;i<MaxLen;i++){
			newNum[i] = '0';
			squareTemp[i] = 0;
	}
	for(i=0;i<strNumLen;i++){
			for(j=0;j<strNumLen;j++){
					squareTemp[i+j] += (strNum[i]-'0')*(strNum[j]-'0');
			}
	}
	for(i=0;i<MaxLen;i++){
			newNum[MaxLen-i-1] += squareTemp[i] %10;
			squareTemp[i+1] += squareTemp[i]/10;
	}
}

int IsPalindrome(){
	int i;
	int start,end = MaxLen-1;
	for(start = 0;newNum[start] == '0';start++);
	while(start < end){
			if(newNum[start] != newNum[end]) return 0;
			start++;
			end--;
	}
	return 1;
}

int main(){
	int testcaseCount;
	int i,j,a,num,temp;
	long long answer;

	scanf("%d",&testcaseCount);
	for(a=1;a<=testcaseCount;a++){
			answer = 0;
			scanf("%s %s",inputFrom,inputTo);
			inputFromLen = strlen(inputFrom);
			inputToLen = strlen(inputTo);

			// Align input number to right for easier calculation
			for(i=inputFromLen;i>=0;i--) inputFrom[MaxLen+i-inputFromLen] = inputFrom[i];
			for(i=0;i<MaxLen-inputFromLen;i++) inputFrom[i] = '0';

			for(i=inputToLen;i>=0;i--) inputTo[MaxLen+i-inputToLen] = inputTo[i];
			for(i=0;i<MaxLen-inputToLen;i++) inputTo[i] = '0';

			// Palindrome type 1: 1234554321

			num = 0;
			do{
					num++;

					sprintf(strNum,"%d",num);
					temp = strlen(strNum);
					for(i=0;i<=temp;i++){
							strNum[temp+i] = strNum[temp-i-1];
					}
					strNum[temp*2] = '\0';

					//Compute strNum Squared and collect into newNum (right-aligned)
					Square();
			}while(strcmp(newNum,inputFrom) < 0);

			num--;

			while(1){
					num++;

					sprintf(strNum,"%d",num);
					temp = strlen(strNum);
					for(i=0;i<=temp;i++){
							strNum[temp+i] = strNum[temp-i-1];
					}
					strNum[temp*2] = '\0';

					//Compute strNum Squared and collect into newNum (right-aligned)
					Square();
					if(strcmp(newNum,inputTo) <= 0){
							if(IsPalindrome()){
									//printf("%s\n",newNum);
									answer++;
							}
					}else{
							break;
					}
			}

			// Palindrome type 2: 123454321

			num = 0;
			do{
					num++;

					sprintf(strNum,"%d",num);
					temp = strlen(strNum);
					for(i=0;i<temp;i++){
							strNum[temp+i] = strNum[temp-i-2];
					}
					strNum[temp*2-1] = '\0';

					//Compute strNum Squared and collect into newNum (right-aligned)
					Square();
			}while(strcmp(newNum,inputFrom) < 0);

			num--;

			while(1){
					num++;

					sprintf(strNum,"%d",num);
					temp = strlen(strNum);
					for(i=0;i<temp;i++){
							strNum[temp+i] = strNum[temp-i-2];
					}
					strNum[temp*2-1] = '\0';

					//Compute strNum Squared and collect into newNum (right-aligned)
					Square();
					if(strcmp(newNum,inputTo) <= 0){
							if(IsPalindrome()){
									//printf("%s\n",newNum);
									answer++;
							}
					}else{
							break;
					}
			}

			printf("Case #%d: %lld\n",a,answer);
	}

	return 0;
}

