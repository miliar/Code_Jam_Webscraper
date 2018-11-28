#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>
#include <list>
#include <cstring>
#include <cstdlib>
#include <limits>
#include <stack>

using namespace std;

ofstream fout ("A-small-attempt0.out");
ifstream fin ("A-small-attempt0.in");

int main() {
    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        int a, b;
        fin >> a;
        int A[4][4], B[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fin >> A[i][j];
            }
        }
        fin >> b;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fin >> B[i][j];
            }
        }
        int ans = 0;
        int c = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (A[a-1][i] == B[b-1][j]) {
                    c++;
                    ans = A[a-1][i];
                }
            }
        }
        if (c == 1) fout << "Case #" << t << ": " << ans << endl;
        else if (c == 0) fout << "Case #" << t << ": Volunteer cheated!" << endl;
        else fout << "Case #" << t << ": Bad magician!" << endl;
    }
}
