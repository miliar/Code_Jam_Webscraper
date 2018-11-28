#include <algorithm>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

#define INPUT "a.in"
#define OUTPUT "a.out"

#define N 4

void read() {
    ifstream fin(INPUT);
    ofstream fout(OUTPUT);

    int t; fin >> t;
    
    for (int tt = 1; tt <= t; tt++) {
        set<int> cards;
        cards.clear();

        int line; fin >> line;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int card; fin >> card;
                if (i + 1 == line) {
                    cards.insert(card);
                }
            }
        }

        fin >> line;
        int cnt = 0;
        int magicCard = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                int card; fin >> card;
                if (i + 1 == line && cards.find(card) != cards.end()) {
                    ++cnt;
                    magicCard = card;
                }
            }
        }

        fout << "Case #" << tt << ": ";
        switch (cnt) {
            case 0:
                fout << "Volunteer cheated!\n";
                break;
            case 1:
                fout << magicCard << "\n";
                break;
            default:
                fout << "Bad magician!\n";
        }
    }

    fin.close();
    fout.close();
}

int main() {
    read();    
    return 0;
}
