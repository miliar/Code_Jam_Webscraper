#include <cstdio>
#include <cstring>

// for large problem set
const int MAX_COUNT = 1001;
const int MAX_N = 100000001;

// countTestCases should be less or equal to 100
int countTestCases = 0;

int cutTime[MAX_COUNT];
int serveCount[MAX_N];

void init() {
    memset(cutTime, 0, sizeof(int) * MAX_COUNT);
}

int getMinCutTime(int countBarber) {
    int minCutTime = MAX_N;
    for (int i = 0; i < countBarber; ++i) {
        if (minCutTime > cutTime[i]) {
            minCutTime = cutTime[i];
        }
    }

    return minCutTime;
}

void swap(int &a, int &b) {
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int gcd(int a, int b)
{
    if (a < b)
        swap(a, b);

    if (b == 0)
        return a;
    else
        return gcd(b, a%b);
}


int ngcd(int *a, int n)
{
    if (n == 1)  return *a;

    return gcd(a[n-1], ngcd(a, n-1));
}


//lcm(a, b) = a*b/gcd(a, b)
int lcm(int a, int b)
{
    return a*b/gcd(a, b);
}

int nlcm(int *a, int n)
{
    if (n == 1)
        return *a;
    else
        return lcm(a[n-1], nlcm(a, n-1));
}

int solve(int countBarber, int n) {

    const int minCutTime = getMinCutTime(countBarber);
    int countTotalServedCustomer = countBarber;

    if (n <= countBarber) {
        return n;
    }

    const int lcm = nlcm(cutTime, countBarber);

    // calculate how many customers could be served during a fixed time
    for (int i = 1; i < lcm; ++i) {
        for (int j = 0; j < countBarber; ++j) {
            if (i % cutTime[j] == 0) {
                ++countTotalServedCustomer;

                if (countTotalServedCustomer >= n) {
                    //printf("Return countTotalServedCustomer = %d lcm=%d\n", countTotalServedCustomer, lcm);
                    return j + 1;
                }
            }
        }
    }

    n %= countTotalServedCustomer;
    int newServed = countBarber;
    //printf("n=%d, newServed = %d, totalServed = %d, lcm=%d\n", n, newServed, countTotalServedCustomer, lcm);
    if (n <= newServed) {
        if (n == 0) {
            int lastBarber = countBarber;

            for (int i = 1; i < lcm; ++i) {
                for (int j = 0; j < countBarber; ++j) {
                    if (i % cutTime[j] == 0) {
                        lastBarber = j + 1;
                    }
                }
            }

            return lastBarber;
        } else {
            return n;
        }
    }

    newServed = countBarber;
    for (int i = 1; i < lcm; ++i) {
        for (int j = 0; j < countBarber; ++j) {
            if (i % cutTime[j] == 0) {
                ++newServed;

                if (newServed >= n) {
                    return j + 1;
                }
            }
        }
    }

    return 0;
}

int main() {

    init();

    scanf("%d", &countTestCases);

    int i = 0;

    for ( ; i < countTestCases; ++i) {
        int countBarber = 0;
        int n = 0;

        scanf("%d %d", &countBarber, &n);

        for (int j = 0; j < countBarber; ++j) {
            scanf("%d", &cutTime[j]);
        }

        printf("Case #%d: %d\n", i + 1, solve(countBarber, n));
    }

    return 0;
}
