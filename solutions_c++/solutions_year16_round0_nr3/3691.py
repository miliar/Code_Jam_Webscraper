#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<limits>

using namespace std;

int str[32];
double nonTrivialDiv[9];
int n, j, nRes = 0;

bool areSame(double a, double b) {
    return std::fabs(a - b) < std::numeric_limits<double>::epsilon();
}

bool isPrime(double num, int basei) {
    if(num < 2.0) {
        nonTrivialDiv[basei] = 1.0;
        return false;
    }
    if(areSame(fmod(num, 2.0), 0.0) && !areSame(num, 2.0)) {
        nonTrivialDiv[basei] = 2.0;
        return false;
    }
    if(areSame(fmod(num, 3.0), 0.0) && !areSame(num, 3.0)) {
        nonTrivialDiv[basei] = 3.0;
        return false;
    }
    for(double k = 1; 36 * k * k - 12 * k < num; k += 1) {
        if(areSame(fmod(num, 6 * k + 1), 0.0)) {
            nonTrivialDiv[basei] = 6 * k + 1;
            return false;
        }
        if(areSame(fmod(num, 6 * k - 1), 0.0)) {
            nonTrivialDiv[basei] = 6 * k - 1;
            return false;
        }
    }
    return true;
}

double strInBaseK(int k) {
    double res = 0.0;
    for(int i = 0; i < n; i++)
        if(str[i] == 1)
            res += pow((double)k, n - i - 1);
    return res;
}

void printCoinJam() {
    for(int i = 0; i < n; i++) printf("%d", str[i]);
}

void printNonTrivialDiv() {
    for(int i = 0; i < 9; i++) printf(" %.0f", nonTrivialDiv[i]);
    printf("\n");
}

void findCoinJam(int x) {
    if(x < n) {
        if(x == 0 || x == n - 1) {
            str[x] = 1;
            findCoinJam(x + 1);
        }
        else {
            for(int i = 0; i <= 1; i++) {
                str[x] = i;
                findCoinJam(x + 1);
            }
        }
    }
    else {
        bool isCoinJam = true;
        for(int k = 2; k <= 10; k++) {
            double res = strInBaseK(k);
            if(isPrime(res, k-2)) {
                isCoinJam = false;
                break;
            }
        }
        if(isCoinJam) {
            printCoinJam();
            printNonTrivialDiv();
            ++nRes;
        }
        if(nRes == j) {
            exit(EXIT_SUCCESS);
        }
    }
}

int main() {
    int t;
    scanf("%d%d%d", &t, &n, &j);
    printf("Case #1:\n");
    findCoinJam(0);
    return 0;
}
