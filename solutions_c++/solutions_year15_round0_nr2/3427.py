#include <bits/stdc++.h>

using namespace std;

int Solve() {
    size_t size;
    cin >> size;
    vector <int> arr(size);
    for (int &element : arr) {
        cin >> element;
    }
    int answer = 1000;
    for (int i = 1; i <= 1000; ++i) {
        int rival = 0;
        for (const int& element : arr) {
            rival += max((element - 1) / i, 0);
        }
        answer = min(answer, rival + i);
    }
    return answer;
}

int main() {
#ifdef _DEBUG
    assert(freopen("B.in", "r", stdin) != NULL);
    assert(freopen("output.txt", "w", stdout) != NULL);
#endif
    size_t number;
    cin >> number;
    for (size_t index = 0; index < number; ++index) {
        cout << "Case #" << index + 1 << ": " << Solve() << endl;
    }
    return 0;
}
