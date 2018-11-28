#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <queue>
using namespace std;

#define MOD 1000002013

struct trip {
    int o;
    int e;
    int p;
};

trip trips[1000];

int N;
int M;

long long int calculate (int o, int e, int p) {
    long long int d = (e - o);
    long long int cost = d*N - (d*(d-1))/2;
    cost = ((cost%MOD) * p) % MOD;

    return cost;
}

long long int calc () {
    long long int total = 0;
    for (int i = 0; i < M; ++i) {
        int e = trips[i].e;
        int o = trips[i].o;
        int p = trips[i].p;

        total = (total + calculate(o, e, p)) % MOD;
    }

    return total;
}

struct point {
    int o;
    int p;
};

long long int cheapest () {
    std::map<int, int> x;
    for (int i = 0; i < M; ++i) {
        int e = trips[i].e;
        int o = trips[i].o;
        int p = trips[i].p;

        x[o] += p;
        x[e] -= p;
    }

    long long int expected_cost = 0;
    std::stack<point> entered;

    for (auto k : x) {
        int o  = k.first;
        int dp = k.second;

        fprintf(stderr, "%d: %d\n", o, dp);

        if (dp < 0) {
            fprintf(stderr, "gotta let go p=%d\n", -dp);
            int c = -dp;

            while (c) {
                point& pt = entered.top();
                int popped = std::min(c, pt.p);

                expected_cost = (expected_cost + calculate(pt.o, o, popped)) % MOD;

                c -= popped;
                pt.p -= popped;

                if (pt.p == 0) {
                    entered.pop();
                }
            }
        }

        if (dp > 0) {
            point more = { o, dp };
            entered.push(more);
            fprintf(stderr, "entering p=%d\n", dp);
        }
    }

    fprintf(stderr, "STACKSIZE: %ld\n", entered.size());

    return expected_cost;
}

void solve (int CASE)
{
    cin >> N >> M;
    for (int i = 0; i < M; ++i) {
        cin >> trips[i].o >> trips[i].e >> trips[i].p;
    }

    long long int real = cheapest();
    long long int expected = calc();
    long long int loss = (expected - real + MOD) % MOD;

    fprintf(stderr, "Expected: %lld\n", expected);
    fprintf(stderr, "Real    : %lld\n", real);
    printf("Case #%d: %lld\n", CASE, loss);
}

int main ()
{
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) solve(i);
  return 0;
}

