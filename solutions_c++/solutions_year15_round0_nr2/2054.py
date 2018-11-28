#include <iostream>
#include <fstream>
#include <cmath>
#include <climits>

using namespace std;

const int P = 1001;
int dp[1001][1001]; // dp[i][j] is the sequential cost to bring a stack of size i down to size j.
int p[1001];

void init() {
    for(int p = 1; p <= P; p++) {
        for(int q = 1; q <= p; q++) {
            dp[p][q] = ceil((double)p / q) - 1;
        }
    }
}

int main() {
    ifstream file_in("B-large.in");
    ofstream file_out("B-large.out");

    size_t T;
    init();

    file_in >> T;
    for(size_t t = 1; t <= T; t++) {
        file_out << "Case #" << t << ": ";
        size_t D = 0;
        file_in >> D;
        int max_p = 0;
        for(size_t d = 0; d < D; d++) {
            file_in >> p[d];
            if(p[d] > max_p) max_p = p[d];
        }
        int min_cost = INT_MAX;
        for(int par = 1; par <= max_p; par++) { // enumerate parallel cost.
            int seq = 0;
            for(size_t d = 0; d < D; d++) { // compute sequential cost.
                if(p[d] >= par) {
                    seq += dp[p[d]][par];
                }
            }
            if(seq + par < min_cost) min_cost = seq + par;
        }
        file_out << min_cost << endl;
    }
    file_in.close();
    file_out.close();
}