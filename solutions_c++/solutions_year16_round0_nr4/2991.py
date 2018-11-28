#include <iostream>
#include <vector>
using namespace std;

long lpow(long base, long exp)
{
    long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

vector<long> solve(long K, long C, long S)
{
    vector<long> result;
    if (C > K) {
        C = K;
    }
    
    long totalNum = lpow(K, C);
    
    long numRegularTests = K / C;
    long numTests = (K + C - 1) / C;
    
    if (S < numTests) {
        return result; // Impossible
    }
    
    for (long test=0; test<numRegularTests; ++test) {
        long index = 0;
        for (long cc=0; cc < C; ++cc) {
            index += (test*C+cc) * lpow(K, C-cc-1);
        }
        result.push_back(index+1); // 1-based
    }
    
    if (numTests > numRegularTests)
    {
        long D = K - numRegularTests * C;
        long index = 0;
        for (long dd=0; dd < D; ++dd) {
            index += (numRegularTests*C+dd) * lpow(K, D-dd-1);
        }
        if(index>=totalNum) {
            abort();
        }
        result.push_back(index+1);
    }
    
    return result;
}

int main()
{
    int nCases;
    cin >> nCases;
    cin.ignore (1, '\n');
    for (int i=0; i<nCases; ++i) {
        long K, C, S;
        cin >> K >> C >> S;
        vector<long> result = solve(K, C, S);
        cout << "Case #" << i+1 << ": ";
        if (result.empty()) {
            cout << "IMPOSSIBLE";
        } else {
            for (int i=0; i<result.size()-1; ++i) {
                cout << result[i] << " ";
            }
            cout << result[result.size()-1];
        }
        cout << endl;
    }
    return 0;
}
