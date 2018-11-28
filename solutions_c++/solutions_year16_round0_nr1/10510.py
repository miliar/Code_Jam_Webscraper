#include <bits/stdc++.h>
using namespace std;

#define REP(I, N) for(int I=0; I<(N); ++I)
#define REP1(I, N) for(int I=1; I<=(N); ++I)
#define REPP(I, A, B) for(int I=(A); I<(B); ++I)
#define REPR(I, N) for(int I=N-1; I>=0; --I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int X; scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define MP make_pair
#define PB push_back
#define MSET(x, y) memset(x, y, sizeof(x))
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> pii;

/***************************************************************/

bool num[10] = {0};


bool isSaw(int n){
	bool flg = true;
	while( n > 0 ){
		num[n%10] = true;
		n /= 10;
	}
	for( int i = 0 ; i < 10 ; i++)
		if ( !num[i] ){
			flg = false;
			break;
		}
	return flg;
}

int main() {
	//freopen("a.in", "r", stdin);
	FILE *fptr = freopen("a.ans", "w", stdout);
	int t , n;
	scanf("%d",&t);
	for( int k = 1 ; k <= t ; k++ ){
		scanf("%d",&n);
		memset(num,0,sizeof(num));
		bool isgood = false;
		for( int i = 2 , tmp = n ; i < 100 ; i++ ){
			if ( isSaw(n) ){
				isgood = true;
				break;
			}
			n = i * tmp % 1000000000;
		}
		if ( isgood ){
			fprintf(fptr,"Case #%d: %d\n",k,n);
		}
		else{
			fprintf(fptr,"Case #%d: INSOMNIA\n",k);
		}
	}
	
	return 0;
}

