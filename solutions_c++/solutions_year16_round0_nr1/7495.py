#include <iostream>
#include <fstream>
#include <string>
using namespace std;

typedef unsigned long long int64;
ifstream in("/Users/msiddeek/workspace/algorithms/input.txt");
ofstream out("/Users/msiddeek/workspace/algorithms/output.txt");

int64 naive(int64 N) {
    int64 x = N;
    int64 v = 0;
    int64 i = 0;
    while (v ^ ((1<<10) - 1)) {
        int64 t = x;
        while (t)
            v |= (1 << (t % 10)), t /= 10;
        x += N;
        i++;
    }
    return x - N;
}

int main() {
    int64 T;
    in >> T;
    for (int64 i = 0; i < T; ++i) {
        int64 N;
        in >> N;
        out << "Case #" << (i + 1) << ": ";
        if (N == 0)
            out << "INSOMNIA";
        else
            out << naive(N);
        out << endl;
    }
    return 0;
}