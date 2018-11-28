#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;

#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define forl(a,b) for(l = a; l <= b; l++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

long long int powtable[12][50];
bool isPrime[100000000];
int primes[10000000];
int primecount;

long long int getDivisorIfNotPrime(long long int num) {
    long long int i = 2;
    long long int root = (long long int) (sqrt(num));

    for (int i = 0; i < primecount && primes[i] <= root; i++) {
        if (num % primes[i] == 0) {
            return primes[i];
        }
    }
    return -1;
}

void sieveprimes() {
    long long int i, j;
    primecount = 0;
    fori(2, 100000000) {
        isPrime[i] = true;
    }
    fori(2, 100000000) {
        if (isPrime[i]) {
            primes[primecount] = i;
            primecount++;
            for(j = i*i; j <= 100000000LL; j += i) {
                isPrime[j] = false;
            }
        }
    }
    primes[0] = 2;
}

int main() {
    int t, i, n, j, k, l, count, counter;
    sieveprimes();
    scani(t)
    
    //calculate powtable
    fori(2, 10) {
        powtable[i][0] = 1;
        powtable[i][1] = i;
        forj(2, 17) {
            powtable[i][j] = ll(i) * powtable[i][j-1];
        }
    }
    
    fori(1, t) {
        count = 0;
        counter = 0;
        
        scani(n)
        scani(j)
        
        printf("Case #%d:\n", i);
        long long int result[j][10];
        
        char number[n];
        number[0] = number[n-1] = '1';
        number[n] = '\0';
        
        while (count < j) {
            int index = n-2;
            int temp = counter;
            while (counter > 0) {
                int last = counter % 2;
                counter = counter / 2;
                number[index] = '0' + last;
                index--;
            }
            while (index >= 1) {
                number[index] = '0';
                index--;
            }
            
            counter = temp + 1;
            
            bool isPrimeBase = false;
            long long int num;
            fork(2, 10) {
                num = 0LL;
                forl(0, n-1) {
                    num = num + ll(number[l] - '0') * powtable[k][n-1-l];
                }
                int divisor = getDivisorIfNotPrime(num);
                if (divisor == -1) {
                    isPrimeBase = true;
                    break;
                }
                result[count][k-1] = divisor;
            }
            if (!isPrimeBase) {
                result[count][0] = num;
                count++;
            }
        }
        
        fork(0, j-1) {
            forl(0, 9) {
                printf("%lld ", result[k][l]);
            }
            printf("\n");
        }
    }
    return 0;
}