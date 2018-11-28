#include <fstream>
using namespace std;

int T;
int X, R, C;

int main() {
    ifstream fin("D-small-attempt2.in");
    ofstream fout("D-small-attempt2.out");
    fin >> T;
    int casenum = 1;
    while (T--) {
        fin >> X >> R >> C;
        //
        if (X == 1) {
            fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
        } else if (X == 2) {
            if (R == 1) {
                if (C == 1 || C == 3) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 2 || C == 4) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                }
            } else if (R == 2) {
                fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
            } else if (R == 3) {
                if (C == 1) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 2) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                } else if (C == 3) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 4) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                }
            } else if (R == 4) {
                fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
            }
        } else if (X == 3) {
            if (R == 1) {
                fout << "Case #" << casenum << ": " << "RICHARD" << endl;
            } else if (R == 2) {
                if (C == 1 || C == 2 || C == 4) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 3) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                }
            } else if (R == 3) {
                if (C == 1) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 2 || C == 3 || C == 4) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                }
            } else if (R == 4) {
                if (C == 1) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 2) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else if (C == 3) {
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                } else if (C == 4) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                }
            }
        } else if (X == 4) {
            if (R < 3 || C < 3) {
                fout << "Case #" << casenum << ": " << "RICHARD" << endl;
            } else {
                // R, C at least 3
                if (R == 3 && C == 3) {
                    fout << "Case #" << casenum << ": " << "RICHARD" << endl;
                } else {
                    // 3 4, 4 3, 4 4
                    fout << "Case #" << casenum << ": " << "GABRIEL" << endl;
                }
            }
        }
        //
        casenum++;
    }
    return 0;
}