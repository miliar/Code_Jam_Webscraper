#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

struct Quaternion {
    bool sign;
    char symbol;

    Quaternion(bool _sign, char _symbol) {
        sign = _sign;
        symbol = _symbol;
    }

    Quaternion multiply(Quaternion quaternion) {
        Quaternion result = product(symbol, quaternion.symbol);
        result.sign ^= sign;
        result.sign ^= quaternion.sign;

        return result;
    }

    void dump() {
        if (!sign)
            cout << "-";
        cout << symbol;
    }

    static const Quaternion matrix[4][4];

private:
    int getId(char symbol) {
        switch(symbol) {
        case '1':
            return 0;
        case 'i':
            return 1;
        case 'j':
            return 2;
        case 'k':
            return 3;
        default:
            return -1;
        }
    }

    Quaternion product(char leftSymbol, char rightSymbol) {
        int leftSymbolId = getId(leftSymbol);
        int rightSymbolId = getId(rightSymbol);
        return matrix[leftSymbolId][rightSymbolId];
    }
};

const Quaternion Quaternion::matrix[4][4] = {
    { Quaternion(false, '1'), Quaternion(false, 'i'), Quaternion(false, 'j'), Quaternion(false, 'k') },
    { Quaternion(false, 'i'), Quaternion(true, '1'), Quaternion(false, 'k'), Quaternion(true, 'j') },
    { Quaternion(false, 'j'), Quaternion(true, 'k'), Quaternion(true, '1'), Quaternion(false, 'i') },
    { Quaternion(false, 'k'), Quaternion(false, 'j'), Quaternion(true, 'i'), Quaternion(true, '1') }
};

int N;
int L, X;
string expr;
bool res;

char next(char symbol) {
    switch(symbol) {
    case 'i':
        return 'j';
    case 'j':
        return 'k';
    case 'k':
        return '#';
    default:
        return '*';
    }
}

bool isRight(char symbol, int from, int to) {
    if (from > to) {
        return symbol == '#';
    }

    if (symbol == '#') {
        return false;
    }

    Quaternion q(false, expr[from++]);
    while(from <= to) {
        if (!q.sign && q.symbol == symbol) {
            bool success = isRight(next(symbol), from, to);
            if (success) {
                return true;
            }

            if (symbol == 'i' || symbol == 'j') return false;
        }
/*
        cout << q.sign << " | " << q.symbol << " vs " << symbol << endl;
*/
        Quaternion otherQ(false, expr[from++]);
        /*q.dump();
        cout << " * ";
        otherQ.dump();*/

        q = q.multiply(otherQ);

        /*cout << " = ";
        q.dump();
        cout << endl;*/
    }

    bool flag = false;
    if (!q.sign && q.symbol == symbol) {
        flag = isRight(next(symbol), from, to);
    }
    return flag;
}

void solve() {
    res = isRight('i', 0, expr.size() - 1);
}

void clean() {
    expr.clear();
}

void read() {
    cin >> L >> X;
    string subExpr;
    cin >> subExpr;

    for (int i = 0; i < X; i++) {
        expr.append(subExpr);
    }
}

void print() {
    if (res) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}

int main() {
    int n;
    scanf("%d", &n);
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');

    for (int i = 1; i <= n; i++) {
        clean();
        read();
        solve();

        printf("Case #%d: ", i);
        print();
        printf("\n");
    }

    return 0;
}

