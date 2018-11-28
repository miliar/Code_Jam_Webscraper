#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

string s;
int k;

void flap(int p)
{
    for(int i = 0; i < k; ++i)
    {
        if(s[p+i] == '-')
        {
            s[p+i] = '+';
        }else
        {
            s[p+i] = '-';
        }
    }
}

int main()
{
    string file_name = "A-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        f1 >> s >> k;
        int counter = 0;
        for(int i = 0; i <= s.size() - k; ++i)
        {
            if(s[i] == '-')
            {
                flap(i);
                ++counter;
            }
        }
        bool impossible = 0;
        for(int i = s.size() - k + 1; i < s.size(); ++i)
        {
            if(s[i] == '-')
            {
                impossible = 1;
            }
        }
        if(impossible)
        {
            f2 << "IMPOSSIBLE" << endl;
        }else
        {
            f2 << counter << endl;
        }
    }
    return 0;
}

