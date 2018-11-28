#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string solve(string puzzle)
{
    string phone_number;

    char numbers[10] = { '0', '2', '4', '1', '3', '5', '6', '7', '8', '9' };
    char digits[10] = { 'Z', 'W', 'U', 'O', 'R', 'F', 'X', 'S', 'G', 'N' };
    string full_digits[10] = { "ZERO", "TWO", "FOUR", "ONE", "THREE", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

    for(unsigned int i = 0; i < 10; i++)
    {
        while(puzzle.find(digits[i]) != string::npos)
        {
            if(i == 3 && phone_number.find('2') != string::npos) phone_number.insert(phone_number.find('2'), 1, numbers[i]);
            else if(i == 3 && phone_number.find('4') != string::npos) phone_number.insert(phone_number.find('4'), 1, numbers[i]);
            else if(i == 4 && phone_number.find('4') != string::npos) phone_number.insert(phone_number.find('4'), 1, numbers[i]);
            else phone_number.append(1, numbers[i]);
            for(unsigned int j = 0; j < full_digits[i].length(); j++)
            {
                puzzle.erase(puzzle.find(full_digits[i][j]), 1);
            }
        }
    }

    return phone_number;
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

    int cases, test = 1;
    string puzzle;
    file_input >> cases;

    while(test <= cases)
    {
        file_input >> puzzle;
        file_output << "Case #" << test << ": " << solve(puzzle) << "\n";
        test++;
    }

    file_input.close();
    file_output.close();

    return 0;
}
