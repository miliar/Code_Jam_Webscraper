#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
	int cases;
	scanf("%d", &cases);
	for(int i1 = 1;i1 <= cases;i1++) {
		int x;
		int r;
		int c;
		scanf("%d %d %d", &x, &r, &c);
		int t1 = r;
		int t2 = c;
		if(t1 < t2) {
			int t = t1;
			t1 = t2;
			t2 = t;
		}
		if(x == 1) {
			printf("Case #%d: GABRIEL\n",i1);
		}else if(x == 2){
			if((t1 * t2) % 2 == 0) {
					printf("Case #%d: GABRIEL\n",i1);
			}else {
				printf("Case #%d: RICHARD\n",i1);
			}
		}else if(x == 3) {
			if(t1 == 3 && t2 == 3) {
				printf("Case #%d: GABRIEL\n",i1);
			}else if(t1 == 3 && t2 == 2) {
				printf("Case #%d: GABRIEL\n",i1);
			}else if(t1 == 4 && t2 == 3) {
				printf("Case #%d: GABRIEL\n",i1);
			}else {
				printf("Case #%d: RICHARD\n",i1);
			}
		}else {
			if(t1 == 4 && t2 == 3) {
				printf("Case #%d: GABRIEL\n",i1);
			}else if(t1 == 4 && t2 == 4) {
				printf("Case #%d: GABRIEL\n",i1);
			}else {
				printf("Case #%d: RICHARD\n",i1);
			}
		}
	}
	return 0;
}
