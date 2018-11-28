#include <iostream>
#include <stdio.h>
#include <string>
 using namespace std;
int numbers[10];
void count(string str){
	for(int i=0; i<10; i++) numbers[i]=0;
	for(int i=0; i<str.length(); i++){
		char c = str[i];
		int k;
		if(c == 'Z') k=0;
		else if(c == 'O') k=1;
		else if(c == 'W') k=2;
		else if(c == 'H') k=3;
		else if(c == 'U') k=4;
		else if(c == 'F') k=5;
		else if(c == 'X') k=6;
		else if(c == 'V') k=7;
		else if(c == 'G') k=8;
		else if(c == 'I') k=9;
		else k=-1;
		if(k>=0)numbers[k]++;
	}

	numbers[1] = numbers[1]-numbers[0]-numbers[2]-numbers[4];
	numbers[3] = numbers[3]-numbers[8];
	numbers[5] -= numbers[4];
	numbers[7] -= numbers[5];
	numbers[9] = numbers[9]-numbers[5]-numbers[6]-numbers[8];
	
}


int main(){
	int N;
	scanf("%d", &N);
	string str;

	for(int i=0; i<N; i++){
		cin >> str;
		count(str);
		printf("Case #%d: ", i+1);
		for(int i=0; i<10; i++){
			int until = numbers[i];
			for(int j=0; j<until; j++) printf("%d", i);
		}
		printf("\n");
	}
	

}