#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;


bool is_square(unsigned long long num){
	double d_sqrt = sqrt(num);
	unsigned long long i_sqrt = d_sqrt;
	return d_sqrt == i_sqrt;

}


bool is_palindrome(unsigned long long num){
    unsigned long long n, digit, rev = 0;
    n = num;
    do {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     } while (num!=0);
    //cout << " The reverse of the number is: " << rev << endl;
	return n == rev;
}
int main(){
	int cases;
	unsigned long long low, high, count;
	cin >> cases;
	for (int i = 0; i < cases; i++){
		count = 0;
		// cout << "hello" << endl;
		// scanf("%d %d", &low, &high);
		cin >> low >> high;
		//cout << low << " " << high << endl;
		for (unsigned long long j = low; j < high+1; j++){
			if (is_square(j) && is_palindrome(j) && is_palindrome(sqrt(j))){
				count++;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	
}