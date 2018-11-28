#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define FOR(i,f_start,f_end) for(i=f_start;i<f_end;++i)
#define pb push_back
#define mp make_pair

const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

// ========================================================
int T, sum;

int data[1024];

int check(int n, int max) {
    int count = 0;
    F0(i, n) {
        if (data[i] == max ) {
            count++;
        }
    }

    if (count == 2 ) {
        return false;
    }
    return true;
}

void work(int n) {

    int max = 0;
    while ( sum > 0 ) {
        //printf("\n sum :%d", sum);
        printf(" ");
        max = 0;
        //if 2 == sum {
        //    F0(i, n) {
        //        if (data[i])
        //            printf("%c", 'A'+i);
        //    }
        //    sum -= 2;
        //}

        F0(i, n) {
            if (data[i] > max) {
                max = data[i];
            }
        }
        if (true == check(n, max)) {
            F0(i, n) {
                if (max == data[i]) {
                    printf("%c", 'A' + i);
                    data[i]--;
                    sum --;
                    break;
                }
            }
        } else {
            F0(i, n) {
                if (max == data[i]) {
                    printf("%c", 'A' + i);
                    data[i]--;
                    sum --;
                }
            }
        }
    }

}

int main() {
    scanf("%d", &T);
    int m, n;
    F0(caset,T) {
        scanf("%d", &n);
        printf("Case #%d:", caset+1);

        sum = 0;
        F0(i, n) {
            scanf("%d", &data[i]);
            sum += data[i];
        }

        work(n);
        printf("\n");
    }
    return 0;
}
