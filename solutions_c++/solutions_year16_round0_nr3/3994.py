#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

int N, J;

typedef long long ll;

const int pn = 10000000;
int mark[pn+1],prime[pn+1],cnt; // mark[i]代表i的最小素因子，prime[i]代表第i个素数
void Get_Prime(int n=pn){
	memset(mark,0,sizeof(mark));
	cnt = 0;
	for(int i=2; i<=n; i++){
		if(!mark[i]) mark[i] = prime[cnt++] = i;
		for(int j=0; j<cnt&&prime[j]*i<=n; j++){
			mark[i*prime[j]] = prime[j];
			if(i%prime[j] == 0) break;
		}
	}
}

ll getn(int n, int m) {
    ll res = 0;
    for(ll i = 1, j = 1; i <= 1 << 16; i <<= 1, j *= m) {
        if(n & i) res += j;
    }
    return res;
}

ll r[12];

bool isPrime(ll n, int m) {
    for(ll i = 2; i <= sqrt(n); i++) {
        if(n % i == 0) {
            r[m] = i;
            return false;
        }
    }
    return true;
}

int main() {
    //Get_Prime();
    int T;
    scanf("%d",&T);
    int cs =1;
    while(T--) {
        scanf("%d %d",&N, &J);
        printf("Case #%d:\n",cs++);
        for(int i = (1 << (N-1)) + 1; i < (1 << N); i+=2) {
                //printf("\ni=%d\n",i);
            memset(r, 0, sizeof(r));
            for(int j = 2; j <= 10; j++) {

                    //printf("----getn(i,j)=%I64d\n",getn(i,j));
            //for(int j = 2; j <= 10; j++) printf(" %I64d", r[j]);
                //printf("\n");

                if(isPrime(getn(i,j),j)) break;
            }
//        for(int j = 1 << (N-1); j; j >>= 1) {
//                    if(j & i) printf("1");
//                    else printf("0");
//                }
//                for(int j = 2; j <= 10; j++) printf(" %I64d", r[i]);
            if(r[10]) {
                J--;
                for(int j = 1 << (N-1); j; j >>= 1) {
                    if(j & i) printf("1");
                    else printf("0");
                }
                for(int j = 2; j <= 10; j++) printf(" %I64d", r[j]);
                printf("\n");
            }
            if(!J) break;
        }
    }
    return 0;
}
