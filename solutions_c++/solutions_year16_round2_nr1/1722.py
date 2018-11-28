#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
int count[260];
int answer[10];

main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int t, tcase = 1;
	char str[2005];
	scanf("%d",&t);
	for(int i = 0; i < t; i++) {
		scanf("%s", str);
		int j;
		int len = strlen(str);
		for(j = 'A'; j <= 'Z'; j++) {
			count[j] = 0;
		}
		for(j = 0 ; j <= 9; j++) answer[j] = 0;
		for(int j = 0; j < len; j++) {
			count[str[j]]++;
		}
		
		while(count['W'] > 0) {
			answer[2]++;
			count['T']--;
			count['W']--;
			count['O']--;
		}
		
		while(count['G'] > 0) {
			answer[8]++;
			count['E']--;
			count['I']--;
			count['G']--;
			count['H']--;
			count['T']--;
		}
		
		while(count['X'] > 0) {
			answer[6]++;
			count['S']--;
			count['I']--;
			count['X']--;
		}
		
		while(count['Z'] > 0) {
			answer[0]++;
			count['Z']--;
			count['E']--;
			count['R']--;
			count['O']--;
		}
		
		while(count['S'] > 0) {
			answer[7]++;
			count['S']--;
			count['E']--;
			count['V']--;
			count['E']--;
			count['N']--;
		}
		
		while(count['V'] > 0) {
			answer[5]++;
			count['F']--;
			count['I']--;
			count['V']--;
			count['E']--;
		}
		
		while(count['F'] > 0) {
			answer[4]++;
			count['F']--;
			count['O']--;
			count['U']--;
			count['R']--;
		}
		
		while(count['I'] > 0) {
			answer[9]++;
			count['N']--;
			count['I']--;
			count['N']--;
			count['E']--;
		}
		
		while(count['N'] > 0) {
			answer[1]++;
			count['O']--;
			count['N']--;
			count['E']--;
		}
		
		while(count['H'] > 0) {
			answer[3]++;
			count['T']--;
			count['H']--;
			count['R']--;
			count['E']--;
			count['E']--;
		}
		
		printf("Case #%d: ", tcase++);
		for(j = 0; j <= 9; j++) {
			for(int k = 0; k < answer[j]; k++) {
				printf("%d", j);
			}
		}
		printf("\n");
	}
}

