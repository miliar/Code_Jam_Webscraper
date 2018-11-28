#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>
#include <unistd.h>

using namespace std;

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases+1; ++c)
    {
        string s;
        is >> s;
        //cout << s << endl;

        int n = 0;

        for (size_t pm = s.find('-'); pm != std::string::npos; pm = s.find('-'), ++n)
        {
            //usleep(100000);
            if (s[0] == '+')
            {
                if (pm == string::npos) pm = s.size();
                for (size_t p = 0; p != pm; ++p) {
                    s[p] = '-';
                }
            } else {
                size_t plm = s.find_last_of('-');
                string ss = s;
                //cout << plm << endl;
                for (size_t p = 0; p != plm+1; ++p)
                    if (ss[p] == '+') s[plm-p] = '-';
                    else s[plm-p] = '+';
            }
            //cout << s << endl;
        } 

        cout << "Case #" << c << ": " << n << endl;
    }
}

