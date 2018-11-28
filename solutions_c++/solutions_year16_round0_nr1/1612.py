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
    bool seen[10];

    input_file >> nb_test_cases;

    for(int _i = 0 ; _i < nb_test_cases ; ++_i)
    {
        long long n;
        long long cur = 0;

        input_file >> n;

        if(n == 0)
        {
            cout << "Case #" << _i + 1 << ": INSOMNIA" << endl;
            continue;
        }

        for(int i = 0 ; i < 10 ; ++i)
            seen[i] = false;
        int nb_seen = 0;

        while(nb_seen < 10)
        {
            cur += n;
            //cout << cur << endl;
            long long pow = 1;
            while(cur / pow > 0)
            {
                int digit = (cur / pow) % 10;
                if(!seen[digit])
                {
                    //cout << "New digit seen: " << digit << endl;
                    seen[digit] = true;
                    ++nb_seen;
                }
                pow *= 10;
                //cout << "Stop? " << cur/pow << endl;
            }
        }

        cout << "Case #" << _i + 1 << ": " << cur << endl;
    }

    return 0;
}
