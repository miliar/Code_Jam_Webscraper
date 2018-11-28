#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int k;

    fin >> k;

    char str[256];
    for (auto i = 0; i < k; i++)
    {
        unsigned int Norig;
        unsigned int N;
        unsigned int counter = 2;
        unsigned int num = 0; // 1111111111 = 1023
        fin >> N;
        Norig = N;

        if (N == 0)
        {
            fout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }

        int failcount = 0;
        while (1)
        {
            bool found = false;

            while (N != 0 )
            {
                int shift = N % 10;
                N = N / 10;

                if (!(num & (1 << shift) ))
                {
                    num = num | (1 << shift);
                    found = true;
                }
            }

            if (num == 1023)
                break;

            N = Norig * counter;
            counter ++;
        }
        fout << "Case #" << i+1 << ": " << Norig * (counter-1) << endl;
        //cout << Norig << " " << N << " " << counter << endl;

    }


    return 0;
}