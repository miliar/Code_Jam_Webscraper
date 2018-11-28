#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
const int MAXN = 1100;

ifstream fin ("B.in");
ofstream fout ("B.out");

int N, K;
int dlo[MAXN], dhi[MAXN], dcur[MAXN];

int main()
{
    int ntest = 0;
    fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
        fin >> N >> K;
        for (int i = 0; i < K; i++)
            dlo[i] = dhi[i] = dcur[i] = 0;
        
        int v0, prev;
        for (int i = 0; i <= N - K; i++)
        {
            int sum; fin >> sum;
            if (i > 0)
            {
                int loc = (i + K - 1) % K;
                dcur[loc] += sum - prev;
                dhi[loc] = max (dhi[loc], dcur[loc]);
                dlo[loc] = min (dlo[loc], dcur[loc]);
            }
            else
                v0 = sum;
            prev = sum;
        }
        
        int dep = 0;
        for (int i = 0; i < K; i++)
        {
            dep = max (dep, dhi[i] - dlo[i]);
            //fout << dlo[i] << " " << dhi[i] << "\n";
        }
        
        int wid = 0, tot = 0;
        for (int i = 0; i < K; i++)
        {
            wid += dep - (dhi[i] - dlo[i]);
            tot += -dlo[i];
        }
        
        bool works = false;
        if (wid >= K - 1) works = true;
        tot = ((tot % K) + K) % K;
        int next = (tot + wid) % K;
        int res = ((v0 % K) + K) % K;
        
        if (wid < K - 1) {
            if (tot <= next && tot <= res && res <= next) works = true;
            if (tot > next)
            {
                works = true;
                if (next < res && res < tot) works = false;
            }
        }
        
        if (!works) dep++;
        
        //if (wid < K - 1)
        //fout << tot << " " << res << " " << next << " " << K << " " << ((works) ? 1 : 0) << "\n";
        
        fout << "Case #" << test + 1 << ": " << dep << "\n";
    }
    return 0;
}
