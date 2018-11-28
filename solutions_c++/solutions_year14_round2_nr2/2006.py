#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

#define INF ~(1 << 31)

using namespace std;
int main(int argc, char *argv[]) {
    
    ifstream fin("lottery.in");
    ofstream fout("lottery.out");
    
    int T; fin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        int A, B, K; fin >> A >> B >> K;
        int count = 0;
        for (int i = 0; i < A; i++)
            for (int j = 0; j < B; j++)
                count += ((i & j) < K);
                    
        fout << "Case #" << t << ": " << count << "\n";
    }
    
    fin.close();
    fout.close();
    return 0;
}