#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream in("mote.in");
    ofstream out("mote.out");

    int times = 0;
    in >> times;
    for (int num = 0;num < times;num++)
    {
        int me = 0;
        in >> me;
        int all = 0;
        in >> all;
        vector<int> vec1;
        for (int i = 0;i < all;i++) { int temp = 0; in >> temp; vec1.push_back(temp); }
        sort(vec1.begin(),vec1.end());
        int minP = all;

        if (me == 1)
        {
            out << "Case #" << num + 1 << ": " << all << '\n';
            continue;
        }

        for (int i = 0;i <= all;i++)
        {
            int t = 0;
            int current = me;
            for (int j = 0;j < i;j++)
            {
                if (current > vec1[j]) { current += vec1[j]; }
                else
                {
                    int p = 0;
                    int m = 0;
                    m = (vec1[j] + 1 - current) / (current - 1);
                    if ((vec1[j] + 1 - current) % (current - 1)) { m++; }
                    m += 1;
                    int flag = 0;
                    while (m != 1) { if (m % 2) flag = 1; m /= 2; p++; }
                    if (flag) p++;

                    int mult = 1;
                    for (int k = 0;k < p;k++) { mult *= 2; }
                    mult--;
                    current += mult * (current - 1);
                    current += vec1[j];
                    t += p;
                }
            }
            t += all - i;
            if (t < minP) minP = t;
        }

        out << "Case #" << num + 1 << ": " << minP << '\n';
    }
    return 0;
}
