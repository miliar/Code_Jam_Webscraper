#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
//-----------------------------------------------------------

#define MAXN 22
#define BIT(i) ((ull)1 << (i))

int A[MAXN];
int B[MAXN];
int X[MAXN];
bool used[MAXN];

int N;
bool isfind ;
int LISdp[MAXN];

//回傳LIS長度
int LIS(int LISlen, int* R)
{
	int i, j, ans = 0;
    // 初始化，每一個數字本身就是長度為一的 subsequence
    for (i=0; i<LISlen; i++) LISdp[i] = 1;
    for (i=0; i<LISlen; i++)
        for (j=i+1; j<LISlen; j++)	// 找出能接在 s[i] 後面的數字
            if (R[j] >R[i])		// 若是可以接，長度就增加
                LISdp[j] = max(LISdp[j], LISdp[i] + 1);

    return LISdp[LISlen - 1];
}

void search(int pos){

	if(pos == N){
		int XR[MAXN] = {0};
		memcpy(XR, X, sizeof(X));
		reverse(XR, XR + N);
		for(int i = 0; i < N; i++){
			if(LIS(i + 1, XR) != B[N - i - 1]) return;
		}
		forn(i, N){
			if(i) printf(" ");
			printf("%d", X[i]);
		}
		printf("\n");
		isfind = true;
		return;
	}
	if(isfind) return;

	if(pos == 0){
		// A[0] must be 1
		for(int i = B[0]; i <= N && !isfind; i++){
			X[pos] = i;
			used[i] = true;
			//printf("%d = %d\n", pos, X[pos]);
			search(pos + 1);
			used[i] = false;
		}
	}
	else {
		for(int i = 1; i <= N; i++){
			if(used[i]) continue;
			X[pos] = i;
			if(LIS(pos + 1, X) != A[pos]){
#if 0
				printf("%d = %d (LIS:%d)\n", pos, X[pos], LIS(pos + 1, X));
				forn(i, pos + 1){
					if(i) printf(" ");
					printf("%d", X[i]);
				}
				printf("\n");
#endif
				continue;
			}
			used[i] = true;
			//printf("%d = %d\n", pos, X[pos]);
			search(pos + 1);
			used[i] = false;
		}
	}
}

int main() {
	int cases;
	int casenum = 1;
	freopen("input", "r", stdin);
	//freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		seta(X, 0);
		seta(used, false);
		isfind = false;

		int maxa = 0, maxb = 0;
		scanf("%d", &N);
		forn(i, N) 	{scanf("%d", &A[i]);maxa = max(maxa, A[i]);}
		forn(i, N) 	{scanf("%d", &B[i]);maxb = max(maxb, B[i]);}

		printf("Case #%d: ", casenum++);
		search(0);

		fflush(stdout);

	}
	return 0;
}

