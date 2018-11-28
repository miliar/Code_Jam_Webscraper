#include <iostream>
#include <fstream>

using namespace std;


std::ifstream fin("input.in");
std::ofstream fout("output.out");


int main()
{
    int t, i, j;
    long long n, pl;
    int a [150];
    int b [10];

    fin >> t;
    for (i=0; i<t; i++)
    {
        for (j=0; j<10; j++) b[j] = false;
        fin >> n;
        pl = n;
        if (n==0) fout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        if (n!=0)
        {
            while (2>1) {
            long long n1 = n;
                        while (2>1)
                        {
                            int k = n1 % 10;
                            b[k] = true;
                            n1 = n1 / 10;
                            if (n1==0) break;
                        }
            bool ans = true;
            for (j=0; j<10; j++) ans = ans & b[j];
            if (ans==true)
            {
                fout << "Case #" << i + 1 << ": " << n << endl;
                break;
            }
            else
            {
                n += pl;
            }
                }
        }
    }

    return 0;
}
