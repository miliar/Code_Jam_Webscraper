#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int find_max1(int p[], int &f, int n)
{
    int x = 0, index = 0;
    for (int i = 0; i < n; ++i)
    {
        if (x < p[i])
        {
            index = i;
            x = p[i];
        }
    }
    p[index]--;
    if (p[index] == 0) f += 1;
    return index;
}

int find_max2(int p[], int &f, int n)
{
    int x = 0, index = 0;
    if (n == 2)
    {
        if (p[0] == p[1]) return -1;
    }
    for (int i = 0; i < n; ++i)
    {
        if (x < p[i])
        {
            index = i;
            x = p[i];
        }
    }
    p[index]--;
    if (p[index] == 0) f += 1;
    if ((f < n - 1) || (f == n)) return index;
    f -= 1; p[index]++;
    return -1;
}


int main()
{
    ifstream fin ("A-large.in");
    ofstream fout ("output_large.txt");
    string s;
    int t;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        fout << "Case #" << o << ": ";
        int p[26] = {0}, f = 0, n;
        fin >> n;
        for (int i = 0; i < n; ++i) fin >> p[i];
        int i = 0;
        while (f != n)
        {
            fout << (char) ('A' + (char) find_max1(p, f, n));
            int var = find_max2(p, f, n);
            if (var != -1) fout << (char) ('A' + (char) var);
            fout << " ";
        }
        fout << endl;
    }
}
