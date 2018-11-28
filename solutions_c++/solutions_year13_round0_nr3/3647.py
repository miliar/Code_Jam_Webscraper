#include <algorithm>
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>

bool isPalindrome(int x) {
	char buffer[102]; 
	itoa(x, buffer, 10);
	int length = strlen(buffer)-1;
	for(int i = 0; i <= length; i++)
		if (buffer[i] != buffer[length-i]) 
			return 0;
	return 1;
}

void main() {
	int i,T,Trun=1;
	int A,B,number,number2,counter;
	std::cin >> T;
	while (Trun <= T) {
		counter = 0;
		std::cin >> A >> B;
		number = 1;
		number2 = number*number;
		while ( number2 < A) {
			number++;
			number2 = number*number;
		}
		while ( number2 <= B) {
			if (isPalindrome(number) && isPalindrome(number2)) {
				counter++;
				// printf("*");
			}
			// printf("%d %d\n",number,number2);
			number++;
			number2 = number*number;
		}
		printf("Case #%d: %d\n",Trun++,counter);
	}
}

