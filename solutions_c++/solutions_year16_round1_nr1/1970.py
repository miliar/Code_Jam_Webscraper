#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
    ifstream fi ("A-large.in");
    ofstream fo ("output_large.txt");
    int t;
    fi >> t;
    char s[1001], s2[1001];
    for (int o = 1; o <= t; ++o)
    {
        fi >> s;
        int i;
        s2[0] = s[0];
        for (i = 1; s[i] != '\0' ; ++i)
        {
            if (s2[0] > s[i]) s2[i] = s[i];
            else
            {
                for (int j = i - 1; j >= 0; --j) s2[j + 1] = s2[j];
                s2[0] = s[i];
            }
        }
        s2[i] = '\0';
        fo << "Case #" << o << ": " << s2 << endl;
    }
}
