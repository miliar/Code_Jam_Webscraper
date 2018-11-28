#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>

#define FOR(i, a, b) for(int i = a; i < b; i++)

using namespace std;

int T, N;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("result-large.txt");


    fin >> T;
    vector<bool> digitFound;
    FOR(i, 0, 10) {
        digitFound.push_back(false);
    }
    int noDigitsFound = 0;
    int currNum = 0;
    int currNumTemp = 0;
    FOR(i, 0, T) {
        fin >> N;
        if (N == 0) {
            fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        }
        else {
            noDigitsFound = 0;
            FOR(k, 0, 10) {
                digitFound[k] = false;
            }
            FOR(j, 1, 101) {
                currNum = N * j;
                currNumTemp = currNum;
                int pow10 = 1;
                int digit;
                while (currNumTemp > 0) {
                    digit = currNumTemp % 10;
                    if (!digitFound[digit]) {
                        digitFound[digit ]= true;
                        noDigitsFound++;
                    }
                    currNumTemp /= 10;
                }
                if (noDigitsFound == 10) {
                    break;
                }
            }
            fout << "Case #" << i + 1 << ": " << currNum << endl;
        }

    }

    fin.close();
    fout.close();

    return 0;
}
