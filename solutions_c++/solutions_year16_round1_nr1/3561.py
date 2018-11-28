#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
    int count = 0;
    cin >> count;

    cin.ignore();

    for (int cnt = 1; cnt <= count; cnt++) {
        string S;
        getline(cin, S);

        deque<char> deq;

        deq.push_back(S[0]);

        for (int i = 1; i < S.size(); i++) {

            char deqBack = deq.back();
            char deqFront = deq.front();

            if (deqFront <= S[i] ) {
                deq.push_front(S[i]);
            } else {
                deq.push_back(S[i]);
            }
        }

        cout << "Case #" << cnt << ": ";

        for (char c : deq) {
            cout<<c;
        }

        cout << endl;
    }
}