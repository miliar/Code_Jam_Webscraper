#include <iostream>

using namespace std;

void testLine(char *plateau, bool & winX, bool &winO, int inc) {
    bool O(true), X(true);
    for (int i = 0; i < 4*inc; i+=inc) {
        if (plateau[i] != 'O' && plateau[i] != 'T') {
            O = false;
        }
        if (plateau[i] != 'X' && plateau[i] != 'T') {
            X = false;
        }
    }

    winO |= O;
    winX |= X;
}

enum {
    Left = 1,
    Right = 2,
    Up = 4,
    Down = 8
};

int main()
{
    int n;
    cin >> n;

    for (int Case = 0; Case < n; Case++) {
        int w, h;
        cin >> h >> w;

        char *plateau = new char[w*h];
        char *plateau2 = new char[w*h];

        auto get = [&](int i, int j) {
            return plateau[i+j*w];
        };
        auto getMaxL = [&](int j) {
            int max = 0;

            for (int i = 0; i < w; i++) {
                if (get(i, j) > max) {
                    max = get(i, j);
                }
            }
            return max;
        };
        auto getMaxC = [&](int i) {
            int max = 0;

            for (int j = 0; j < h; j++) {
                if (get(i, j) > max) {
                    max = get(i, j);
                }
            }
            return max;
        };


        for (int i = 0; i < w*h; i++) {
            cin >> plateau[i];
            plateau2[i] = 100;
        }

        for (int j = 0; j < h; j ++) {
            int max = getMaxL(j);
            for (int i = 0; i < w; i++) {
                if (plateau2[i+j*w] > max) {
                    plateau2[i+j*w] = max;
                }
            }
        }
        for (int i = 0; i < w; i ++) {
            int max = getMaxC(i);
            for (int j = 0; j < h; j++) {
                if (plateau2[i+j*w] > max) {
                    plateau2[i+j*w] = max;
                }
            }
        }

        bool allOk = true;
        for (int i = 0; i < w*h; i++) {
            if (plateau[i] != plateau2[i]) {
                allOk = false;
            }
        }

//        for (int j = 0; j < h; j++) {
//            for (int i = 0; i < w; i++) {
//                cout << ok[j*w+i] << " ";
//            }
//            cout << endl;
//        }

        if (allOk) {
            cout << "Case #" << (Case+1) << ": YES" << endl;
        } else {
            cout << "Case #" << (Case+1) << ": NO" << endl;
        }

        delete [] plateau;
    }

    return 0;
}

