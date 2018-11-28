#include <iostream>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

void tc() {
    static int cas = 1;
    cout << "Case #" << cas++ << ": ";
    int r, c; cin >> r >> c;
    vector<string> M(r);
    for (int i = 0; i < r; ++i) cin >> M[i];
    int num = 0;
    for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) {
#define D(dx, dy) ({ int ip, jp; for (ip = i + dy, jp = j + dx; ip >= 0 && ip < r && jp >= 0 && jp < c; ip += dy, jp += dx) if (M[ip][jp] != '.') break; (ip >= 0 && ip < r && jp >= 0 && jp < c); })
#define REQ(v) if (!(v)) { cout << "IMPOSSIBLE" << endl; return; } else { ++num; }
        switch (M[i][j]) {
            case '<': if (!D(-1, 0)) { REQ(D(1, 0) || D(0, -1) || D(0, 1)) } break;
            case '>': if (!D(1, 0)) { REQ(D(-1, 0) || D(0, -1) || D(0, 1)) } break;
            case '^': if (!D(0, -1)) { REQ(D(-1, 0) || D(1, 0) || D(0, 1)) } break;
            case 'v': if (!D(0, 1)) { REQ(D(-1, 0) || D(1, 0) | D(0, -1)) } break;
            case '.': break;
            default: assert(0);
        }
    }
    cout << num << endl;
}

int main() {
    int T; cin >> T; while (T--) tc();
}
