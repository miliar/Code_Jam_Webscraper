#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("output2.txt");
    int t, o;
    fin >> t;
    for (o = 1; o <= t; o++)
    {
        int n;
        fin >> n;
        int i, drop = 0, a[1000];
        long long int y = 0, z = 0;
        for (i = 0; i < n; ++i) fin >> a[i];
        for (i = 1; i < n; ++i)
        {
            if (a[i-1] - a[i] > drop) drop = a[i-1] - a[i];
        }
        for (i = 1; i < n; ++i)
        {
            if (a[i-1] - a[i] > 0) y += a[i-1] - a[i];
        }
        for (i = 0; i < n-1; ++i)
        {
            if (a[i] >= drop) z+= drop;
            else z+= a[i];
        }
        fout << "Case #" << o << ": " << y << " " << z << endl;
    }
}
