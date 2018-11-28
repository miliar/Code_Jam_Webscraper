#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#include <string>

#define FOR(i, a, b) for(int i = a; i < b; i++)

using namespace std;

int T, N;
string S;

int main()
{
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("result-large.txt");
    fin >> T;
    FOR(i, 0, T) {
        fin >> S;
        int interchanges = 0;
        FOR(j, 0, S.length() - 1) {
            if (S[j] != S[j + 1]) {
                interchanges++;
            }
        }
        if (S[S.length() - 1] == '-') {
            interchanges++;
        }
        fout << "Case #" << i + 1 << ": " << interchanges << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
