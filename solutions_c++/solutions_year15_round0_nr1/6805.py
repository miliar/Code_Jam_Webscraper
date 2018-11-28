#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin ("A.txt");
    ofstream fout ("Ao.txt");
    int T, Smax;
    fin >> T;
    for(int i = 0; i < T; i++)
    {
        string str;
        fin >> Smax >> str;
        for(int j = 0; j <= Smax; j++)
            str[j] -= '0';
        int sum = 0;
        int to_add = 0;

        for(int j = 0; j <= Smax; j++)
        {
            if(str[j] > 0 && sum <= j)
                to_add = max(to_add, j - sum);
            sum += str[j];
        }
        fout << "Case #" << i+1 << ": " << to_add << "\n";
    }
    return 0;
}
