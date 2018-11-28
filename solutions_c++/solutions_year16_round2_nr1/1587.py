#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;


int main( void ) {
	int T;
	scanf("%i", &T);
	
	char *digits[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int order[10] = {0, 2, 4, 6, 8, 3, 1, 5, 7, 9};
	
	for( int t = 1; t <= T; t++ ) {
		char S[2222];
		scanf("%s", S);
		
		int n = strlen(S);
		
		int letters[26] = {0};
		for( int i = 0; i < n; i++ ) {
			letters[S[i]-'A']++;
		}
		
		vector<int> phone;
		for( int i = 0; i < 10; i++ ) {
			int idx = order[i];
			
			while( true ) {
				int req[26] = {0};
				for( int j = 0; j < strlen(digits[idx]); j++ ) {
					char c = digits[idx][j];
					req[c-'A']++;
				}
				
				bool can = true;
				for( int j = 0; j < 26; j++ ) {
					if( letters[j] < req[j] ) {
						can = false;
					}
				}
				
				if( can ) {
					phone.push_back(order[i]);
					for( int j = 0; j < 26; j++ ) {
						letters[j] -= req[j];
					}
				} else {
					break;
				}
			}
		}
		
		sort(phone.begin(), phone.end());
		
		printf("Case #%i: ", t);
		for( int e : phone ) printf("%i", e);
		puts("");
	}
	
	return 0;
}