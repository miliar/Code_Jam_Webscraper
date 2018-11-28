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

int T, N;
vector<int> parties;
int totSen = 0;

void remove_largest(ofstream fout) {
    int largestParty;
    int noSen = -1;
    FOR(i, 0, N) {
        if (parties[i] > noSen) {
            noSen = parties[i];
            largestParty = i;
        }
    }
    parties[largestParty]--;
    fout << (char)(largestParty + 65) << ' ';
}

void clean_up(ofstream fout) {
    FOR(i, 0, N) {
        if (parties[i] == 1) {
            parties[i]--;
            fout << (char)(i + 65);
        }
    }
}

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("A-largeoutput.txt");

    fin >> T;

    FOR(i, 0, T) {
        fin >> N;
        fout << "Case #" << i + 1 << ": ";
        FOR(j, 0, N) {
            int temp;
            fin >> temp;
            totSen += temp;
            parties.push_back(temp);
        }
        int noPartiesActive = 0;
        FOR(j, 0, totSen - 2) {
            int largestParty;
            int noSen = -1;
            FOR(k, 0, N) {
                if (parties[k] > noSen) {
                    noSen = parties[k];
                    largestParty = k;
                }
                if (parties[k] > 0) {
                    noPartiesActive++;
                }
            }
            if (noPartiesActive > 2) {
                parties[largestParty]--;
                fout << (char)(largestParty + 65) << ' ';
            }
            else {
                break;
            }
        }
            if (noPartiesActive == 2) {
                int p1 = -1;
                int p2 = -1;
                FOR(k, 0, N) {
                    if (parties[k] > 0) {
                        if (p1 == -1) {p1 = k;}
                        else {p2 = k;};
                    }
                }
                FOR(k, 0, parties[p1]) {
                    fout << (char)(p1 + 65) << (char)(p2 + 65) << ' ';
                }
            }
            FOR(k, 0, N) {
        if (parties[k] == 1) {
            parties[k]--;
            fout << (char)(k + 65);
        }
    }

        parties.clear();
        totSen = 0;
        fout << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
