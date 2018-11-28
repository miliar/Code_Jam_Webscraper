#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;
int main()
 {
	int t;
	int i,j,k;
	scanf("%d",&t);
	getchar();
	freopen("a.txt","w",stdout);
	for (i = 0; i < t; i++) {
		int i1 = 0;
		int i2 = 0;
		int j1 = 0;
		int j2 = 3;
		int x = 0;
		int x1 = 0;
		int o = 0;int o1 = 0;
		int t = 0;int t1 = 0;
		int flag = 0;
		char a[4][4];
		int c = 0;
		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				cin >> a[j][k];
				if (a[j][k] == '.') {
					c = 1;
				}
				if (j == i1 && k == j1) {
					if (a[j][k] == 'X') {
						x++;
					} else if (a[j][k] == 'O') {
						o++;
					} else if (a[j][k] == 'T') {
						t++;
					}
					i1++;j1++;
				}
				if (j == i2 && k == j2) {
					if (a[j][k] == 'X') {
						x1++;
					} else if (a[j][k] == 'O') {
						o1++;
					} else if (a[j][k] == 'T') {
						t1++;
					}
					i2++;j2--;
				}
			}
		}

		
		if (x == 4) {
			printf("Case #%d: X won\n",i+1);
			flag = 1;		
		} else if (o == 4) {
			printf("Case #%d: O won\n",i+1);
			flag = 1;
		} else {
			if (x == 3 && t == 1) {
				printf("Case #%d: X won\n",i+1);
				flag = 1;
			} else if (o == 3 && t == 1) {
				printf("Case #%d: O won\n",i+1);
				flag = 1;
			}
		}
		if (flag == 0) {
		if (x1 == 4) {
			printf("Case #%d: X won\n",i+1);
			flag = 1;
		} else if (o1 == 4) {
			printf("Case #%d: O won\n",i+1);
			flag = 1;
		} else {
			if (x1 == 3 && t1 == 1) {
				printf("Case #%d: X won\n",i+1);
				flag = 1;
			} else if (o1 == 3 && t1 == 1) {
				printf("Case #%d: O won\n",i+1);
				flag = 1;
			}
		}
		}
		if (flag == 0) {	
		for (j = 0; j < 4; j++) {
			o = 0;t = 0;x = 0;
			for (k = 0; k < 4; k++) {
				if (a[j][k] == 'X') {
					x++;
				} else if (a[j][k] == 'O') {
					o++;
				} else if (a[j][k] == 'T') {
					t++;
				}
			}
			if (x == 4) {
				printf("Case #%d: X won\n",i+1);
				flag = 1;
				break;
			} else if (o == 4) {
				printf("Case #%d: O won\n",i+1);
				flag = 1;
				break;
			} else {
				if (x == 3 && t == 1) {
					printf("Case #%d: X won\n",i+1);
					flag = 1;
					break;
				} else if (o == 3 && t == 1) {
					printf("Case #%d: O won\n",i+1);
					flag = 1;
					break;
				}
			}
		}}
		if (flag == 0) {
		for (k = 0; k < 4; k++) {
			o = 0;t = 0;x = 0;
			for (j = 0; j < 4; j++) {
				if (a[j][k] == 'X') {
					x++;
				} else if (a[j][k] == 'O') {
					o++;
				} else if (a[j][k] == 'T') {
					t++;
				}
			}
			if (x == 4) {
				printf("Case #%d: X won\n",i+1);
				flag = 1;
				break;
			} else if (o == 4) {
				printf("Case #%d: O won\n",i+1);
				flag = 1;
				break;
			} else {
				if (x == 3 && t == 1) {
					printf("Case #%d: X won\n",i+1);
					flag = 1;
					break;
				} else if (o == 3 && t == 1) {
					printf("Case #%d: O won\n",i+1);
					flag = 1;
					break;
				}
			}
		}
		}
		if (flag == 0) {
			if(c == 1) {
				printf("Case #%d: Game has not completed\n",i+1);
			} else {
				printf("Case #%d: Draw\n",i+1);
			}
		}

	}
 }
