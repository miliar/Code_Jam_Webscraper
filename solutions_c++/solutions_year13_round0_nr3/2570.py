/* Fair and square */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cerr;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;
#include <sstream>

#include <math.h>

using namespace std;

unsigned long long fair_sqr[39];

bool is_palindrome(unsigned long long val)
{
	unsigned long long rem, sum = 0;
	unsigned long long numbers = val;
	while (numbers != 0) {
		rem = numbers % 10;
		numbers = numbers / 10;
		sum = sum * 10 + rem;
	}
	if (val == sum) {
		return true;
	}		
	return false;
}

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
  
	size_t cases;
	input_file >> cases;
	
	
	unsigned long long A, B, n, num, count = 0;
	
	A = 1;
	B = 100000000000000;
	
	n = ceil(sqrt(A));
	
	for ( ;;n++) {
		num = pow(n, 2);
		if (num > B) {
			break;
		}
		if (is_palindrome(sqrt(num)) && (is_palindrome(num))) {
			fair_sqr[count++] = num;
		}
	}
	int max = count;
			
	for (size_t i = 1; i <= cases; ++i) {
		count = 0;
		input_file >> A;
		input_file >> B;

		
		int start_pos = 0, end_pos = 0;
		bool found_pos = false;
		for (int from = 0; from < max; ++from) {
			if (A <= fair_sqr[from]) {
				start_pos = from;
				found_pos = true;
				break;
			}
		}
		
		if (!found_pos) {
			output_file << "Case #" << i << ": 0";
			if (i != cases) {
				output_file << endl;
			}
			continue;
		}
		
		found_pos = false;
		for (int from = start_pos; from < max; ++from) {
			if (B == fair_sqr[from]) {
				end_pos = from;
				found_pos = true;
				break;
			} else if (B < fair_sqr[from]) {
				end_pos = from - 1;
				found_pos = true;
				break;
			}
		}
		if (!found_pos) {
			end_pos = max - 1;
		}
		count = end_pos - start_pos + 1;
		
		output_file << "Case #" << i << ": " << count;
		if (i != cases) {
			output_file << endl;
		}
	
	}				
	
    input_file.close();
    output_file.close();
	return 0;
}