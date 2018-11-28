#include <iostream>

using namespace std;

int main() {
    int n = 0, a1 = 0, a2 = 0, map1[4][4], map2[4][4];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a1;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                cin >> map1[x][y];
            }
        }
        cin >> a2;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                cin >> map2[x][y];
            }
        }
        int ii = 0, num = 0;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                if (map1[a1-1][x] == map2[a2-1][y]) {
                    ii++;
                    num = map1[a1-1][x];
                }
            }
        }
        switch(ii) {
            case 1: 
                cout << "Case #" << i+1 << ": " << num << "\n";
                break;
            case 0:
                cout << "Case #" << i+1 << ": " << "Volunteer cheated! \n";
                break;
            default:
                cout << "Case #" << i+1 << ": " << "Bad magician! \n";
        }
    }
    //cout << "Case #" << i+1 << ": ";
    return 0;
}