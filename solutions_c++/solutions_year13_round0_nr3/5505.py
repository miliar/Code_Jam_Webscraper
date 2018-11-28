#include <iostream>
#include <string>
#include <sstream>
#include <math.h>

std::string fromInToString (const float& digit) {
	std::string tmp;
	std::stringstream ss;
	ss << digit;
	ss >> tmp;
	return tmp;
}

bool isPalindrom (const float& digit) {
	std::string tmp = fromInToString(digit);
	for (int i = 0; i < tmp.size()/2; i++) {
		if (tmp[i] != tmp[tmp.size()-1-i]) return false;
	}
	return true;
}

bool isSQRT (const float& digit) {
	float a = sqrt(digit);
	std::string tmp = fromInToString(a);
	for (int i = 0; i < tmp.size(); i++) {
		if (tmp[i] == '.') return false;
	}
        if (!isPalindrom (a)) return false;
	return true;
}

int main ()
{
	int T = 0;
	std::cin >> T;
        int j = 0;
	while (j < T) {
           int count = 0;
	   int A = 0;
           int B = 0;
           std::cin >> A;
	   std::cin >> B;
           for (float i = A; i <= B; i++) {  
	      if (isPalindrom(i) && isSQRT(i)) {
		count++;
	      }
	   } 
           std::cout << "Case #" << j+1 << ": " << count << std::endl;
	   j++;
	}
}
