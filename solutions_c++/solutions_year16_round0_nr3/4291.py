#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int CNT = 50;

struct node {
    int value;
    int div[9];
};

int n;
vector<node> sol;
vector<int> primes;

void print_binary(int curr, vector<int>& bits) {
    bits.clear();
    for (int i = 0; i < n; i++)
        if (curr & (1 << i)) bits.push_back(1);
        else bits.push_back(0);
}

node test(int curr) {
    node ret;
    ret.value = -1;
    vector<int> bits;
    print_binary(curr, bits);
    if (bits[0] != 1 || bits.back() != 1)
        return ret;
    for (int i = 2; i <= 10; i++) {
        long long value = 0;
        long long curr = 1;
        for (int j = 0; j < bits.size(); j++) {
            value += curr * bits[j];
            curr *= i;
        }
        bool found = false;
        for (int j = 0; j < primes.size(); j++) {
            if (primes[j] == value) break;
            if ((int)sqrt(value) < primes[j]) break;
            if (value % primes[j] == 0) {
                ret.div[i - 2] = primes[j];
                found = true;
                break;
            }
        }
        if (!found) return ret;
    }
    ret.value = curr;
}

int main() {
    n = 16;

    // Read primes
    freopen("primes_small.out", "r", stdin);
    int p;
    while (scanf("%lld", &p) != EOF) {
        primes.push_back(p);
    }

    for (int i = 0; i < (1 << n); i++) {
        node curr = test(i);
        if (curr.value != -1) sol.push_back(curr);
        if (sol.size() == CNT) break;
    }

    printf("Case #1:\n");
    vector<int> bits;
    for (int i = 0; i < CNT; i++) {
        print_binary(sol[i].value, bits);
        for (int j = bits.size() - 1; j >= 0; j--) printf("%d", bits[j]);
        for (int j = 0; j < 9; j++) printf(" %d", sol[i].div[j]);
        printf("\n");
    }

    return 0;
}
