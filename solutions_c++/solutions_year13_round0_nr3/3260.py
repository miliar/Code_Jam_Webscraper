#include <iostream>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

bool palindrome(int n) {
	int rev = 0,ford = n;
	int ret = true;
	while(n != 0) {
		rev = rev * 10;
		rev = rev + n % 10;
		n = n / 10;
	}
	//cout << "n " << n << "rev " << rev << endl;
	if(ford != rev) ret = false;
	return ret;
}

int solve(int A,int B, map<int,int> store) {
	int ctr = 0;
	for(int i= A; i <= B; i++) {
		if(store[i]) {
			//cout << i << " " << store[i] << endl;
			if(palindrome(i) && palindrome(store[i])) {
				ctr++;
			}
		}
	}
	return ctr;
}

int main() {
	int T, A, B;
	int cases = 0;
	scanf("%d", &T);
	map<int,int> store;
	for(int i=1; i <= 1000; i++) {
		store[i*i] = i;
	}
	while(T--) {
		cases += 1;
		scanf("%d %d", &A, &B);
		int ret = solve(A,B,store);
		printf("Case #%d: %d\n", cases, ret);
	}
	return 0;
}