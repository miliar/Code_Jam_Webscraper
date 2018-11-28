/* Fair and Square.

Is a square number, a palindrome, and its square root is also a palindrome.

Given interval [M, N], sqrt(n) is the ending point for checking */

#include <iostream>
#include <cmath>
	using namespace std;
	
int isPalindrome (int number) {

	int reverse = 0;
	int num = number;

	do {
	
		reverse = reverse*10 + number%10;
		number /= 10;
		
	} while (number > 0);
	
	if (reverse == num)
		return 1;
	else
		return 0;
		
}

int main() {

	int total;
	cin>>total;
	
	for (int k = 1; k <= total; k++) {
	
		int ll, ul;
		cin>>ll>>ul;
	
		int count = 0;
		
		for (int i = ceil(sqrt(ll)); i <= floor(sqrt(ul)); i++) {
		
			if (isPalindrome(i*i) && isPalindrome(i)) count++;
			
		}
			
		cout<<"Case #"<<k<<": "<<count<<endl;
		
	}
	
}