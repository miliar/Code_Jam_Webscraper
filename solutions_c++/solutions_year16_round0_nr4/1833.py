#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 100;
char flip (char c)
{
    if (c == '-') return '+';
    return '-';
}

int count_flips(string S)
{
    int flips = 0;
    char cur = S[0];
    int sz = S.length();
    for (int i = 1; i < sz; ++i)
    {
        while (i < sz && S[i] == cur)
        {
            ++i;
        }
        if (i < sz)
        {
            ++flips;
            cur = S[i];
        }
    }
    if (cur == '-') ++flips;
    return flips;
}

int main(int argc, char * argv[]) {

    ifstream fin(argv[1]);
    ofstream fout (argv[2]);
    int T;
    int K;
    int C;
    int S;
    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        fin >> K >> C >> S;
        fout << "Case #" << i << ":";
        for (int j = 1; j <= K; ++j)
        {
            fout << " " << j;
        }
        fout << endl;
    }
    return 0;
}
