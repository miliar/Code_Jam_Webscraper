#include <iostream>
#include <string>
using namespace std;

void work(uint64_t no) {
    unsigned char lawn[100][100];
    int width, height;
    cin >> height >> width;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cin >> lawn[i][j];
        }
    }
    for (int i = 0; i < height; i++) {
        unsigned char lowest = -1;
        for (int j = 0; j < width; j++) {
            bool higher_x = false;
            bool higher_y = false;
            for (int k = 0; k < height; k++) {
                if (k == i)
                    continue;
                if (lawn[i][j] < lawn[k][j])
                    higher_x = true;
            }
            for (int k = 0; k < width; k++) {
                if (k == j)
                    continue;
                if (lawn[i][j] < lawn[i][k])
                    higher_y = true;
            }
            if (higher_x && higher_y) {
                cout << "Case #" << no << ": NO" << endl;
                return;
            }
        }
    }
    cout << "Case #" << no << ": YES" << endl;
}

int main(void) {
    uint64_t cases;
    cin >> cases;
    for (uint64_t i = 1; i <= cases; i++) {
        work(i);
    }
    return 0;
}