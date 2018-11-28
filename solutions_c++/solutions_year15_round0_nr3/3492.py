#define _CRT_SECURE_NO_WARNINGS

#define INPUT "C-small-attempt1.in"
#define OUTPUT "output.txt"

#include <iostream>
using namespace std;

int T, L, X;
int i, j, k,l;
bool negative;
char input[10001];
char curr;

int map[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{ 0, 3, -4, -1, 2 },
	{ 0, 4, 3, -2, -1}
};


int main(){
	freopen(OUTPUT, "w+", stdout);
	freopen(INPUT, "r", stdin);

	cin >> T;

	for (i = 0; i < T; i++){
		cin >> L;
		cin >> X;
		for (j = 0; j < L; j++){
			cin >> input[j];
			input[j] -= 'g';
		}
		k = 2;
		l = 1;
		negative = false;

		while (X--){
			for (j = 0; j < L; j++){
				l = map[l][input[j]];
				if (l < 0){
					l *= -1;
					negative ^= true;
				}
				if (l == k){
					l = 1;
					k++;
				}
			}
		}
		
		printf("Case #%d: %s\n", i + 1, k == 5 && !negative && l == 1? "YES" : "NO");
	}
}