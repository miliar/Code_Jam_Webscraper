#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include <cmath>

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
        cout << "Case #" << _i + 1 << ":";
        int K, C, S;
        input_file >> K >> C >> S;
        if(K < C)
            C = K;

        if(ceil(K / C) > S)
            cout << " IMPOSSIBLE" << endl;
        else if(K <= S)
        {
            for(int i = 0 ; i < K ; ++i)
                cout << " " << i + 1;
            cout << endl;
        }
        else
        {
            for(int i = 0 ; i < K / C ; ++i)
            {
                long long offset_c = (long long)(C) * (i + 1);
                long long offset_k = (long long)(K) * C * i;
                cout << " " << (offset_c + offset_k);
            }
            cout << endl;
        }
    }

    return 0;
}
