enum Contest { CodeChef, CodeJam };
enum IOBinding { File, StandartStream };

Contest contest = CodeJam;

IOBinding inputBinding = File;
//IOBinding inputBinding = StandartStream;

IOBinding outputBinding = File;
//IOBinding outputBinding = StandartStream;

#include <string>
#include <fstream>
#include <istream>
#include <ostream>
#include <iostream>

std::istream *input;
std::ostream *output;

class Problem {
public:
    Problem();
    ~Problem();

    void solve();

    static char mult(char a, char b);

private:
    void yes() const { *output << "YES\n"; }
    void no () const { *output << "NO\n"; }
    int L, X;
    char *data;
};

Problem::Problem() {
    *input >> L >> X;
    data = new char [L*X];
    for(int i = 0; i < L; ++i) {
        *input >> data[i];
        switch (data[i]) {
        case 'i': data[i] = 2; break;
        case 'j': data[i] = 3; break;
        case 'k': data[i] = 4; break;
        }
    }
    for(int j = 1; j < X; ++j)
        for(int i = 0; i < L; ++i)
            data[i+j*L] = data[i+(j-1)*L];
}

Problem::~Problem() {
    delete[] data;
}

void Problem::solve() {
    int n = 0, N = X*L;
    char val = 1;

    while((n < N) && (val != 2)) {
        val = mult(val, data[n]);
        ++n;
    }

    if (val != 2) return no();
    else val = 1;

    while((n < N) && (val != 3)) {
        val = mult(val, data[n]);
        ++n;
    }

    if (val != 3) return no();
    else val = 1;

    while((n < N) && (val != 4)) {
        val = mult(val, data[n]);
        ++n;
    }

    if (val != 4) return no();
    else val = 1;

    while(n < N) {
        val = mult(val, data[n]);
        ++n;
    }

    if (val != 1) return no();
    else return yes();
}

char Problem::mult(char a, char b) {
    static char table[4][4] = {
        {  1,  2,  3,  4 },
        {  2, -1,  4, -3 },
        {  3, -4, -1,  2 },
        {  4,  3, -2, -1 }
    };
    char res = 1;
    if (a < 0) { res *= -1; a = -a; }
    if (b < 0) { res *= -1; b = -b; }
    return res * table[--a][--b];
}

void solveCase() {
    Problem p;
    p.solve();
}

int main(int argc, char *argv[])
{
    std::ios_base::sync_with_stdio(false);

    if (inputBinding == File)
        input = new std::ifstream("input.txt");
    else input = &std::cin;

    if (outputBinding == File)
        output = new std::ofstream("output.txt");
    else output = &std::cout;

    int T; *input >> T;
    for(int t = 1; t <= T; ++t) {
        if (contest == CodeJam)
            *output << "Case #" << t << ": ";
        solveCase();
    }

    if (inputBinding == File) delete input;
    if (outputBinding == File) delete output;

    return 0;
}
