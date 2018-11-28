#include <fstream>
#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
ifstream f("A-small-attempt2.in");
ofstream g("sol.out");

int t, n;
string string1, string2;

int main()
{
    f >> t;
    for (int i = 1; i <= t; i ++)
    {
        g << "Case #"<< i << ": ";
        f >> n;
        f >> string1;
        f >> string2;
        string local1 = "";
        string local2 = "";
        local1 += string1[0];
        for (int j = 1; j < string1.size(); j ++)
            if (string1[j] != string1[j - 1])
                local1 += string1[j];
        local2 += string2[0];
        for (int j = 1; j < string2.size(); j ++)
            if (string2[j] != string2[j - 1])
                local2 += string2[j];
        if (local1 != local2)
            g << "Fegla Won" << endl;
        else
        {
            int indice1 = 0;
            int indice2 = 0;
            int numar = 0;
            while (indice1 < string1.size() || indice2 < string2.size())
            {
                if (string1[indice1] == string2[indice2])
                {
                    indice1 ++;
                    indice2 ++;
                }
                else
                {
                    if (string1[indice1 - 1] == string1[indice1])
                    {
                        while (string1[indice1] != string2[indice2])
                        {
                            indice1 ++;
                            numar ++;
                        }
                    }
                    else
                    {
                        while (string1[indice1] != string2[indice2])
                        {
                            indice2 ++;
                            numar ++;
                        }
                    }
                }
            }
            g << numar << endl;
        }
    }
    return 0;
}
