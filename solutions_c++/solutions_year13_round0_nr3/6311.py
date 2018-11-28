#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>

using namespace std;

list <unsigned int> 
reverse_digitalize (unsigned long num) 
{
  list <unsigned int> digits;
  unsigned int i = 1;
  unsigned int divider = 10;
  unsigned long n = num;

  while (n >= divider) {
     unsigned int remainder = n % divider;
     digits.push_back(remainder);
	n /= divider;
  }
  digits.push_back(n);
  return digits;
}

unsigned long
numerize (list <unsigned int> M) 
{
	unsigned long num = 0;
	list <unsigned int> :: iterator it = M.begin();
	for (; it != M.end(); it++) {
	     num = num * 10 + *it;
	}
	return num;
}

int 
isPerfect_Square (unsigned long A)
{
	double d_sqrt = sqrt(A);
	unsigned long i_sqrt = d_sqrt;
	if (i_sqrt == d_sqrt) {
	    return 1;
	}
	return 0;
}

int 
isPalindrome(unsigned long A) 
{
	list <unsigned int> LL = reverse_digitalize(A);
	if (A == numerize(LL)) {
	    return 1;
	}
	return 0;
}

unsigned int 
Fair_Square(unsigned long A, unsigned long B)
{
	unsigned long num = A;
	unsigned long i_sqrt;
	unsigned count = 0;
	unsigned int LSB;

	if (A > B) {
	    return count;
	}

	while (num <= B) {
		LSB = num % 10;
		
		if (LSB != 0 && LSB != 4 && LSB != 5 && LSB != 6 && LSB != 9 && LSB != 1) {
		    num++;
		    continue;
		}

		if (isPalindrome(num) && isPerfect_Square(num)) {
		    if (isPalindrome(sqrt(num))) {
			   count++;
		    }
		}
		num++;
	}

	return count;
}


int main(int argc, char **argv) {
	int case_num = 1;
	char buffer[100];
	string str;
	bool first = 0;
	int total_cases;
	unsigned int TC_num = 0;
	unsigned long A, B;
	unsigned int count;
	
	ifstream read_file (argv[1]);

	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
			 } else {
				 stringstream ss(str);
				 ss >> A >> B;
				 count = Fair_Square(A, B);
				 cout << "Case #" << ++TC_num <<": "<< count << endl;
			 }
	    }
	    read_file.close();
	}
}
