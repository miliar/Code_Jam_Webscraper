#include <iostream>
#include <limits>
#include <string>
#include <sstream>

bool is_palindrome(const int number)
{
    std::ostringstream oss;
    oss << std::dec << number;
    std::string num_str = oss.str();

    for(int i=0, j=num_str.size()-1 ; i<j ; i++, j--)
    {
        if(num_str[i] != num_str[j]) { return false; }
    }

    return true;
}

int main()
{
    int N;
    std::cin >> N;
    ++N;//test cases are indexed from 1

    //now ingore the rest of the line inc newline, eases some tests that
	//try to read a line at a time (and stick on this \n if not removed)
    std::cin.ignore( std::numeric_limits<std::streamsize>::max() , '\n' );


    for( int test_case=1 ; test_case<N ; ++test_case )
    {
    //Prep
        long count = 0;
        long long min, max;
        std::cin >> min >> max;

        long long root=1;

        while(true)
        {
            long long val = root*root;
            if(val > max) { break; }
            if(min <= val && is_palindrome(root) && is_palindrome(val)) { count += 1; }
            ++root;
        }

    //Work
        std::cout << "Case #" << test_case << ": " << count << std::endl;

    //Clean Up
    }
}
