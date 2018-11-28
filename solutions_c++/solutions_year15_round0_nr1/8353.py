#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int solve(string shyness, int shyest)
{
    int friends = 0, stood = 0;
    for(int i=0; i<shyest; i++)
    {
        while(stood < i)
        {
            friends++;
            stood++;
        }
        stood += shyness[i] - '0';
    }
    return friends;
}

int main(int argc, char *argv[])
{
    ifstream file_input("A-large.in", ios::in);
    ofstream file_output("A-large(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        int games, test=1, shyest;
        string shyness;
        file_input >> games;
        while(test<=games)
        {
            file_input >> shyest >> shyness;

            file_output << "Case #" << test << ": " << solve(shyness, shyest+1) << "\n";

            test++;
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file !" << endl;
    return 0;
}
