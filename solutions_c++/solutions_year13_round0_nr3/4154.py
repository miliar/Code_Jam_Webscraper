// Used boost multiprecision library @ http://www.boost.org/users/history/version_1_53_0.html
// and GMP library @ http://gmplib.org/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <boost/multiprecision/gmp.hpp>
using namespace std;
using boost::multiprecision::mpz_int;
using boost::multiprecision::mpf_float;


typedef struct Limits {
    mpz_int smallest;
    mpz_int biggest;
} Limits;


void output_answer(mpz_int number_of_palindromes, fstream& output_file) {
    output_file << number_of_palindromes;
}

bool is_palindrome_helper(string& s, int i, int j) {
    return (j - i < 1) || ((s[i] == s[j]) && (is_palindrome_helper(s, i+1, j-1)));
}

bool is_palindrome(string& s) {
    return is_palindrome_helper(s, 0, s.size() - 1);
}

void check_if_has_fair_square(Limits& limits, mpz_int& number, mpz_int& number_of_fair_and_square) {
    // Find square of this palindrome
    mpz_int square(number);
    square *= square;
    string square_string = square.str();
    bool square_is_palindrome = is_palindrome(square_string);
    if (square_is_palindrome && square >= limits.smallest && square <= limits.biggest) {
        number_of_fair_and_square++;
    }
}

mpz_int generate_fair_square(Limits& limits) {
    mpz_int number_of_fair_and_square(0);
    string number;

    mpf_float start_from(limits.smallest);
    mpf_float work_until(limits.biggest);
    start_from = boost::multiprecision::sqrt(start_from);
    work_until = boost::multiprecision::sqrt(work_until);
    mpz_int start_from_int(start_from);
    mpz_int work_until_int(work_until);

    mpz_int nine("9");
    mpf_float ten_float("10");

    if (start_from < ten_float) {
        for (mpz_int i = start_from_int; i <= nine && i <= work_until_int; i++) {
            check_if_has_fair_square(limits, i, number_of_fair_and_square);
        }
    }

    // Prepare digits to insert between numbers
    bool still_work_to_do = true;
    vector<char> digits;
    for (int i = 0; i <= 9; i++) {
        digits.push_back('0' + i);
    }

    for (mpz_int i = 1; still_work_to_do; i++) {
        // Convert to string
        number = i.str();
        string reversed_number = number;
        still_work_to_do = false;

        // Prepare reverse
        reverse(reversed_number.begin(), reversed_number.end());

        // Prepare palindrome when no digit is in between
        string nothing_between_number = number + reversed_number;
        mpz_int nothing_between_number_big(nothing_between_number);
        if (nothing_between_number_big <= work_until_int) {
            still_work_to_do = true;

            check_if_has_fair_square(limits, nothing_between_number_big, number_of_fair_and_square);
        }

        // Use all digits between number and its reverse
        for (vector<char>::iterator it = digits.begin(); it != digits.end(); it++) {
            string new_number = number + *it + reversed_number;
            mpz_int new_number_big(new_number);
            // If between limits, good to go
            if (new_number_big <= work_until_int) {
                still_work_to_do = true;
                check_if_has_fair_square(limits, new_number_big, number_of_fair_and_square);
            }
        }
    }
    return number_of_fair_and_square;

}

void find_number_of_fair_square_numbers(Limits& limits, fstream& output_file) {
    mpz_int number_of_fair_squares;
    number_of_fair_squares = generate_fair_square(limits);
    output_answer(number_of_fair_squares, output_file);
}

int main()
{
    fstream input_file;
    fstream output_file;
    input_file.open("fair_and_square.in", ios::in);
    output_file.open("fair_and_square.out", ios::out | ios::trunc);
    if (input_file.is_open() && output_file.is_open()) {
        int test_cases;
        input_file >> test_cases;
        input_file.get(); // Skip newline

        string line_of_input;
        for (int i = 1; i <= test_cases; i++) {
            Limits limits;

            getline(input_file, line_of_input);
            stringstream ss(line_of_input);
            ss >> limits.smallest;
            ss >> limits.biggest;

            output_file << "Case #" << i << ": ";
            find_number_of_fair_square_numbers(limits, output_file);
            if (i < test_cases) {
                output_file << "\n";
            }
        }
        input_file.close();
        output_file.close();
    } else {
        cout << "Error opening file.";
    }
    return 0;
}

