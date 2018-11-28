#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cctype>
#include <math.h>

using namespace std;

typedef unsigned long long ull;
//typedef long double ull;

inline string convert(const ull& i)
{
    ostringstream conv;
    conv << i;
    return conv.str();
}

inline bool is_palin(const ull& i)
{
    string s = convert(i);
    return equal(s.begin(), s.end(), s.rbegin());
}

int main()
{
    ifstream infile("C-small-attempt0.in");
    ofstream outfile("out.txt");
    int i;
    string line;
    getline(infile, line);
    istringstream str(line);
    str >> i;
    //cout << i << endl;
    for (int j = 0; j < i; ++j) {
        getline(infile, line);
        istringstream str2(line);
        ull a, b;
        str2 >> a >> b;
        //cout << "A: " << a << " B: " << b << endl;
        ull count = 0;
        ull beg = sqrt(a);
        //cout << "beg: " << beg << endl;
        ull sq = beg*beg;
        while (1) {
            if (is_palin(beg)) {
                sq = beg*beg;
                if (sq > b) break;
                if (is_palin(sq) && sq >= a)
                    ++count;
                ++beg;
                continue;
            }
            ++beg;
        }
        outfile << "Case #" << j+1 << ": " << count << endl;
    } 
    return 0;
}