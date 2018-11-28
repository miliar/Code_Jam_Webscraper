#include <bits/stdc++.h>
#define ll long long int
using namespace std;

const int MAX_N = 26 + 1;
int findMaxi(int* pa, int n) {
    int maxV = -1;
    int maxInd = -1;

    for (int i=0;i<n;i++) {
        if (maxV < pa[i]) {
            maxV = pa[i];
            maxInd = i;
        }
    }

    return maxInd;
}
bool check(int* p, int n) {
    int maxV = -1;
    int sum = 0;

    for (int i=0;i<n;i++) {
        sum += p[i];
        maxV = max(maxV, p[i]);
    }

    return maxV * 2 <= sum;
}
int main() {
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int t;
    in >> t;
    for (int x=0;x<t;x++) {
        int n, sum = 0;
        int p[MAX_N];
        in >> n;
        for (int i=0;i<n;i++) {
            in >> p[i];
            sum += p[i];
        }
        out << "Case #" << x+1 << ": ";
        for (int i=0;i<sum;i++) {
            int maxInd = findMaxi(p, n);
            p[maxInd]--;
            if (!check(p, n)) {
                int maxIndex2 = findMaxi(p, n);
                p[maxIndex2]--;
                i++;
                out<<(char)('A'+maxInd)<<(char)('A'+maxIndex2)<<" ";
            } else {
                out<<(char)('A'+maxInd)<<" ";
            }
        }
        out << "\n";
    }
    return 0;
}
