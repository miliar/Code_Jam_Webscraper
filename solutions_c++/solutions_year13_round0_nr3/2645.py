#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPalindrome(int a){
	int b = 0, temp = a;
	while (temp){
		b = 10*b + temp%10;
		temp/=10;
	}
	return (a == b);
}

int main(){
        ifstream in("C-small-attempt0.in");
        ofstream out("bar");

        int T;
        in >> T;

	for (int p = 0; p < T; p++){
		int answer = 0;
		int a, b;
		in >> a >> b;	
		for (int i = floor(sqrt(a) - 1); i <=sqrt(b) + 1; i++){
			if (isPalindrome(i*i) && isPalindrome(i) && i*i >= a && i*i <= b)
				answer++;
		}
		out << "Case #" << p+1 << ": " << answer << endl;
	}
	
	return 0;
}
