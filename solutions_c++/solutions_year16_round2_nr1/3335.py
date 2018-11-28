#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

#define mem0(x) memset(x, 0, sizeof(x))
#define mem1(x) memset(x, -1, sizeof(x))

char str[5005];
int dig[30];
char S[10][10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int num[10];

void print(){
	for(int i = 0; i < 26; i++) printf("%d ", dig[i]);
	printf("\n");
}

int main(){
	int t, _case = 1;
//	for(int i = 0; i < 10; i++) puts(S[i]);
	scanf("%d", &t);
	while(t--){
		mem0(dig);
		mem0(num);
		scanf("%s", str);
		int len = strlen(str);
		for(int i = 0; i < len; i++){
			dig[str[i]-'A']++;
		}
		printf("Case #%d: ", _case++);
		if(dig['W'-'A']>0){
			num[2] = dig['W'-'A'];
			for(int i = 0; i < 3; i++)
				dig[S[2][i]-'A']-=num[2];		
		}
		if(dig['G'-'A']>0){
			num[8] = dig['G'-'A'];
			for(int i = 0; i < 5; i++)
				dig[S[8][i]-'A']-=num[8];			
		}	
		if(dig['T'-'A']>0){
			num[3] = dig['T'-'A'];
			for(int i = 0; i < 5; i++)
				dig[S[3][i]-'A']-=num[3];			
		}
		if(dig['Z'-'A']>0){
			num[0] = dig['Z'-'A'];
			for(int i = 0; i < 4; i++)
				dig[S[0][i]-'A']-=num[0];		
		}
		if(dig['X'-'A']>0){
			num[6] = dig['X'-'A'];
			for(int i = 0; i < 3; i++)
				dig[S[6][i]-'A']-=num[6];		
		}
		if(dig['S'-'A']>0){
			num[7] = dig['S'-'A'];
			for(int i = 0; i < 5; i++)
				dig[S[7][i]-'A']-=num[7];
		}
		if(dig['R'-'A']>0){
			num[4] = dig['R'-'A'];
			for(int i = 0; i < 4; i++)
				dig[S[4][i]-'A']-=num[4];
		}
		if(dig['V'-'A']>0){
			num[5] = dig['V'-'A'];
			for(int i = 0; i < 4; i++)
				dig[S[5][i]-'A']-=num[5];
		}
		if(dig['I'-'A']>0){
			num[9] = dig['I'-'A'];
			for(int i = 0; i < 4; i++)
				dig[S[9][i]-'A']-=num[9];
		}
		num[1] = dig['E'-'A'];
		for(int i = 0; i < 10; i++)
			for(int j = 0; j < num[i]; j++)
				printf("%d", i);
		printf("\n");
	}
	return 0;
} 
