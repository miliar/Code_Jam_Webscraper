#include <fstream>

using namespace std;

ifstream fin("magictrick.in");
ofstream fout("magictrick.out");

int main() {

    int T; fin >> T;

    for (int i = 1; i <= T; i++) {

        int firstRow; fin >> firstRow;
        int firstCards[4][4];
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                fin >> firstCards[j][k];
            }
        }

        int secondRow; fin >> secondRow;
        int secondCards[4][4];
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                fin >> secondCards[j][k];
            }
        }

        int same;
        int sameCount = 0;

        for (int j = 0; j < 4; j++) {
            int compare = firstCards[firstRow - 1][j];
            for (int k = 0; k < 4; k++) {
                if (compare == secondCards[secondRow - 1][k]) {
                    same = compare;
                    sameCount++;
                    break;
                }
            }
        }
        if (sameCount == 1) {
            fout << "Case #" << i << ": " << same << "\n";
        } else if (sameCount > 1) {
            fout << "Case #" << i << ": Bad magician!" << "\n";
        } else if (sameCount == 0) {
            fout << "Case #" << i << ": Volunteer cheated!" << "\n";
        }
    }

fout.close();

return 0;
}
