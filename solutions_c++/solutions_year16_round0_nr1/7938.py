#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll solve(ll input) {
    bitset<10> digits; digits.reset();
    ll answer = input;

    int maxIteration = 12345;

    for (int i = 1; maxIteration > 0 && digits.count() != 10; i++, maxIteration--) {
        ll t = input * i;
        answer = t;
        while (t > 0) {
            int digit = (int) (t % 10ll);
            digits[digit] = 1;
            t = t / 10ll;
        }
    }

    return maxIteration == 0 ? -1 : answer;
}

int main()
{
    //freopen("/home/gdhsnlvr/Workspace/OlmProg/urozero/out", "w", stdout);

    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        ll n; cin >> n;
        ll res = solve(n);

        std::cout << "Case #" << i << ": ";
        if (res == -1) {
            std::cout << "INSOMNIA" << std::endl;
        } else {
            std::cout << res << endl;
        }
    }
    return 0;
}

