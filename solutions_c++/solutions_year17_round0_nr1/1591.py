#include <iostream>
using namespace std;

char reverse(char a) {
    if (a == '-') {
        return '+';
    } else {
        return '-';
    }
}

int countMinStep(string s, int k) {
    int steps = 0;
    int size = s.size();

    for (int i = 0; i < size - k + 1; i++) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; j++) {
                s[j] = reverse(s[j]);
            }
            steps += 1;
        }
    }

    for (int i = size - k + 1; i < size; i++) {
        if (s[i] == '-') {
            steps = -1;
            break;
        }
    }

    return steps;
}

int main() {
    int t;
    string s;
    int k;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> s >> k;
        
        int ansValue = countMinStep(s, k);

        cout << "Case #" << i << ": ";
        if (ansValue == -1) {
          cout << "IMPOSSIBLE";
        } else {
          cout << ansValue;
        }
        cout << endl;
    }
    return 1;
}
