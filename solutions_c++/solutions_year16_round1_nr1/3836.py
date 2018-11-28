#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 100;


int main(int argc, char * argv[]) {

    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int T;
    string S;
    string outS;
    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        fin >> S;
        outS = S[0];
        for (int j = 1; j < S.length(); ++j)
        {
            if (S[j] >= outS[0])
            {
                outS = S[j] + outS;
            }
            else
            {
                outS = outS + S[j];
            }
        }
        fout << "Case #" << i << ": " << outS << endl;

    }
    return 0;
}
