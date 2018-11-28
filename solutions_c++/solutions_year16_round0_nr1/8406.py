#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

bool Solved(bool *digits, int i)
{
    if(digits[i] == false) return false;
    if(i<9) return Solved(digits, i+1);
    return true;
}

bool Solved(bool *digits)
{
    return Solved(digits, 0);
}

string IntToString(int number)
{
    ostringstream oss;
    oss << number;
    return oss.str();
}

string solve(int start)
{
    if(start == 0) return "INSOMNIA";

    unsigned int i, n;
    bool solved = false;
    string number;

    bool digits[10] = {false};

    for(n = 1; n < 100; n++)
    {
        number = IntToString(start * n);
        //cout << "n = " << n << " ; length = " << number.length() << " ; number = " << number << endl;

        for(i = 0; i < number.length(); i++)
        {
            digits[number[i]-'0'] = true;
        }

        if(solved = Solved(digits)) break;
    }

    if(solved) return number;
    return "INSOMNIA";
}

int main(int argc, char *argv[])
{
    ifstream file_input("A-large.in", ios::in);
    ofstream file_output("A-large(answer).in", ios::trunc | ios::out);

    if(!file_input || !file_output)
    {
        cerr << "Error : Cannot open the files !" << endl;
        return -1;
    }

    int cases, test=1, start;
    file_input >> cases;

    while(test <= cases)
    {
        file_input >> start;
        file_output << "Case #" << test << ": " << solve(start) << "\n";
        test++;
    }

    file_input.close();
    file_output.close();

    return 0;
}
