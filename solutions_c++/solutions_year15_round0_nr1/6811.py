#include <iostream>
#include <fstream>
using namespace std;

#define S_MAX 1007

int S;
int aud[S_MAX];

int main()
{
    ifstream fin("ovation_large.in"); // make sure to change to small or large.
    ofstream fout("ovation_large.out");
    int T;
    fin >> T;
    for (int t = 0; t < T; t++)
    {
        fin >> S;
        for (int i = 0; i < S + 1; i++)
        {
            char c;
            fin >> c;
            aud[i] = c - '0';
        }

        int standing = aud[0];
        int friends = 0;
        for (int i = 1; i < S + 1; i++)
        {
            if (standing >= i)
            {
                standing += aud[i];
            }
            else
            {
                friends += i - standing; // add minimum # of necessary friends
                standing += aud[i] + i - standing; // add friends who just joined and those with shyness i;
            }
        }
        fout << "Case #" << t + 1 << ": " << friends << '\n';
    }
    return 0;
}
