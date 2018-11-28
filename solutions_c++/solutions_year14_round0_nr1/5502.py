#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        int cand[4];
        int arr[16];
        int r;
        fin >> r;
        for (int i = 0; i < 16; i++) fin >> arr[i];
        memcpy(cand, &arr[(r-1)*4], 4*sizeof(int));
        fin >> r;
        for (int i = 0; i < 16; i++) fin >> arr[i];
        int matches = 0;
        int match;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (cand[i] == arr[4*(r-1)+j]) {
                    matches++;
                    match = cand[i];
                }
            }
        }
        if (matches == 1) fout << "Case #" << t << ": " << match << "\n";
        if (matches == 0) fout << "Case #" << t << ": Volunteer cheated!\n";
        if (matches > 1) fout << "Case #" << t << ": Bad magician!\n";
    }
}