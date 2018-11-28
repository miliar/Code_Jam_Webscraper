#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int N;
int W[4];

bool cover(int tocover, int i)
{
    //cerr << "tocover " << tocover << " " << i << " " << W[i] << endl;
    if (tocover == 0)
        return true;
    if (i == N)
        return false;
    for (int j = 0; j < N; j++)
    {
        //cerr << "bit " << j << endl;
        if ((W[i] & (1<<j)) && (tocover & (1<<j)) && cover(tocover & (~(1<<j)), i+1))
            return true;
    }
    return false;
}

bool iscorrect(int bm)
{
    int obm = bm;
    for (int i = 0; i < N; i++)
    {
        //cerr << "BM: "  << bm << endl;
        W[i] = bm & ((1<<N)-1);
        bm >>= N;
    }
    sort(W, W+N);
    do
    {
        //if (obm == 15)
       // {
           // cerr << W[0] << " " << W[1] << " " << cover(W[0], 1) << endl;
       // }
        if (cover(W[0], 1))
            return false;
       // cerr << "Next?" << endl;
    } while(next_permutation(W, W+N));
    return true;
}

int main()
{
    //istream& in = cin;
    //ostream& out = cout;
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in >> T;
    for (int t = 1; t <= T; t++)
    {
        in >> N;
        int B = 0;
        char c;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                in >> c;
                bool b = (c == '1');
                int p = i*N+j;
                B |= (b<<p);
            }
        }
        //cerr << B << endl;
        int res = N*N;
        for (int i = 0; i < (1<<(N*N)); i++)
        {
            if (B & ~i)
                continue;
            if (iscorrect(i))
            {
                //cerr << "S: " << i << endl;
                res = min(res, __builtin_popcount(i) - __builtin_popcount(B));
            }
        }
        out << "Case #" << t << ": " << res << endl;
    }
}
