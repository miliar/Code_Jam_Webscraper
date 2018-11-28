#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;

        char best = 0;
        int best_j = -1;
        deque<char> q;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] >= best) {
                q.push_front(s[j]);
                best = s[j];
            } else {
                q.push_back(s[j]);
            }
        }

        cout << "case #" << i + 1 << ": ";
        for (char c : q) {
            cout << c;
        }
        cout << "\n";
    }
    return 0;
}
