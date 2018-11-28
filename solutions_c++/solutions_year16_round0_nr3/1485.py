#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <random>

using namespace std;
FILE* in; FILE* out;

const int MAX = 1024;

mt19937_64 mt;
long long rnd() {
    long long ret = mt();
    return ret < 0 ? -ret : ret;
}

const int NUM_PRIMES = 100;

vector <int> primes;
vector < vector <int> > rem(9, vector <int>(NUM_PRIMES, 0));

bool good(unsigned num, int digs) {
    for (int i = 0; i < (int)rem.size(); i++)
        for (int c = 0; c < (int)rem[i].size(); c++)
            rem[i][c] = 0;
    
    for (int d = 0; d < digs; d++) {
        for (int i = 0; i < (int)rem.size(); i++) {
            for (int c = 0; c < (int)rem[i].size(); c++) {
                rem[i][c] *= i + 2;
                if (num & (1U << d))
                    rem[i][c]++;
                rem[i][c] %= primes[c];
            }
        }
    }
    
    for (int i = 0; i < (int)rem.size(); i++) {
        bool found = false;
        for (int c = 0; c < (int)rem[i].size(); c++) {
            if (rem[i][c] == 0) {
                found = true;
                break;
            }
        }
        if (!found)
            return false;
    }
    return true;
}

bool isPrime(int num) {
    if (num < 2) return false;
    for (int d = 2; d * d <= num; d++)
        if (num % d == 0) return false;
    return true;
}

void solveTest() {
    int n, k;
    fscanf(in, "%d %d", &n, &k);
    
	for (int next = 2; (int)primes.size() < NUM_PRIMES; next++)
	    if (isPrime(next)) primes.push_back(next);

    set <unsigned> seen;
    while (k > 0) {
        long long bits = rnd();
        unsigned num = (1U << (n - 1)) | 1U;
        for (int i = 1; i < n - 1; i++)
            if (bits & (1LL << i)) num |= (1U << i);

        if (seen.find(num) != seen.end())
            continue;
        seen.insert(num);

        if (good(num, n)) {
            k--;
            for (int i = 0; i < n; i++) {
                fprintf(out, "%d", !!(num & (1U << i)));
            }
            for (int i = 0; i < (int)rem.size(); i++) {
                for (int c = 0; c < (int)rem[i].size(); c++) {
                    if (rem[i][c] == 0) {
                        fprintf(out, " %d", primes[c]);
                        break;
                    }
                }
            }
            fprintf(out, "\n");
        }
    }
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("CoinJam.in", "rt");
	out = fopen("CoinJam.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d:\n", test);
		solveTest();
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
