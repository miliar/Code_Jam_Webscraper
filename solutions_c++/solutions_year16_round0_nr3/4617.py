#include <bits/stdc++.h>
#include <string>

using namespace std;

const size_t kMaxBase = 10;

int T;

class Solution {
public:
    int divisors[kMaxBase + 1];
    string solution;

    friend ostream& operator<<(ostream &out, const Solution &sol) {
        out << sol.solution << " ";
        for (int i = 2; i < kMaxBase + 1; i++) {
            out << sol.divisors[i] << " ";
        }

        return out;
    }
};

string get_bit_repr(int x) {
    string res = "";

    while (x != 0) {
        res = to_string(x % 2) + res;
        x /= 2;
    }

    return res;
}

long long to_base(string bits, int base) {
    int pw = bits.size() - 1;
    long long ans = 0L;

    for (int i = 0; i < bits.size(); i++) {
        ans += (long long)(bits[i] - '0') * (long long)pow(base, pw - i);
    }

    return ans;
}

int get_divisor(long long x) {
    for (long long i = 2; i * i <= x; i++) {
        if (x % i == 0)
            return i;
    }

    return 1;
}

Solution current_solution;

void gen() {
    int x = to_base(current_solution.solution, 2);
    cerr << "first bits: " << current_solution.solution << "\n";

    while (true) {
        x += 2;

        string bits = get_bit_repr(x);
        cerr << "current bits: " << bits << endl;
        current_solution.solution = bits;

        int i;
        for (i = 2; i < kMaxBase + 1; i++) {
            int div = get_divisor(to_base(bits, i));
            if (div > 1) {
                current_solution.divisors[i] = div;
            } else {
                break;
            }
        }

        if (i == kMaxBase + 1) {
            for (int j = 2; j < 11; j++) {
//                cerr << "  " << to_base(bits, j) << "\n";
            }
            return;
        }
    }
}

void solve(int J, int N) {
    cout << "Case #1:\n";

    current_solution.solution = get_bit_repr((1 << (N - 1)) - 1);

    for (int i = 0; i < J; i++) {
        gen();
        cout << current_solution << "\n";
    }
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    ios_base::sync_with_stdio(false);

    cin >> T;

    for (int t = 0; t < T; t++) {
        int j, n;
        cin >> n >> j;
        solve(j, n);
    }
}
