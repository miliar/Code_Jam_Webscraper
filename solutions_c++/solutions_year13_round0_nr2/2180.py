#include <cstdlib>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream in("lawn.in");
    ofstream out("lawn.out");
    int N;
    in >> N;
    int data[105][105];
    int row[105];
    int col[105];
    for (int i = 0; i < N; i++) {
        int W, H;
        in >> H >> W;
        for (int i2 = 0; i2 < H; i2++)
            for (int i3 = 0; i3 < W; i3++) {
                in >> data[i2][i3];
                row[i2] = -1;
                col[i3] = -1;
            }
        for (int i2 = 0; i2 < H; i2++)
            for (int i3 = 0; i3 < W; i3++)
                if (data[i2][i3] > row[i2])
                    row[i2] = data[i2][i3];
        for (int i2 = 0; i2 < H; i2++)
            for (int i3 = 0; i3 < W; i3++)
                if (data[i2][i3] > col[i3])
                    col[i3] = data[i2][i3];
        bool valid = true;
        for (int i2 = 0; i2 < H && valid; i2++)
            for (int i3 = 0; i3 < W && valid; i3++)
                if (data[i2][i3] != row[i2] && data[i2][i3] != col[i3]) {
                    valid = false;
                }
        if (valid)
            out << "Case #" << (i + 1) << ": YES\n";
        else
            out << "Case #" << (i + 1) << ": NO\n";
    }
    return 0;
}

