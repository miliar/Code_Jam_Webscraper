#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

int N;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> N;
    for (int i = 0; i < N; ++ i)
    {
        int x;
        fin >> x;
        if (x == 0)
        {
            fout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        bool flg[10] = {};
        int y = 0;
        bool sleep = false;
        int k = 0;
        while (!sleep)
        {
            k ++;
            y = k * x;
            while (y > 0)
            {
                flg[y % 10] = 1;
                y /= 10;
            }
            sleep = true;
            for (int j = 0; j < 10; ++ j)
            {
                if (!flg[j])
                {
                    sleep = false;
                    break;
                }
            }
        }
        fout << "Case #" << i + 1 << ": ";
        fout << x * k << endl;
    }
    return 0;
}

