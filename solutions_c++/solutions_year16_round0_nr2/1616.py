#include <iostream>
#include <string>
using namespace std;

int N, CNT;
string S;

void flip(int P) {
    string NS;
    for (int a = P; a >= 0; --a) {
        NS.push_back(S[a] == '-' ? '+' : '-');
    }
    for (int a = P + 1; a < (int)S.size(); ++a)
        NS.push_back(S[a]);
    S = NS;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int a = 1; a <= N; ++a) {
        cin >> S;
        CNT = 0;
        while (true) {
            int last = -1;
            int lrun = -1;
            for (int b = 0; b < (int)S.size(); ++b)
                if (S[b] == '-')
                    last = b;
            for (int b = 0; b < (int)S.size(); ++b) {
                if (S[b] == '+')
                    ++lrun;
                else break;
            }
            if (last == -1) break;
            ++CNT;
            if (~ lrun) flip(lrun);
            else flip(last);
        }
        cout << "Case #" << a << ": " << CNT << "\n";
    }
    return 0;
}
