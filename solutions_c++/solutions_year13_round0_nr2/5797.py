#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <limits>
#include <iomanip>

#define all(c) (c).begin(),(c).end()

using namespace std;

typedef long long llong;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int caseNum=1;
ifstream fin("B.in");
ofstream fout("B.out");

#define gout fout << "Case #" << caseNum++ << ": ", fout

int main (int argc, char* argv[]) {
    int T;
    fin >> T;

    while (T--) {
        int R,C;
        fin >> R >> C;
        int map[100][100];
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++)
                fin >> map[j][i];
        }
        bool impossible = false;
        for (int r=0; r<R && !impossible; r++) {
            int highest = 0;
            for (int j=0; j<C; j++)
                highest = max(map[j][r], highest);
            for (int c=0; c<C; c++) {
                if (map[c][r] != highest) {
                    for (int r2=0; r2<R; r2++) {
                        if (map[c][r2] > map[c][r]) {
                            impossible = true;
                            break;
                        }
                        map[c][r2] = map[c][r];
                    }
                }
            }
        }
        for (int r=0; r<R; r++) {
            for (int c=0; c<C; c++) {
                cout << map[c][r];
            }
            cout << endl;
        }
        if (impossible) 
            gout << "NO\n";
        else
            gout << "YES\n";
    }

    fin.close();
    fout.close();
    return 0;
}
