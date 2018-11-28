#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#define present(col, el) (col.find(el) != col.end())

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int main() {
    long long T, A, n, last = -1;
    fin >> T;
    for (int t = 0; t < T; ++t) {
        last = -1;
   //     cout << "testCase #" << t + 1 << endl;
        fin >> A >> n;
        vector<long long> a(n), b;
        for (int i = 0; i < n; ++i) {
            fin >> a[i];
        }
        sort(a.begin(), a.end());

        for (int i = 0; i < n; ++i) {
            if (A > a[i]) {
                A += a[i];
                last = i;
            }
        }
        for (int i = last + 1; i < n; ++i) {
            b.push_back(a[i]);
        }
        long long minOperations = 100000, curOperations;
        if (A > 1) {
            for (int i = 0; i <= b.size(); ++i) {
                long long pA = A;
                curOperations = b.size() - i; /// b.size()->| o o o | O O |<-0
                for (int j = 0; j < i; ++j) {
                    while (pA <= b[j]) {
                        pA += (pA - 1);
                        curOperations++;
                    }
                    pA += b[j];
                }
                if (curOperations < minOperations) {
                    minOperations = curOperations;
                }
            }
        }
        else {
            minOperations = b.size();
        }
        fout << "Case #" << t + 1 << ": " << minOperations << endl;
    }
    return 0;
}
