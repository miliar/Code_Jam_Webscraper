#include <fstream>
#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

vector<string> ReadTask(istream& in)
{
    size_t count;
    in >> count;
    vector<string> words;
    while (count-- > 0)
    {
        string w;
        in >> w;
        words.push_back(w);
    }
    return words;
}

void DoTask(string w, ostream& os)
{
    static size_t caseCount = 0;
    os << "Case #" << ++caseCount << ": ";

    string last;
    for (char c : w)
    {
        if (last.empty())
        {
            last += c;
            continue;
        }
        if (c >= last.front())
        {
            last = c + last;
        }
        else
        {
            last += c;
        }
    }
    os << last << std::endl;
}

int main()
{
    vector<string> words = ReadTask(ifstream("input.txt"));
    ofstream ofs("output.txt", std::ios::trunc);
    for (string w : words)
    {
        DoTask(w, ofs);
    }
    return 0;
}
