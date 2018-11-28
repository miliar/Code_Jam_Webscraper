#include<stdio.h>
//#include<iostream>
#include<stdlib.h>
//#include<algorithm>
#include<math.h>
#include<string.h>

// If max = 1, f1 is greater
// If max = 2, f2 is grarter
// If max = 0, both equals

int len;
char ans1[20], ans2[20];
bool haveAns;

int min(int a, int b) {
	if(a < b) return a;
	return b;
}

void cur(int j, char str1[], char str2[], int status) {
	//printf("%s %s\n", str1, str2);
	if(j >= len) {
		//printf("\t %s %s\n", str1, str2);
		if(!haveAns) {
			strcpy(ans1, str1);
			strcpy(ans2, str2);
			haveAns= true;
		} else {
			if(len <= 9) {
				int a, b, c, d;
				sscanf(ans1, "%d", &a);
				sscanf(ans2, "%d", &b);
				
				sscanf(str1, "%d", &c);
				sscanf(str2, "%d", &d);
				
				//printf("\t\t %d %d %d %d\n", a, b, c, d);
				
				if(abs(c - d) < abs(a - b)) {
					strcpy(ans1, str1);
					strcpy(ans2, str2);
				} else if(abs(c - d) == abs(a - b)) {
					if(c < a) {
						strcpy(ans1, str1);
						strcpy(ans2, str2);
					} else if(c == a && d < b) {
						strcpy(ans1, str1);
						strcpy(ans2, str2);
					}
				}
			} else {
				int a1, a2, b1, b2, c1, c2, d1, d2;
				char a1front[15], a1back[15], a2front[15], a2back[15];
				for(int i = 0; i < 9; i++) {
					a1front[i] = ans1[i];
					a2front[i] = ans2[i];
				}
				a1front[9] = '\0';
				a2front[9] = '\0';
				
				for(int i = 9; i < len; i++) {
					a1back[i] = ans1[i];
					a2back[i] = ans2[i];
				}
				a1back[len] = '\0';
				a2back[len] = '\0';
				
				sscanf(a1front, "%d", &a1);
				sscanf(a2front, "%d", &c1);
				sscanf(a1back, "%d", &b1);
				sscanf(a2back, "%d", &d1);
				
				//------------------------
				
				for(int i = 0; i < 9; i++) {
					a1front[i] = str1[i];
					a2front[i] = str2[i];
				}
				a1front[9] = '\0';
				a2front[9] = '\0';
				
				for(int i = 9; i < len; i++) {
					a1back[i] = str1[i];
					a2back[i] = str2[i];
				}
				a1back[len] = '\0';
				a2back[len] = '\0';
				
				sscanf(a1front, "%d", &a2);
				sscanf(a2front, "%d", &c2);
				sscanf(a1back, "%d", &b2);
				sscanf(a2back, "%d", &d2);
				
				if(abs(a2 - c2) != abs(a1 - c1) || abs(b2 - d2) != abs(b1 - d1)) {
					if(abs(a2 - c2) < abs(a1 - c1) || (abs(a2 - c2) == abs(a1 - c1) && abs(b2 - d2) < abs(b1 - d1))) {
						strcpy(ans1, str1);
						strcpy(ans2, str2);
					}
				} else {
					if(a2 < a1 || (a2 == a1 && c2 < c1)) {
						strcpy(ans1, str1);
						strcpy(ans2, str2);
					} else if (b2 < b1 || (b2 == b1 && d2 < d1)) {
						strcpy(ans1, str1);
						strcpy(ans2, str2);
					}
				}
			}
		}
		return;
	}
	if(status == 0) {
		if(str1[j] == '?' && str2[j] == '?') {
			str1[j] = '0';
			str2[j] = '0';
			cur(j + 1, str1, str2, 0);
			
			str1[j] = '1';
			str2[j] = '0';
			cur(j + 1, str1, str2, 1);
			
			str1[j] = '?';
			str2[j] = '?';
			
			str1[j] = '0';
			str2[j] = '1';
			cur(j + 1, str1, str2, 2);
			
			str1[j] = '?';
			str2[j] = '?';
		} else if(str1[j] == '?' && str2[j] != '?') {
			str1[j] = str2[j];
			cur(j + 1, str1, str2, 0);
			
			str1[j] = (((str2[j] - '0') + 1) % 10) + '0';
			cur(j + 1, str1, str2, 1);
			
			str1[j] = (((str2[j] - '0') - 1 + 10) % 10) + '0';
			cur(j + 1, str1, str2, 2);
			
			str1[j] = '?';
		} else if(str2[j] == '?' && str1[j] != '?') {
			str2[j] = str1[j];
			cur(j + 1, str1, str2, 0);
			
			str2[j] = (((str1[j] - '0') + 1) % 10) + '0';
			cur(j + 1, str1, str2, 2);
			
			str2[j] = (((str1[j] - '0') - 1 + 10) % 10) + '0';
			cur(j + 1, str1, str2, 1);
			
			str2[j] = '?';
		} else {
			if(str1[j] > str2[j]) status = 1;
			else if(str2[j] > str1[j]) status = 2;
			cur(j + 1, str1, str2, status);
		}
	} else {
		if(str1[j] == '?' && str2[j] =='?') {
			if(status == 1) {
				str1[j] = '0';
				str2[j] = '9';
			} else if(status == 2) {
				str2[j] = '0';
				str1[j] = '9';
			}
			cur(j + 1, str1, str2, status);
			str1[j] = '?';
			str2[j] = '?';
		} else if(status == 1 && str1[j] != '?' && str2[j] == '?') {
			str2[j] = '9';
			cur(j + 1, str1, str2, status);
			str2[j] = '?';
		} else if(status == 2 && str2[j] != '?' && str1[j] == '?') {
			str1[j] = '9';
			cur(j + 1, str1, str2, status);
			str1[j] = '0';
		} else if(status == 1 && str2[j] != '?' && str1[j] == '?') {
			str1[j] = '0';
			cur(j + 1, str1, str2, status);
			str1[j] = '?';
		} else if(status == 2 && str1[j] != '?' && str2[j] == '?') {
			str2[j] = '0';
			cur(j + 1, str1, str2, status);
			str2[j] = '?';
		} else cur(j + 1, str1, str2, status);
	}
}

main() {
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t, tcase = 1;
	scanf("%d", &t);
	int i;
	char str1[20], str2[20];
	for(i = 0; i < t; i++) {
		scanf("%s %s", str1, str2);
		len = strlen(str1);
		haveAns = false;
		cur(0, str1, str2, 0);
		/*int status = 0;
		for(int j = 0; j < len; j++) {
			if(status == 0) {
				if(str1[j] == '?' && str2[j] == '?') {
					str1[j] = '0';
					str2[j] = '0';
				} else if(str1[j] == '?' && str2[j] != '?') {
					str1[j] = str2[j];
				} else if(str2[j] == '?' && str1[j] != '?') {
					str2[j] = str1[j];
				} else {
					if(str1[j] > str2[j]) status = 1;
					else if(str2[j] > str1[j]) status = 2;
				}
			} else if(str1[j] == '?' && str2[j] =='?') {
				if(status == 1) {
					str1[j] = '0';
					str2[j] = '9';
				} else if(status == 2) {
					str2[j] = '0';
					str1[j] = '9';
				}
			} else if(status == 1 && str1[j] != '?' && str2[j] == '?') {
				str2[j] = '9';
			} else if(status == 2 && str2[j] != '?' && str1[j] == '?') {
				str1[j] = '9';
			} else if(status == 1 && str2[j] != '?' && str1[j] == '?') {
				str1[j] = '0';
			} else if(status == 2 && str1[j] != '?' && str2[j] == '?') {
				str2[j] = '0';
			} 
		}*/
		printf("Case #%d: ", tcase++);
		printf("%s %s\n", ans1, ans2);
	}
}

