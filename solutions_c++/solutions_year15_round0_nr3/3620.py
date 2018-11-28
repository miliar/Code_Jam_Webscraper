#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

std::map<string, string> multTable;

string multiply(string s, char c)
{
    string ret = "";
    if ( s[0] == '-' )
    {
        ret = multTable[string(1,s[1])+string(1,c)];
        if ( ret[0] == '-' )
        {
            ret = string(1,ret[1]);
        } else {
            ret = "-" + ret;
        }
    } else {
        ret = multTable[s+c];
    }

    return ret;
}

int main()
{
    multTable["11"] = "1"; multTable["1i"] = "i"; multTable["1j"] = "j"; multTable["1k"] = "k";
    multTable["i1"] = "i"; multTable["ii"] = "-1"; multTable["ij"] = "k"; multTable["ik"] = "-j";
    multTable["j1"] = "j"; multTable["ji"] = "-k"; multTable["jj"] = "-1"; multTable["jk"] = "i";
    multTable["k1"] = "k"; multTable["ki"] = "j"; multTable["kj"] = "-i"; multTable["kk"] = "-1";

    ifstream in("C-small-attempt0.in");
    //ifstream in("large-practice.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";

        int L,X;
        in >> L >> X;

        string str;
        in >> str;

        string currentValue = "1";
        string ijk = "";

        for (int i = 0; i < L * X; i++)
        {
            currentValue = multiply(currentValue, str[i%L]);
            if (currentValue == "i" && ijk == "")
            {
                ijk = "i";
                currentValue = "1";
            }
            else if (currentValue == "j" && ijk == "i")
            {
                ijk = "ij";
                currentValue = "1";
            }
        }

        if (currentValue == "k" && ijk == "ij")
        {
            out << "YES";
        } else {
            out << "NO";
        }
        out << endl;
    }

    return 0;
}
