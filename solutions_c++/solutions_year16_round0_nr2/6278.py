#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream file_reader("large_input.in");
    ofstream file_writer("large_answer.txt");

    int t;
    file_reader >> t;

    for (int c = 1; c<=t; ++c)
    {
        string s;
        file_reader >> s;

        int moves = 0;
        char initial = s[0];
        for (int i = 1; i<s.size(); ++i)
        {
            if(s[i]!=initial)
            {
                ++moves;
                initial = s[i];
            }
        }
        if(s[s.size()-1]=='-')
            ++moves;

        file_writer << "Case #" << c << ": " << moves << endl;
    }
}
