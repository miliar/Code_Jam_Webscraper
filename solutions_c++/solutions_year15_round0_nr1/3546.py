#include <bits/stdc++.h>

using namespace std;

int Solve() {
    size_t size;
    cin >> size;
    int people = 0, answer = 0;
    for (size_t index = 0; index < size + 1; ++index) {
        char symbol;
        cin >> symbol;
        if (symbol != '0' && index > people + answer) {
            answer = index - people;
        }
        people += symbol - '0';
    }
    return answer;
}

int main() {
    assert(freopen("A.in", "r", stdin) != NULL);
    assert(freopen("output.txt", "w", stdout) != NULL);
    size_t number_question;
    cin >> number_question;
    for (size_t number = 0; number < number_question; ++number) {
        cout << "Case #" << number + 1 << ": " << Solve() << endl;
    }
    return 0;
}
