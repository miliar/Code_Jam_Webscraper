#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>
#include <bitset>

#define VI vector<int>
#define PII pair<int, int>
#define VPI vector<PII>
#define MII map<int, int>
#define LLI long long int
#define SZN 105
#define MXN 1005
#define _ ios_base::sync_with_stdio(0); // do not use scanf or printf with this

const int inf = 0x3f3f3f3f;
const double eps = 1e-6;
const double pi = acos(-1.0);

using namespace std;

/* structs */

/* globals */
vector<int> primes;
int powers[75000][11][33];
int binary[33];
int t, n, m;

/* function declarations */
int isPrime(int);


/* Problem */
int main() { _ // disable sync with stdio
    cin >> t >> n >> m; // m instead of j
    cout << "Case #1:\n";

    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);
    bool bad;
    for (int i = 7; i < 1000000; i += 2) {
        bad = false;
        for (int j = 1; j < min((int) primes.size(), (int) sqrt(i) + 1); ++j) {
            if (i % primes[j] == 0) {
                bad = true;
                break;
            }
        }
        if (!bad) {
            primes.push_back((LLI) i);
        }
    }

    int tmp;
    for (int k = 0; k < 25000; ++k) {
        for (int i = 2; i <= 10; ++i) {
            powers[k][i][0] = 1;
            tmp = 1;
            for (int j = 1; j < n; ++j) {
                tmp *= i;
                tmp = tmp % primes[k];
                powers[k][i][j] = tmp;
            }
        }
    }

    memset(binary, 0, sizeof(binary));
    binary[0] = 1;
    binary[n-1] = 1;
    while (m) {
        string str = "";
        int numOnes = 0;
        for (int i = 0; i < n; ++i) {
            if (binary[i]) {
                str = "1" + str;
                ++numOnes;
            } 
            else str = "0" + str;
        }
        str += " ";
        bool bad = false;
        for (int j = 2; j < 11; ++j) {
            int divisor = isPrime(j);
            if (divisor == -1) {
                bad = true;
                break;
            } else {
                str += " " + to_string(divisor);
            }
        }
        if (!bad) {
            cout << str << "\n";
            --m;
        }
        if (numOnes == n) {
            cout << "need more...\n";
            break;
        }
        for (int j = 1; j < n-1; ++j) {
            if (binary[j] == 1) {
                binary[j] = 0;
            } else {
                binary[j] = 1;
                break;
            }
        }
    }

    return 0;
}

int isPrime(int index) {
    int sum;
    for (int i = 0; i < 25000; ++i) {
        if (primes[i] > pow(index, n/2)) {
            break;
        }
        sum = 0;
        for (int j = 0; j < n; ++j) {
            if (binary[j])
                sum += powers[i][index][j];
        }
        if (sum % primes[i] == 0) {
            return primes[i];
        }
    }
    return -1;
}
