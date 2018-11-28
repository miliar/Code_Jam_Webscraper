#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<ll> vi;
typedef vector<pii> vii;
#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << endl
#define ALL(x) x.begin(), x.end()
#define INF (1 << 30)
#define pb push_back
#define lend '\n'

set<int> primes;
set<int> generatePrimes(int n) {
    vi cands(n + 1, true);
    for (int i = 2; i * i <= n; ++i)
        if (cands[i])
            for (int j = i * i; j <= n; j += i)
                cands[j] = false;
    set<int> primes;
    for (int i = 0; i < (int)cands.size(); ++i)
        if (cands[i]) primes.insert(i);
    return primes;
}

bool accept(bitset<16> bs) {
    vi nums;
    for (int b = 2; b <= 10; ++b) {
        ll num = 0;
        ll po = 1;
        for (int j = 0; j <= 15; ++j) {
            num += bs.test(j) * po;
            po *= b;
        }
        if (primes.count(num) != 0)
            return false;
        nums.pb(num);
    }
    stringstream ss;
    ss << bs.to_string() << " ";
    int divs = 0;
    for (int i = 0; i < (int) nums.size(); ++i) {
        int sr = sqrt(nums[i]) + 2;
        for (int j = 2; j <= sr; ++j) {
            if (nums[i] % j == 0) {
                ss << j << " ";
                ++divs;
                break;
            }
        }
    }
    ss << "\n";
    if (divs != 9) return false;
    cout << ss.str();
    return true;
}

void work() {
    int J = 50;
    int smallest = (1 << 15);
    int largest = (1 << 16) - 1;
    int ans = 0;

    for (int i = smallest; ans != J && i < largest; ++i) {
        if (i % 2 == 0) continue;
        bitset<16> coinjam(i);
        if (accept(coinjam))
            ++ans;
        if (ans == J)
            break;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int largest = (1 << 17) - 1;
    primes = generatePrimes(largest);
    cout << "Case #1:\n";
    work();
}
