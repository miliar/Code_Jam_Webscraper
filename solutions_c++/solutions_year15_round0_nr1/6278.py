#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<ctime>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define pb push_back

int T,N,A[1055];

bool test() {
	int C=A[0];
	FOE(i,1,N) {
		if (C>=i) C+=A[i];
		else return 0;
	}
	return 1;
}

int main () {
	
	scanf("%d",&T);
	
	FOE(tc,1,T) {
		scanf("%d",&N);
		FOE(i,0,N) scanf("%1d",A+i);
		FOE(i,0,N) {
			if (test()) {
				printf("Case #%d: %d\n",tc,i);
				break;
			}
			A[0]++;
		}
	}
	
	return 0;
}

