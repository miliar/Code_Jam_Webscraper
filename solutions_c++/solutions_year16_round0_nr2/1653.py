#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void get_line(ifstream& input_file, string& line)
{
    char c;

    input_file >> line; // First word
    string word;

    while(input_file.get(c) && c != '\n')
    {
        input_file >> word;
        line += " " + word;
    }
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        cout << "[ERROR] No input file given!" << endl;
        return 1;
    }

    ifstream input_file;
    input_file.open(argv[1]);

    if(!input_file.is_open())
    {
        cout << "[ERROR] Could not open file " << argv[1] << "!" << endl;
        return 2;
    }

    int nb_test_cases;

    input_file >> nb_test_cases;

    for(int _i = 0 ; _i < nb_test_cases ; ++_i)
    {
        string pancakes;
        input_file >> pancakes;

        int nb_ops = 0;
        for(int i = 1 ; i < pancakes.size() ; ++i)
            if(pancakes[i] != pancakes[i - 1])
                ++nb_ops;
        if(pancakes[pancakes.size() - 1] == '-')
            ++nb_ops;

        cout << "Case #" << _i + 1 << ": " << nb_ops << endl;
    }

    return 0;
}
