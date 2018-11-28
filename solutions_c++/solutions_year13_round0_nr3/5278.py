#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <sstream>

using namespace std;

bool isFairNSquare(int num);
bool isPalindrome(string text);
void generate(int min, int max, vector<int>& storage);
string toStr(int number);
void splitStr(int& a, int& b, string s);

int main(int argc, char* argv[])
{
    ifstream inputFile(argv[1]);

    string line, low, high;

    getline(inputFile, line);

    int numCases = atoi(line.c_str());

    int cCase = 0;

    while (cCase < numCases) {
        getline(inputFile, line);
        int low, high;
       
        splitStr(low, high, line); 

        vector<int> numsToCheck;
        generate(low, high, numsToCheck);        
       
        int numFnS = 0;
        
        for (vector<int>::iterator i = numsToCheck.begin(); i != numsToCheck.end(); ++i) {
            if (isFairNSquare(*i))
               ++numFnS;
        }

        cout << "Case #" << cCase+1 << ": " << numFnS << endl;
        ++cCase;
    }

    return 0;
}

bool isFairNSquare(int num)
{
    if (isPalindrome(toStr(num))) {
        double d_sqrt = sqrt(num);
        int i_sqrt = d_sqrt;

        if (d_sqrt == i_sqrt) {
            return isPalindrome(toStr(i_sqrt));
        }
    }

    return false;
}

bool isPalindrome(string text)
{
    int left  = 0;                      // Indexes of the leftmost and
    int right = text.length() - 1;      // rightmost unchecked character.

    // Check palindrome by moving left and right boundaries progressively
    // closer until they finally meet or pass each other.  Bail early if
    // we find a mismatch.
    while (left < right) {
        if (text[left] != text[right])
            return false;

        ++left;
        --right;
    }

    // All the characters checked out.
    return true;
}

void generate(int min, int max, vector<int>& storage)
{
    for ( ; min <= max; ++min) {
        storage.push_back(min);
    }
}

string toStr(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

void splitStr(int& a, int& b, string s)
{
    string aa, bb;
    bool next = false;

    for (size_t i = 0; i < s.length(); ++i) {
        if (s.at(i) == ' ') {
            next = true;  
        }
        if (next) {
            bb.push_back(s.at(i));
        }
        else {
            aa.push_back(s.at(i));
        }
    }

    istringstream(aa) >> a;
    istringstream(bb) >> b;
}
