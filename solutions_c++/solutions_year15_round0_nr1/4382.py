#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>


using namespace std;

struct p1 {
   long long type;
   long long count;
};

int main()
{
    int T;

    //ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\input.txt");
    ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\A-large.in");
    ofstream fout("output.txt");

    fin >> T;
    int res = 0;
    long long total = 0;


    for (int i = 0; i < T; i++)
    {
        int smax = 0;
        fin >> smax;
        string s;
        fin >> s;

        int totalInvite = 0;
        int curStanding = 0;
        for (int j = 0; j <= smax; j++)
        {
            int cur = s[j] - '0';
            if (cur == 0) continue;

            if (curStanding >= j)
            {
                curStanding += cur;
            }
            else {
                int newInvite = j - curStanding;
                totalInvite += newInvite;
                curStanding += newInvite + cur;
            }
        }

        fout << "Case #" << i + 1 << ": " << totalInvite << endl;

    }
    return 0;
}