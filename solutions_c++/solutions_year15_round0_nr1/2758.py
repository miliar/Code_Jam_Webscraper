#include <iostream>
using namespace std;

int T, S, freq, friends, sum;
char x;

int main() {
	scanf ("%d", &T);
	for (int k = 1 ; k <= T ; k++) {
		friends = sum = 0;
		scanf ("%d", &S);
		scanf ("%c", &x); // read space
		for (int i = 0 ; i <= S ; i++) {
			scanf ("%c", &x);
			freq = (int) (x-'0');
			if (sum < i) { 
				friends += i - sum; 
				sum = i; 
			}
			sum += freq;
		}
		printf ("Case #%d: %d\n", k, friends);
	}
	return 0;
}