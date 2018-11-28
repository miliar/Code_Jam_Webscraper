#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;
const string num[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int T;					 //		//		//		//		//		// 		//		//		//		 //
int main() {
	scanf("%d", &T);
	char s[2500];
	for (int time = 1; time <= T; time++) {
		int Num[26] = { 0 };
		int Ans[10] = { 0 };
		printf("Case #%d: ", time);
		scanf("%s", s);
		for (int i = 0; i < strlen(s); i++) {
			Num[s[i] - 'A']++;
		}
		while (Num['Z' - 'A']--) {
			Num['E' - 'A']--;
			Num['R' - 'A']--;
			Num['O' - 'A']--;
			Ans[0]++;
		}
		while (Num['X' - 'A']--) {
			Num['S' - 'A']--;
			Num['I' - 'A']--;
			Ans[6]++;
		}
		while (Num['W' - 'A']--) {
			Num['T' - 'A']--;
			Num['O' - 'A']--;
			Ans[2]++;
		}
		while (Num['G' - 'A']--) {
			Num['E' - 'A']--;
			Num['I' - 'A']--;
			Num['H' - 'A']--;
			Num['T' - 'A']--;
			Ans[8]++;
		}
		while (Num['U' - 'A']--) {
			Num['F' - 'A']--;
			Num['O' - 'A']--;
			Num['R' - 'A']--;
			Ans[4]++;
		}
		while (Num['O' - 'A']--) {
			Num['N' - 'A']--;
			Num['E' - 'A']--;
			Ans[1]++;
		}
		while (Num['F' - 'A']--) {
			Num['I' - 'A']--;
			Num['V' - 'A']--;
			Num['E' - 'A']--;
			Ans[5]++;
		}
		while (Num['I' - 'A']--) {
			Num['N' - 'A']--;
			Num['N' - 'A']--;
			Num['E' - 'A']--;
			Ans[9]++;
		}
		while (Num['R' - 'A']--) {
			Num['T' - 'A']--;
			Num['H' - 'A']--;
			Num['E' - 'A']--;
			Num['E' - 'A']--;
			Ans[3]++;
		}
		while (Num['S' - 'A']--) {
			Num['E' - 'A']--;
			Num['V' - 'A']--;
			Num['E' - 'A']--;
			Num['N' - 'A']--;
			Ans[7]++;
		}
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < Ans[i]; j++)
				printf("%d", i);
		printf("\n");
	}
}