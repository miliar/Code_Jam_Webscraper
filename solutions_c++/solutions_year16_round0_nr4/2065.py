#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;

ll power(int a, int b)
{
    if (b == 0)
        return 1;

    ll ret = a;
    for (int i = 1; i < b; i++)
        ret *= a;

    return ret;
}

int main()
{
    ifstream fin("in.in");
    ofstream fout("out.out");

    int times;
    fin >> times;
    for (int i = 1; i <= times; i++)
    {
        int length, complexity, to_pick;
        fin >> length >> complexity >> to_pick;

        fout << "Case #" << i << ": ";

        //calculate minimum needed (round up)
        int min = length / complexity;
        if (length % complexity != 0) min ++;

        if (to_pick < min)
            fout << "IMPOSSIBLE" << endl;
        else
        {
            //magical for loop prints positions
            bool first = true;
            for (int i = 0; i < length;)
            {
                ll pos = 0;
                for (int j = complexity - 1; j >= 0; j--)
                {
                    pos += i * power(length, j);
                    i++;
                    if (i == length) break;
                }

                if (first) first = false;
                else fout << " ";

                fout << pos + 1;
            }
            fout << endl;
        }
    }

    cin.get();

    fout.close();
    fin.close();
}