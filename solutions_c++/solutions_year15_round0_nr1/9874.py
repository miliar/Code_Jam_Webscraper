#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
	int T, Sm, res, sum;
	char Sarr[1001];
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		res = 0;
		sum = 0;
		scanf("%d %s", &Sm, &Sarr);
		for(int j = 0; j <= Sm; j++) {
			if(sum < j) {
				res += j - sum;
				sum = j;
			}
			sum += Sarr[j] - '0';
		}
		
		cout << "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}