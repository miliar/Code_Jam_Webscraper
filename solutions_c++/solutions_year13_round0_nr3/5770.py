#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

int DEBUG = 0;
int count = 0;

void readInput(string);
string itos(double);
bool checkPalindrome(string str);

int main(int argc, char* argv[])
{
    string filename = argv[1];

    readInput(filename);
    return 0;
}

void readInput(string filename)
{
    int cases = 0;
    double lower,
           upper;
    string str;
    bool original = false,
         square = false;

    ifstream myIn;
    myIn.open(filename.c_str());

    myIn >> cases;
    for (int i = 0; i < cases; i++)
    {
        myIn >> lower >> upper;
        
        for (int x = lower; x <= upper; x++)
        {
            str = itos(x);
            original = checkPalindrome(str);
            str = itos(sqrt(x));
            square = checkPalindrome(str);
            if (original && square)
                count++;
            original = false;
            square = false;
        }
        
        cout << "Case #" << i+1 << ": " << count << endl;
        count = 0;
    }

    myIn.close();
}

string itos(double a)
{
    stringstream ss;
    ss << a;
    string str = ss.str();
    return str;
}

bool checkPalindrome(string str)
{
    bool pali = false;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] != str[str.length()-i-1])
            return false;
    }
    if (DEBUG) cout << str << endl;
    return true;
}
