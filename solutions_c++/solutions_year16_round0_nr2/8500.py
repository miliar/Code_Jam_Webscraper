#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int solve(string pancakes)
{
    int nb_flip = 0, last_blank = 0;

    while(pancakes.find('-') != string::npos)
    {
        last_blank = pancakes.find_last_of('-');
        for(unsigned int i = 0; i <= last_blank; i++)
        {
            if(pancakes[i] == '-') pancakes.replace(i, 1, "+");
            else pancakes.replace(i, 1, "-");
        }
        nb_flip++;
    }

    return nb_flip;
}

int main(int argc, char *argv[])
{
    ifstream file_input("B-large.in", ios::in);
    ofstream file_output("B-large(answer).in", ios::trunc | ios::out);

    if(!file_input || !file_output)
    {
        cerr << "Error : Cannot open the files !" << endl;
        return -1;
    }

    int cases, test=1;
    string pancakes;
    file_input >> cases;

    while(test <= cases)
    {
        file_input >> pancakes;
        file_output << "Case #" << test << ": " << solve(pancakes) << "\n";
        test++;
    }

    file_input.close();
    file_output.close();

    return 0;
}
