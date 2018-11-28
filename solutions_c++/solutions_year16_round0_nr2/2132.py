#include <iostream>
#include <string>
#include <fstream>
#include <set>

using namespace std;

typedef long long ll;

int main()
{
    ifstream fin("in.in");
    ofstream fout("out.out");

    int times;
    fin >> times;
    for (int i = 1; i <= times; i++)
    {
        int times_flipped = 0;
        char curr = '+';
        string str;
        fin >> str;

        for (int i = str.length() - 1; i >= 0; i--)
        {
            if (str.at(i) != curr)
            {
                times_flipped++;
                curr = str.at(i);
            }
        }
        fout << "Case #" << i << ": " << times_flipped << endl;
    }

    cin.get();

    fout.close();
    fin.close();
}