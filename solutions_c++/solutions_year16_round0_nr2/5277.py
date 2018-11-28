#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int T;

int main()
{
    ifstream in("B-large.in");
    in >> T;

    ofstream out("B-large.out");

    for (int t = 0; t < T; ++t)
    {
        string str;
        in >> str;

        int cnt = 0;
        for (int i = 0; i < str.length() - 1; ++i)
        {
            if (str[i + 1] != str[i]) cnt++;
        }
        if (str.back() == '-') cnt++;

        out << "Case #" << t + 1 << ": " << cnt << endl;
    }

    in.close();
    out.close();

    return 0;
}