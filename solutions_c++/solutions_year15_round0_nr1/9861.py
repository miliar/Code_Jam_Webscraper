#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    ifstream input_file;
    input_file.open(argv[1]);
    string current_line;

    vector<string> test_cases;

    while (getline(input_file, current_line))
    {
        test_cases.push_back(current_line);
    }

    for (int t = 1; t < test_cases.size(); ++t)
    {
        int s_max = test_cases[t][0] - '0';

        int current_p = 0;
        int friends = 0;
        int current_s = 0;

        //cout<<"Test case: "<<test_cases[t]<<endl;

        for (int s_i = 2; s_i <= s_max+2; ++s_i, ++current_s)
        {
            //cout<<"\tCP: "<<current_p<<" CS: "<<current_s<<" F: "<<friends<<endl;
            if (current_p >= current_s)
            {
                current_p += test_cases[t][s_i] - '0';
            }
            else if (current_p < current_s)
            {
                friends += (current_s - current_p);
                current_p += test_cases[t][s_i] - '0' + (current_s - current_p);
            }
        }

        cout<<"Case #"<<t<<": "<<friends<<endl;

        //cout<<" "<<"Answer: "<<friends;

        //cout<<endl;
    }

    input_file.close();
}
