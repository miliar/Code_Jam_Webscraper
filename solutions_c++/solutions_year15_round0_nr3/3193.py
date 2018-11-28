#include <iostream>

using namespace std;

class LoopString {
public:
    string str;
    char at(long long pos) {
        return str.at(pos % str.size());
    }
};

typedef struct {
    bool negative;
    char number;
} NUMBER;

class Quaternion {
private:
    NUMBER quaternion[4][4];
public:
    Quaternion();
    int getPos(char c);
    bool compare(NUMBER n, char c);
    NUMBER multiply(NUMBER a, char b);
};

Quaternion::Quaternion() {
    quaternion[0][0] = {false, '1'};
    quaternion[0][1] = {false, 'i'};
    quaternion[0][2] = {false, 'j'};
    quaternion[0][3] = {false, 'k'};
    quaternion[1][0] = {false, 'i'};
    quaternion[1][1] = {true, '1'};
    quaternion[1][2] = {false, 'k'};
    quaternion[1][3] = {true, 'j'};
    quaternion[2][0] = {false, 'j'};
    quaternion[2][1] = {true, 'k'};
    quaternion[2][2] = {true, '1'};
    quaternion[2][3] = {false, 'i'};
    quaternion[3][0] = {false, 'k'};
    quaternion[3][1] = {false, 'j'};
    quaternion[3][2] = {true, 'i'};
    quaternion[3][3] = {true, '1'};
}

int Quaternion::getPos(char c) {
    switch (c) {
        case '1': return 0;
        case 'i': return 1;
        case 'j': return 2;
        case 'k': return 3;
    }
    return 0;
}

bool Quaternion::compare(NUMBER n, char c) {
    return (!n.negative && n.number == c);
}

NUMBER Quaternion::multiply(NUMBER a, char b) {
    NUMBER c = quaternion[getPos(a.number)][getPos(b)];
    c.negative = a.negative ^ c.negative;
    return c;
}

int main(int argc, char *argv[]) {
    int T, position;
    long long X, L, XL;
    char phrase[] = {'i', 'j', 'k'};
    bool ok;
    LoopString ls;
    NUMBER n;
    Quaternion q;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> X >> L >> ls.str;
        XL = X * L;
        position = 0;
        n.negative = false;
        n.number = ls.at(0);
        for (long long j = 1; j < XL; ++j) {
            if (position < 2) {
                if (q.compare(n, phrase[position])) {
                    ++position;
                    n = {false, ls.at(j)};
                    continue;
                }
            }
            n = q.multiply(n, ls.at(j));
        }
        ok = (position == 2 && q.compare(n, 'k'));
        cout << "Case #" << (i + 1) << ": " << (ok ? "YES" : "NO") << endl;
    }
    return 0;
}
