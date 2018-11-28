#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define N 2005

int anum[256];
char s[N];
int num[10];

int main(){
	int tcase;
	scanf("%d", &tcase);
	for(int icase = 1; icase <= tcase; icase++){
		scanf("%s", s);
		int len = strlen(s);
		memset(anum, 0, sizeof(anum));
		memset(num, 0, sizeof(num));
		for(int i = 0; i < len; i++){
			anum[s[i]]++;
		}
		num[0] = anum['Z'];
		num[2] = anum['W'];
		num[4] = anum['U'];
		num[6] = anum['X'];
		num[8] = anum['G'];
		num[1] = anum['O'] - num[0] - num[2] - num[4];
		num[3] = anum['T'] - num[2] - num[8];
		num[5] = anum['F'] - num[4];
		num[7] = anum['S'] - num[6];
		num[9] = anum['I'] - num[5] - num[6] - num[8];
		printf("Case #%d: ", icase);
		for(int i = 0; i < 10; i++){
			for(int j = 0; j < num[i]; j++){
				printf("%d", i);
			}
		}
		printf("\n");
	}
	return 0;
}
