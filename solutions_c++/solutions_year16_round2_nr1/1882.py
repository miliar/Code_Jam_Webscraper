#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cmath>

#define FOR(i, a, b) for(int i = a; i < b; i++)

using namespace std;

vector<int> digitFreq;
int T;
string S, ans;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("output-large.txt");

    FOR(i, 0, 10) {
        digitFreq.push_back(0);
    }

    fin >> T;

    FOR(i, 0, T) {
        fin >> S;
        FOR(i, 0, 10) {
            digitFreq[i] = 0;
        }

        FOR(j, 0, S.length()) {
            if (S[j] == 'Z') {
                digitFreq[0]++;
            }
            if (S[j] == 'W') {
                digitFreq[2]++;
            }
            if (S[j] == 'U') {
                digitFreq[4]++;
            }
            if (S[j] == 'X') {
                digitFreq[6]++;
            }
            if (S[j] == 'G') {
                digitFreq[8]++;
            }

            if (S[j] == 'F') {
                digitFreq[5]++;
            }
            if (S[j] == 'S') {
                digitFreq[7]++;
            }
            if (S[j] == 'H') {
                digitFreq[3]++;
            }
            if (S[j] == 'O') {
                digitFreq[1]++;
            }
            if (S[j] == 'I') {
                digitFreq[9]++;
            }
        }
        digitFreq[5] -= digitFreq[4];
        digitFreq[7] -= digitFreq[6];
        digitFreq[3] -= digitFreq[8];
        digitFreq[1] -= digitFreq[0] + digitFreq[2] + digitFreq[4];
        digitFreq[9] -= digitFreq[5] + digitFreq[6] + digitFreq[8];

        ans = "";
        char currChar = '0';
        FOR(j, 0, 10) {
            FOR(k, 0, digitFreq[j]) {
                ans += currChar;
            }
            currChar += 1;
        }
        fout << "Case #" << i + 1 << ": " << ans << endl;
    }



    fin.close();
    fout.close();
    return 0;
}
