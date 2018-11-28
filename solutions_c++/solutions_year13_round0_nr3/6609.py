#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

string intToString(double value) {
    stringstream ss;
    ss << value;
    return ss.str();
}

void getLimits(ifstream &isr, int &limA, int &limB) {
    isr >> limA;
    isr >> limB;
}

bool isPalindrome(string str_p) {
    string str_p_rev;
    str_p_rev.resize(str_p.size());
    reverse_copy(str_p.begin(), str_p.end(), str_p_rev.begin());

    for(int i=0; i<str_p.size()/2; ++i) {
        if(str_p[i] != str_p_rev[i])
            return false;
    }
    return true;
}

int main() {
    ifstream is("small.in");
    ofstream os("output.in");

    int caseNumber;
    is >> caseNumber;

    int currentCaseNumber = 1;
    int a, b;

    while(is.good() && currentCaseNumber <= caseNumber) {
        getLimits(is, a, b);
        int palindromeNumber = 0;

        while(a <= b) {
            string str_a = intToString(a);
            bool palindrome = true;
            bool palindromeSqrt = false;

            palindrome = isPalindrome(str_a);

            if(palindrome) {
                double sqrt_a = sqrt(a);
                int sqrt_a_int = sqrt_a;
                if(sqrt_a == sqrt_a_int) {
                    string str_sqrt_a = intToString(sqrt_a);
                    palindromeSqrt = isPalindrome(str_sqrt_a);
                }
            }

            if(palindrome && palindromeSqrt)
                palindromeNumber++;

            a++;
        }

        os << "Case #" << currentCaseNumber << ": " << palindromeNumber << endl;
        currentCaseNumber++;
    }

    is.close();
    os.close();
}
