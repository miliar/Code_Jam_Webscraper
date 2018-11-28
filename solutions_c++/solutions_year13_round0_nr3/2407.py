#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define LL long long

const int MAXN = 50;

LL p[MAXN]={
  1
, 4
, 9
, 121
, 484
, 10201
, 12321
, 14641
, 40804
, 44944
, 1002001
, 1234321
, 4008004
, 100020001
, 102030201
, 104060401
, 121242121
, 123454321
, 125686521
, 400080004
, 404090404
, 10000200001
, 10221412201
, 12102420121
, 12345654321
, 40000800004
, 1000002000001
, 1002003002001
, 1004006004001
, 1020304030201
, 1022325232201
, 1024348434201
, 1210024200121
, 1212225222121
, 1214428244121
, 1232346432321
, 1234567654321
, 4000008000004
, 4004009004004
, 100000020000001
};


int main(){
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);
	
	int T, cases;
	LL A, B;
	int res;
	
	scanf("%d", &T);
	for(cases=1; cases<=T; ++cases){
		scanf("%lld %lld", &A, &B);
		res = 0;
		for(int i=0; i<MAXN; ++i){
			if(p[i]>=A && p[i]<=B) res++;
			if(p[i]>B) break;
		}
		printf("Case #%d: %d\n", cases, res);
	}
	
	return 0;
}
