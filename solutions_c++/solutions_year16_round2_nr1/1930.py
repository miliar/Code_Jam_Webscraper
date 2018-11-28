#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

/*
0 - Z
1 - O
2 - W
3 - H
4 - U
5 - F
6 - X
7 - S
8 - G
9 - I
*/

char digits[10][20] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
	"SIX", "SEVEN", "EIGHT", "NINE"
};

void reduce(int digit, char c, int *d, int *ans) {
	while(d[c]) {
		ans[digit]++;
		for(int j=0;j<strlen(digits[digit]);j++) {
			d[digits[digit][j]]--;
		}
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		char s[2001];
		scanf("%s",&s);
		int d[128]={0};
		for(int i=0;i<strlen(s);i++)d[s[i]]++;
		int ans[10]={0};
		reduce(0, 'Z', d, ans);
		reduce(2, 'W', d, ans);
		reduce(4, 'U', d, ans);
		reduce(5, 'F', d, ans);
		reduce(6, 'X', d, ans);
		reduce(8, 'G', d, ans);
		reduce(3, 'H', d, ans);
		reduce(9, 'I', d, ans);
		reduce(7, 'S', d, ans);
		reduce(1, 'O', d, ans);
		printf("Case #%d: ", casenum);
		for(int i=0;i<10;i++)
			for(int j=0;j<ans[i];j++)
				printf("%d",i);
		puts("");

	}
	return 0;
}