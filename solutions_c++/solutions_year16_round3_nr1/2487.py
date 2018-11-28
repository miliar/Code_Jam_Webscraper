#include <iostream>
#include <queue>
using namespace std;

bool compare(pair <char, int> a, pair <char, int> b) {
    return a.second < b.second;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int N;
        cin >> N;
        int S = 0;
        priority_queue <pair<char, int>,
        std::vector<pair<char, int> >,
        std::function<bool(pair <char, int>, pair <char, int>)> > ps(compare);
        for (int n = 0; n < N; ++n) {
            int P;
            cin >> P;
            S += P;
            ps.push(pair <char, int> ('A' + n, P));
        }

        cout << "Case #" << t + 1 << ":";
        while (!ps.empty()) {
            pair <char, int> top = ps.top();
            ps.pop();

            cout << " " << top.first;

            --top.second;
            --S;
            if (top.second > 0) {
                ps.push(top);
            }

            if (S > 0) {
                top = ps.top();
                if ((double)top.second / (double)S > 0.5) {
                    ps.pop();

                    cout << top.first;

                    --top.second;
                    --S;
                    if (top.second > 0) {
                        ps.push(top);
                    }
                }
            }
        }
        cout << endl;
    }
}
