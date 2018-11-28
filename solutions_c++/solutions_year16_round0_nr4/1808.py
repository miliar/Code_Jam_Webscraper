#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream in;
    in.open("D.in");
    ofstream out;
    out.open("D.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i)
    {
        int k, c, s;
        in >> k >> c >> s;
        out << "Case #" << i + 1 << ": ";
        if (k == s)
        {
            for (int j = 1; j <= s; ++j)
            {
                out << j << " ";
            }
        }
        out << endl;
    }
    out.close();
    in.close();
    return 0;
}
