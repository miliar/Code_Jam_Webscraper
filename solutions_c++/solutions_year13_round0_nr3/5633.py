#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

bool isPalindrome(int);
string itos(int);

int main() 
{
    int numTests; 
    cin >> numTests;

    for (int i = 0; i < numTests; i++) 
    {
        int low, high;
        cin >> low >> high;
        float top = sqrt(1000);

        int found = 0;
        for (int j = 1; j <= top; j++)
        {
            int squared = j * j;
            if (isPalindrome(j) && isPalindrome(squared)) {
                if (squared >= low && squared <= high) {
                    found++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << found << '\n';
    }

    return 0;
}

string itos(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

bool isPalindrome(int number)
{
    string str = itos(number);
    int length = str.length() / 2;

    string::iterator it = str.begin();
    string::reverse_iterator rit = str.rbegin();
    int i = 0;

    bool match = true;
    for (; i < length; ++i, ++it, ++rit)
    {
        if (*it != *rit) 
        {
            match = false;
            break;
        }
    }


    return match;
}   

