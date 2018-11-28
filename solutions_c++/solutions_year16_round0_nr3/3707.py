#include <iostream>
#include <cstdio>
#include <list>
#include <cmath>
using namespace std;

int n,db;
int primes[17200000];
int pcount = 0;

int solcount = 0;

bool test[16];
void printTest() {
    for (int i = 0; i<n; i++) printf("%c", test[i] ? '1' : '0');
}




bool isPrime(int x) {
    int limit = sqrt(x);
    int i = 0;
    while (i < pcount && primes[i] <= limit) {
        if (x % primes[i] == 0) return false;
        i++;
    }
    return true;
}
int getDivisor(long long x) {
    int limit = (int)(sqrt(x));
    int i = 0;
    while (i < pcount && primes[i] <= limit) {
        if (x % (long long)(primes[i]) == 0) return primes[i];
        i++;
    }
    return -1;
}

int checkSolInBase(int b) {
    long long num = (long long)0;
    for (int i = 0; i<n; i++) {
        num *= (long long)b;
        if (test[i]) num += (long long)1;
    }
    return getDivisor(num);
}

void checkSol() {
    int sols[11];
    for (int i = 2; i<=10; i++) {
        sols[i] = checkSolInBase(i);
        if (sols[i] == -1) return;
    }
    printTest();
    for (int i = 2; i<=10; i++) printf(" %d", sols[i]);
    printf("\n");
    solcount++;
}

void bt(int k) {
    if (solcount == db) return;
    if (k == n-1) { checkSol(); return; }

    test[k] = false;
    bt(k+1);
    test[k] = true;
    bt(k+1);
}



int main()
{
    //freopen("in.txt", "r", stdin);
    scanf("1\n%d %d", &n, &db);

    //n=16; db=50;

    int ub = 317000000;
    for (int i = 2; i<ub; i++) {
        if (isPrime(i)) primes[pcount++] = i;
        //if (i % 1000000 == 0) printf("%d\n", i);
    }
    printf("Case #1:\n");

    test [0] = true;
    test [n-1] = true;

    bt(1);

    return 0;
}
