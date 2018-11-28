#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

string N[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR",
				 "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int L[10][26]; // Letter frequency for each number

int P[10]; // Number of numbers in phone number

void dfs(int *F, int low) {
	bool done = true;
	for(int i=0; i<26; i++) {
		if(F[i] > 0) {
			done = false;
			break;
		}
	}
	if(done) {
		for(int i=0; i<10; i++) {
			for(int j=0; j<P[i]; j++) {
				printf("%d", i);
			}
		}
		printf("\n");
		
		return;
	}
	
	for(int i=low; i<10; i++) {
		bool works = true;
		for(int j=0; j<26; j++) {
			if(F[j] < L[i][j]) {
				works = false;
				break;
			}
		}
		if(works) {
			P[i]++;
			for(int j=0; j<26; j++) {
				F[j] -= L[i][j];
			}
			
			dfs(F, i);
			
			P[i]--;
			for(int j=0; j<26; j++) {
				F[j] += L[i][j];
			}
		}
	}
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	for(int i=0; i<10; i++) {
		string s = N[i];
		for(int j=0; j<s.length(); j++) {
			L[i][s[j] - 'A']++;
		}
	}
	
	int nn;
	scanf("%d\n", &nn);
	for(int cc=1; cc<=nn; cc++) {
		printf("Case #%d: ", cc);
		
		string s;
		getline(cin, s);
		
		int F[26]; // Letter frequency in phone number
		for(int i=0; i<26; i++) F[i] = 0;

		for(int i=0; i<s.length(); i++) {
			F[s[i] - 'A']++;
		}
		
		for(int i=0; i<10; i++) P[i] = 0;
		dfs(F, 0);
	}
	
	return 0;
}
