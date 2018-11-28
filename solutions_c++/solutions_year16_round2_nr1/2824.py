#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

#define MEM(v,i) memset(v,i,sizeof(v))

typedef long long int LL;

int array[28], result[2000], r_count = 0;

void include(int l, int k){
	while(l){
		result[r_count++] = k;
		l--;
	}
}
bool fun(int p, int k){
	int temp = 0;
	if(array[p]!=0){
		include(array[p],k);
		temp = array[p];
		switch(k){
			case(0): array['Z'-'A'] -= temp;
				 array['E'-'A'] -= temp;
				 array['R'-'A'] -= temp;
				 array['O'-'A'] -= temp;
				 break;
			case(1): array['O'-'A'] -= temp;
				 array['N'-'A'] -= temp;
				 array['E'-'A'] -= temp;
				 break;
			case(2): array['T'-'A'] -= temp;
				 array['W'-'A'] -= temp;
				 array['O'-'A'] -= temp;
				 break;
			case(3): array['T'-'A'] -= temp;
				 array['H'-'A'] -= temp;
				 array['R'-'A'] -= temp;
				 array['E'-'A'] -= 2*temp;
				 break;
			case(4): array['F'-'A'] -= temp;
				 array['O'-'A'] -= temp;
				 array['U'-'A'] -= temp;
				 array['R'-'A'] -= temp;
				 break;
			case(5): array['F'-'A'] -= temp;
				 array['I'-'A'] -= temp;
				 array['V'-'A'] -= temp;
				 array['E'-'A'] -= temp;
				 break;
			case(6): array['S'-'A'] -= temp;
				 array['I'-'A'] -= temp;
				 array['X'-'A'] -= temp;
				 break;
			case(7): array['S'-'A'] -= temp;
				 array['E'-'A'] -= 2*temp;
				 array['V'-'A'] -= temp;
				 array['N'-'A'] -= temp;
				 break;
			case(8): array['E'-'A'] -= temp;
				 array['I'-'A'] -= temp;
				 array['G'-'A'] -= temp;
				 array['H'-'A'] -= temp;
				 array['T'-'A'] -= temp;
				 break;
			case(9): array['N'-'A'] -= 2*temp;
				 array['I'-'A'] -= temp;
				 array['E'-'A'] -= temp;
				 break;
		}
	}
}

int main(){
	int test = 0, N = 0;
	int len = 0, i = 0;
	bool flag = 0;
	string s;
	scanf("%d",&test);
	for(int x_test = 1;x_test<=test; x_test++){
		MEM(array,0);
		MEM(result,0);
		r_count = 0;
		cin>>s;
		len = s.length();
		for(i = 0; i<len; i++){
			array[s[i]-'A']++;
		}
		fun((int)('Z'-'A'),0);
		fun((int)('W'-'A'),2);
		fun((int)('U'-'A'),4);
		fun((int)('X'-'A'),6);
		fun((int)('G'-'A'),8);
		fun((int)('O'-'A'),1);
		fun((int)('R'-'A'),3);
		fun((int)('F'-'A'),5);
		fun((int)('S'-'A'),7);
		fun((int)('I'-'A'),9);
		sort(result,result+r_count);
		printf("Case #%d: ",x_test);
		for(i = 0; i<r_count; i++){
			printf("%d",result[i]);
		}
		printf("\n");
	}
	return(0);
}
