#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<ctime>
#include<vector>
#include<queue>
#include<stack>
#include<map>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define LD long double
#define pb push_back
#define x first
#define y second
#define PII pair<int,int>
#define PLI pair<LL,int>
#define PIL pair<int,LL>
#define PLL pair<LL,LL>
#define PDD pair<LD,LD>
#define eps 1e-9
#define HH1 402653189
#define HH2 1610612741

int n,j,a[20];

void gen(int x) {
	a[0] = a[n - 1] = 1;
	FOR(i,0,n - 2) 
		a[i + 1] = (x & (1 << i)) > 0;
	reverse(a,a + n);
}

LL num(int x) {
	LL ret = 0;
	FOR(i,0,n) ret = ret * x + a[i];
	return ret; 
}

int main () {
	
	scanf("%d%d",&n,&j);
	
	n /= 2;
	
	printf("Case #1:\n");
	
	FOR(i,0,j) {
		gen(i);
		FOR(i,0,n) printf("%d",a[i]);
		FOR(i,0,n) printf("%d",a[i]);
		FOE(i,2,10) printf(" %lld",num(i));
		printf("\n");
	}
	
	return 0;
}

