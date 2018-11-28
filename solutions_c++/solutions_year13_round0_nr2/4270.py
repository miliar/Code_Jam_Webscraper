#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <utility>
#include <cmath>
#include <string>

using namespace std;

string lawnmow()
{
    int N, M;
    cin >> N >> M;
    vector< vector<int> > lawn(N);
    for (int n = 0; n < N; ++n) {
        lawn[n] = vector<int>(M);
        for (int m = 0; m < M; ++m)
            cin >> lawn[n][m];
    }
    
//    for (int n = 0; n < N; ++n) {
//        for (int m = 0; m < M; ++m)
//            cout << lawn[n][m] << ' ';
//        cout << endl;
//    }

    for (int n = 0; n < N; ++n) {
        for (int m = 0; m < M; ++m) {
            bool success = true;
            for (int n2 = 0; n2 < N; ++n2) {
                if (lawn[n2][m] > lawn[n][m])
                    success = false;
            }
            if (success)
                continue;
            
            success = true;
            for (int m2 = 0; m2 < M; ++m2) {
                if (lawn[n][m2] > lawn[n][m])
                    success = false;
            }
            if (success)
                continue;
            
            return "NO";
        }
    }
    
    return "YES";
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        string output = lawnmow();

        cout << "Case #" << t + 1 << ": " << output << endl;
    }

    return 0;
}
