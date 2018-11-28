#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>
#include <math.h>
#include <sstream>

using namespace std;

int check(string str)
{
    string::iterator it = str.begin();
    string::reverse_iterator rit = str.rbegin();
    int len = str.length();
    for (int i = 0; i < len / 2; i++, it++, rit++)
    {
        if (*it != *rit)
        {
            return 0;
        }
    }

    return 1;
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;

    for (int tc = 0; tc < T; tc++)
    {
        int A, B;
        fin >> A >> B;
        int ret = 0;

        int sa = (int)sqrt((double)A);
        if (A > sa * sa)
        {
            sa++;
        }
        int sb = (int)sqrt((double)B);
        for (int b = sa; b <= sb; b++)
        {
            stringstream ss;
            ss << b;
            if (check(ss.str()) == 1)
            {
                stringstream ss2;
                ss2 << b * b;
                ret += check(ss2.str());
                //if (check(ss2.str()))
                //{
                //    cout << ss2.str() << endl;
                //}
            }
        }

        fout << "Case #" << tc+1 << ": " << ret << endl;
    }

    return (0);
}
