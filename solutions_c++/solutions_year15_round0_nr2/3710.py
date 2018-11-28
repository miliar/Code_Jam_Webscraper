#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>

using namespace std;

const int MAX_CASE = 101;
const int MAX_D = 1001;
const int MAX_PANCAKE = 1001;
int main()
{
    int T;
    int man[MAX_CASE];
    int pcake[MAX_CASE][MAX_D];
    int keymax[MAX_CASE];
//    int seq_int[MAX_S];

    fstream o;
    o.open("D:\\MyProject\\QtCPP\\GCJ2015\\0411B\\b.in", ios::in);
    o>>T;

    for (int i=0;i < T;i++)
    {

        o>>man[i];
        int n = man[i];
        for (int j=0;j < n;j++)
        {
            o>>pcake[i][j];
            keymax[i] = max(keymax[i], pcake[i][j]);
        }
    }
    o.close();

    fstream f("D:\\MyProject\\QtCPP\\GCJ2015\\0411B\\b.out", ios::out);

    for (int i=0;i < T;i++)
    {

        int keymin = keymax[i];
        int acc = 0;
        for (int j=1;j <= keymax[i];j++)
        {
            acc = j;
            for (int d=0;d < man[i];d++)
            {
                int p = pcake[i][d];
                if (p > j)
                {
                    if (p % j == 0)
                        acc += (p / j) - 1;
                    else
                        acc += p / j;
                }
            }
            keymin = min(keymin, acc);
        }
        f<<"Case #"<<i+1<<": "<<keymin<<endl;
    }
    f.close();
    return 0;
}
