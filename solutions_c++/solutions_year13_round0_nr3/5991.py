/*
	Here, I will go through the whole interval
	and check if its palindrome. If its a palindroms
	I will find its square root and check is its a palindrome.

	Tested under the case for
	1 ≤ T ≤ 100.
	1 ≤ A ≤ B ≤ 1000.

	@author: Chirag Maheshwari
*/
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

bool checkPalindrome(int num) {
	int rev = 0, temp = num;

	while(temp > 0) {
		rev = (rev*10) + (temp%10);
		temp /= 10;
	}

	if(rev == num)
		return true;
	else
		return false;
}

bool check_fair_square(int num) {
	if(!checkPalindrome(num))
		return false;

	int root = sqrt(num);
	if(root*root != num)
		return false;

	if(!checkPalindrome(root))
		return false;
	
	return true;
}

int main() {
	int T, a, b, count;
	scanf("%d", &T);

	for(int z=1; z<=T; z++) {
		scanf("%d%d", &a, &b);
		count = 0;
		for(int i=a; i<=b; i++) {
			if(check_fair_square(i)) {
				count++;
				// cout<<i<<endl;
			}
		}

		printf("Case #%d: %d\n", z, count);
	}
}