#include <iostream>
#include <fstream>
#include <string>
#include <deque>

using namespace std;

int T;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    in >> T;

    for (int t = 0; t < T; ++t)
    {
        string str;
        in >> str;

        deque<char> r;

        r.push_back(str[0]);
        for (int i = 1; i < str.length(); ++i)
        {
            if (str[i] < r.front()) r.push_back(str[i]);
            else r.push_front(str[i]);
        }

        out << "Case #" << t + 1 << ": ";
        for (int i = 0; i < r.size(); ++i) out << r[i];
        out << endl;
    }

    in.close();
    out.close();
}