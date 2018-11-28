#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>

using namespace std;

bool
    is_palindrome (uint64_t number)
{
    uint64_t original = number;
    uint64_t reversed = 0;
    while (number > 0)
    {
        uint64_t digit = number % 10;
        reversed = digit + reversed * 10;
        number = number / 10;
    }

    return (original == reversed);
}

int 
	main () 
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");
		
	size_t test_count;	
	in >> test_count;


	for (size_t i = 1; i <= test_count; ++i) {
        uint64_t low;
        uint64_t high;

        in >> low;
        in >> high;

        uint64_t count = 0;
        uint64_t low_sqrt = sqrt((double)low)-1;        
        uint64_t high_sqrt = sqrt((double)high)+1;

        for (uint64_t sqrt = low_sqrt; sqrt <= high_sqrt; ++sqrt) {
            if (is_palindrome(sqrt)) {
                uint64_t num = sqrt*sqrt;
                if (num > high) {
                    break;
                }
                if (num >= low && is_palindrome(num)) {
                    ++count;
                }
            }
        }

        out << "Case #" << i << ": " << count << endl; 
    }

    in.close();
    out.close();
}
