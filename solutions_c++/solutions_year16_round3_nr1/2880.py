#include <bits/stdc++.h>

using namespace std;

struct data {
    int key, id;
    data (int _k, int _i) {
        key = _k, id = _i;
    }
    data () {}
    bool operator < (const data &d) const {
        return key < d.key;
    }
};

int T, N, cs = 0, Sum;
priority_queue <data> PQ;

int main() {
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    scanf("%d", &T); while (T--) {
        scanf("%d", &N);
        Sum = 0;
        for (int i = 0; i < N; i++) {
            int x; scanf("%d", &x);
            PQ.push(data(x, i));
            Sum += x;
        }
        printf("Case #%d:", ++cs);

        while (Sum) {
            if (PQ.size() == 2) {
                data D1 = PQ.top(); PQ.pop();
                data D2 = PQ.top(); PQ.pop();
                int rem = D1.key;
                char c1 = (char)(D1.id + 'A'), c2 = (char)(D2.id + 'A');
                while (rem--) Sum -= 2, cout << " " << c1 << c2;
                continue;
            }

            data D1 = PQ.top(); PQ.pop();
            data D2 = PQ.top(); PQ.pop();
            data D3 = PQ.top(); PQ.pop();

            if (2 * D1.key - 2 <= Sum and 2 * D2.key + 2 <= Sum and 2 * D3.key + 2 <= Sum) {
                Sum -= 2, D1.key -= 2;
                char c = (char)('A' + D1.id);
                cout << " " << c << c;
            }
            else if (2 * D1.key <= Sum and 2 * D2.key <= Sum and 2 * D3.key + 2 <= Sum) {
                Sum -= 2, D1.key--, D2.key--;
                char c1 = (char)('A' + D1.id), c2 = (char)('A' + D2.id);
                cout << " " << c1 << c2;
            }
            else {
                Sum--, D1.key--;
                char c = (char)('A' + D1.id);
                cout << " " << c;
            }

            if (D1.key) PQ.push(D1);
            if (D2.key) PQ.push(D2);
            if (D3.key) PQ.push(D3);
        }
        cout << endl;
        while (!PQ.empty()) PQ.pop();
    }
    return 0;
}

