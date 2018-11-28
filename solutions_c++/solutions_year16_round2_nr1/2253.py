#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int num, i, j;
	char arr[2001];
	int abc[36];
	int number[10];;
	scanf("%d", &num);
	getchar();
	for (i = 0; i < num; i++){
		for (j = 0; j < 26; j++){
			abc[j] = 0;
		}
		for (j = 0; j < 10; j++){
			number[j] = 0;
		}
		while (scanf("%c", &arr[i])){
			if (arr[i] == '\n') break;
			abc[arr[i] - 'A']++;
		}
		while (abc['S' - 'A'] > 0 && abc['I' - 'A'] > 0 && abc['X' - 'A'] > 0){
			abc['S' - 'A']--;
			abc['I' - 'A']--;
			abc['X' - 'A']--;
			number[6]++;
		}
		while (abc['Z' - 'A'] > 0 && abc['E' - 'A'] > 0 && abc['R' - 'A'] > 0 && abc['O' - 'A'] > 0){
			abc['Z' - 'A']--;
			abc['E' - 'A']--;
			abc['R' - 'A']--;
			abc['O' - 'A']--;
			number[0]++;
		}
		while (abc['E' - 'A'] > 0 && abc['I' - 'A'] > 0 && abc['G' - 'A'] > 0 && abc['H' - 'A'] > 0 && abc['T' - 'A']>0){
			abc['E' - 'A']--;
			abc['I' - 'A']--;
			abc['G' - 'A']--;
			abc['H' - 'A']--;
			abc['T' - 'A']--;
			number[8]++;
		}
		while (abc['F' - 'A'] > 0 && abc['O' - 'A'] > 0 && abc['U' - 'A'] > 0 && abc['R' - 'A'] > 0){
			abc['F' - 'A']--;
			abc['O' - 'A']--;
			abc['U' - 'A']--;
			abc['R' - 'A']--;
			number[4]++;
		}
		while (abc['F' - 'A'] > 0 && abc['I' - 'A'] > 0 && abc['V' - 'A'] > 0 && abc['E' - 'A'] > 0){
			abc['F' - 'A']--;
			abc['I' - 'A']--;
			abc['V' - 'A']--;
			abc['E' - 'A']--;
			number[5]++;
		}
		
		while (abc['T' - 'A'] > 0 && abc['W' - 'A'] > 0 && abc['O' - 'A'] > 0){
			abc['T' - 'A']--;
			abc['W' - 'A']--;
			abc['O' - 'A']--;
			number[2]++;
		}
		while (abc['N' - 'A'] >= 2 && abc['E' - 'A'] > 0 && abc['I' - 'A'] > 0){
			abc['E' - 'A']--;
			abc['I' - 'A']--;
			abc['N' - 'A'] -= 2;
			number[9]++;
		}
		while (abc['O' - 'A'] > 0 && abc['N' - 'A'] > 0 && abc['E' - 'A'] > 0){
			abc['O' - 'A']--;
			abc['N' - 'A']--;
			abc['E' - 'A']--;
			number[1]++;
		}
		while (abc['T' - 'A'] > 0 && abc['E' - 'A'] >= 2 && abc['R' - 'A'] > 0 && abc['H' - 'A'] > 0){
			abc['T' - 'A'] --;
			abc['H' - 'A']--;
			abc['R' - 'A']--;
			abc['E' - 'A'] -= 2;
			number[3]++;
		}
		while (abc['S' - 'A'] > 0 && abc['E' - 'A'] > 1 && abc['V' - 'A'] > 0 && abc['N' - 'A'] > 0){
			abc['S' - 'A']--;
			abc['V' - 'A']--;
			abc['E' - 'A']-=2;
			abc['N' - 'A']--;
			number[7]++;
		}
		printf("Case #%d: ", i + 1);
		for (j = 0; j < 10; j++){
			while (number[j] > 0){
				printf("%d", j);
				number[j]--;
			}
		}
		printf("\n");
	}
	return 0;
}