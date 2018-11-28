#include <iostream>
#include <vector>

using namespace std;

vector<int> counts(2600, 0);

void calc() {
    for (unsigned i = 0; i < counts.size(); i++) {
        int tmp = counts[i];
        if (tmp % 2 == 1) {
            cout << i << " ";
        }
    }    
}

int main() {
    int testCases;
    long long N;
    cin >> testCases;

    for (int i = 1; i <= testCases; i++) {
        cin >> N;
        for (int k = 0; k < (2*N-1)*N; k++) {
            int tmp;
            cin >> tmp;
            counts[tmp]++;
        }
        cout << "Case #" << i << ": ";
        calc();
        cout << endl;
        for (unsigned k = 0; k < counts.size(); k++) {
            counts[k] = 0;
        }
    }

    return 0;
}
