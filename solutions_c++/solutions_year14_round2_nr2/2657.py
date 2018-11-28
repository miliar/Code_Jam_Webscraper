#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream fin, fout;
    long long int T, A, B, K, i, x, y, c=0;
    fin.open("B-small-attempt0.in");
    fout.open("c1.txt");
    fin >> T;
    for (i = 0; i < T; i++)
    {
        c=0;
        fin >> A >> B >> K;
        for (x = 0; x < A; x++)
            for (y = 0; y < B; y++)
            {
                if ((x & y) <K) c++;
            }
        fout << "Case #"<< i+1 <<": " << c << endl;
    }
    fout.close();
    return 0;
    }
