#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

int n, k, nho[20], A[5761470];
bool danhdau[100000005];
ll mu[20][20], gt[20];

bool isPrime(int idx, ll n) {
    int k = sqrt(n);
    for (int i = 1; A[i] <= k; ++i)
        if (n%A[i]==0) {
            nho[idx] = A[i];
            return false;
        }
    return true;
}

void init() {
    for (int i = 2; i <= 100000000; ++i) {
        if (danhdau[i]) continue;
        A[++A[0]] = i;
        for (ll j = (ll)i*i; j <= 100000000; j += i)
            danhdau[j] = true;
    }
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	init();
	printf("Case #1:\n");
	scanf("%d",&n);
    scanf("%d%d",&n,&k);
    for (int i = 2; i <= 10; ++i) {
        mu[i][0] = 1;
        for (int j = 1; j <= 16; ++j)
            mu[i][j] = mu[i][j-1]*i;
    }
    int p = 1<<(n-2);
    for (int i = 0; i < p; ++i) {
        for (int j = 2; j <= 10; ++j)
            gt[j] = mu[j][0] + mu[j][n-1];
        for (int j = 0; j < n-2; ++j)
        if ((1<<j)&i) {
            for (int k = 2; k <= 10; ++k)
                gt[k] += mu[k][j+1];
        }
        bool check = true;
        for (int i = 2; i <= 10; ++i)
            if (isPrime(i,gt[i])) {
                check = false;
                break;
            }
        if (check) {
            k--;
            printf("1");
            for (int j = n-3; j >= 0; --j)
                printf("%d",((1<<j)&i)?1:0);
            printf("1 ");
            for (int i = 2; i <= 10; ++i)
                printf("%d ",nho[i]);
            printf("\n");
            if (k==0) return 0;
        }
    }
	return 0;
}
