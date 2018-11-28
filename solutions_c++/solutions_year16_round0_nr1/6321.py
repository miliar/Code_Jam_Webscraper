#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define maxLength 1000
#define maxNLength 10

void addN(int value[], int* length, int n[], int* lengthN) {
	int carry = 0;
	for(int i=0; i<*lengthN; i++) {
		int tmp = n[i]+ value[i] + carry;
		carry = tmp/10;
		value[i] = tmp%10;
	}
	int position = *lengthN;
	while(carry > 0) {
		int tmp = value[position] + carry;
		carry = tmp/10;
		value[position] = (tmp%10);
		position += 1;
	}
	if(*length < position)
		*length = position;
}

bool ifSeeAll(bool index[], int value[], int length) {
	for(int i=0; i<length; i++)
		index[value[i]] = true;
	bool flag = true;
	for(int i=0; i<10; i++) 
		if(index[i]==false)
			flag = false;
	return flag;
}

int main() {
	int testCase;
	scanf("%d\n", &testCase);
	for(int t=0; t<testCase; t++) {
		int value[maxLength];
		int n[maxNLength];
		memset(value, 0, sizeof(char)*maxLength);
		memset(n, 0,  sizeof(char)*maxNLength);
		int input;
		scanf("%d\n",&input);
		int lengthN = 0;
		while(input > 0) {
			n[lengthN] = input%10;
			input = input/10;
			lengthN += 1;
		}
		if(lengthN == 0) {
			printf("Case #%d: INSOMNIA\n", t+1);
			continue;
		}
		int length = 1;
		int ans = 0;
		bool index[10];
		for(int i=0; i<10; i++)
			index[i] = false;
		while(1) {
			addN(value, &length, n, &lengthN);
			ans += 1;
			if(ifSeeAll(index, value, length)==true) {
				printf("Case #%d: ", t+1);
				for(int i=length-1; i>=0; i--)
					printf("%d", value[i]);
				printf("\n");
				break;
			}
		}
	}
	
	
	return 0;
}
