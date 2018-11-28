#include <iostream>
#include <fstream>

using namespace std;

long long ipow(long long base, long long exp)
{
    long long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

void tiles(int i, int K, int C, int S, ostream &output_file) {
//    cout << K << " " << C << " " << S << "\n";
    output_file << "Case #" << i << ":";
    if (S < K) {
        output_file << " IMPOSSIBLE"; // TODO
    }
    else {
        long long step = ipow(K, C - 1);
        long long s = 1;
        for (int j = 1; j <= K; j++) {
            output_file << " " << s;
            s += step;
        }
    }
    output_file << "\n";
}

int main(int argc, char *argv[]) {
    ifstream input_file;
    ofstream output_file;
    input_file.open("/home/ars/ClionProjects/ForTests/input.txt");
    output_file.open("/home/ars/ClionProjects/ForTests/output.txt");
    if (input_file.fail()) {
        cout << "Failed to open file\n";
    }

    int T, K, C, S;
    input_file >> T;
    for (int i = 1; i <= T; i++) {
        input_file >> K;
        input_file >> C;
        input_file >> S;
        tiles(i, K, C, S, output_file);
    }

    return 0;
}