#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(string str)
{
    bool last_minus = str.back() == '-';

    int diff = 0;
    for (int i = 1; i < str.size(); ++i)
    {
        if (str[i] != str[i - 1])
            diff++;
    }
    if (str.back() == '-')
        diff++;
    return diff;
}

int main()
{
    string input_file = "B-large.in";
    ifstream in(input_file);
    ofstream out("output.txt");

    int T;

    in >> T;

    for (int i = 1; i <= T; ++i)
    {
        string N;
        in >> N;

        out << "Case #" << i << ": " << solve(N) << endl;
    }

    return 0;
}