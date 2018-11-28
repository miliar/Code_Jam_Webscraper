#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

int h[20];

int main(){
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i ++){
		int Ans;
		memset(h, 0, sizeof(h));
		scanf("%d", &Ans);	
		Ans --;
		for (int j = 0; j < 4; j ++)
			for (int k = 0; k < 4; k ++){
				int x;
				scanf("%d", &x);
				if (j == Ans){
					h[x] = 1;	
				}
			}
		scanf("%d", &Ans);	
		Ans --;
		for (int j = 0; j < 4; j ++)
			for (int k = 0; k < 4; k ++){
				int x;
				scanf("%d", &x);
				if (j == Ans){
					h[x] *= 1;	
				}else h[x] *= 0;
			}
		int sum = 0, Out = 0;
		for (int j = 1; j <= 16; j ++)
			if (h[j] == 1) {
				sum ++; 
				Out = j;
			}
		if (sum == 1)
			printf("Case #%d: %d\n", i + 1, Out);
		if (sum > 1)
			printf("Case #%d: Bad magician!\n", i + 1);
		if (sum == 0)
			printf("Case #%d: Volunteer cheated!\n", i + 1);
	}
}

