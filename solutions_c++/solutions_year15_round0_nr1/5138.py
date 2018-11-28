#define _CRT_SECURE_NO_WARNINGS

#define INPUT "A-large.in"
#define OUTPUT "output.txt"

#include <iostream>
using namespace std;

int T;
int S, i, j;
int cnt, clapCnt;
char str[1002];

int main(){
	freopen(OUTPUT, "w+", stdout);
	freopen(INPUT, "r", stdin);

	cin >> T;

	for (i = 0; i < T; i++){
		cin >> S;
		cin >> str;

		clapCnt = 0;
		cnt = 0;
		S++;
		for (j = 0; j <= S; j++){
			if (clapCnt < j){
				cnt += j - clapCnt;
				clapCnt = j;
			}
			clapCnt += str[j] - '0';
		}

		printf("Case #%d: %d\n", i + 1, cnt);
	}
}