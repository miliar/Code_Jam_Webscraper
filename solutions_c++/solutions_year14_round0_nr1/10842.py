#include <stdio.h>
#include <stdlib.h>

int main(){
	int nCases;
	int rowNum;
	int curRow;
	int a, b, c, d;
	int a2, b2, c2, d2;
	int discard;
	int nPoss, answer;
	
	scanf("%d", &nCases);
	
	for(int i = 1; i <= nCases; i++){
		scanf("%d", &rowNum);
		for(int curRow = 1; curRow <= 4; curRow++){
			if(curRow == rowNum){
				scanf("%d %d %d %d", &a, &b, &c, &d);
			} else {
				scanf("%d %d %d %d", &discard, &discard, &discard, &discard);
			}
		}
		scanf("%d\n", &rowNum);
		for(int curRow = 1; curRow <= 4; curRow++){
			if(curRow == rowNum){
				scanf("%d %d %d %d", &a2, &b2, &c2, &d2);
			} else {
				scanf("%d %d %d %d", &discard, &discard, &discard, &discard);
			}
		}
		nPoss = 0;
		if (a == a2 || a == b2 || a == c2 || a == d2){
			nPoss++;
			answer = a;
		}
		if(b == a2 || b == b2 || b == c2 || b == d2){
			nPoss++;
			answer = b;
		}
		if(c == a2 || c == b2 || c == c2 || c == d2){
			nPoss++;
			answer = c;
		}
		if(d == a2 || d == b2 || d == c2 || d == d2){
			nPoss++;
			answer = d;
		}
		if(nPoss == 0){
			printf("Case #%d: Volunteer cheated!\n", i);
		} else if(nPoss > 1){
			printf("Case #%d: Bad magician!\n", i);
		} else {
			printf("Case #%d: %d\n", i, answer);
		}
	}
}