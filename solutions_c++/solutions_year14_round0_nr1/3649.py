#include <iostream>
#include <fstream>
using namespace std;

int n, a, b, cards[4];
bool used[17];

int main() {
    ifstream fin("A.in");
    ofstream fout("A.out");
    fin >> n;
    for (int i = 0; i < n; i++) {
        fin >> a;
        for (int i = 1; i < 17; i++) {
            used[i] = false;
        }
        for (int k = 0; k < a; k++) {
            for (int j = 0; j < 4; j++) {
                fin >> cards[j];
            }
        }
        for (int k = 0; k < 4; k++) {
            used[cards[k]] = true;
        }
        for (int k = a; k < 4; k++) {
            for (int j = 0; j < 4; j++) {
                fin >> cards[j];
            }
        }
        fin >> b;
        for (int k = 0; k < b; k++) {
            for (int j = 0; j < 4; j++) {
                fin >> cards[j];
            }
        }
        int counter = 0, value;
        for (int k = 0; k < 4; k++) {
            if (used[cards[k]]) {
                counter++;
                value = cards[k];
            }
        }
        fout << "Case #" << i + 1 << ": ";
        if (counter == 0) {
            fout << "Volunteer cheated!" << endl;
        }
        else if (counter == 1) {
            fout << value << endl;
        }
        else {
            fout << "Bad magician!" << endl;
        }
        for (int k = b; k < 4; k++) {
            for (int j = 0; j < 4; j++) {
                fin >> cards[j];
            }
        }
    }
}
