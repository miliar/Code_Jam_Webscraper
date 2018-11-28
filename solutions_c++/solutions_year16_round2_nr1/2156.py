#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
    ifstream fi ("A-large.in");
    ofstream fo ("output_large.txt");
    string s;
    int t;
    fi >> t;
    getline (fi,s);
    for (int o = 1; o <= t; ++o)
    {
        getline (fi,s);
        int a[26] = {0};
        char c;
        for (int i = 0; i < s.length(); ++i)
        {
            a[s[i] - 'A'] += 1;
        }
        fo << "Case #" << o << ": ";
        int x = a[25];
        while (x--) fo << "0";
        x = a[14] - a[25] - a[22] - a[20];
        int k = x;
        while (x--) fo << "1";
        x = a[22];
        while (x--) fo << "2";
        x = a[19] - a[22] - a[6];
        while (x--) fo << "3";
        x = a[20];
        while (x--) fo << "4";
        x = a[5] - a[20];
        while (x--) fo << "5";
        x = a[23];
        while (x--) fo << "6";
        x = a[18] - a[23];
        while (x--) fo << "7";
        x = a[6];
        while (x--) fo << "8";
        x = (a[13] - a[18] + a[23] - k)/2;
        while (x--) fo << "9";
        fo << endl;

    }
}
