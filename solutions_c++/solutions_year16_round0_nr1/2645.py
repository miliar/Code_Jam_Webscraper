#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cassert>
using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii > vii;
typedef queue<int> qi;
typedef set<int> si;

#define RE(i,b) for(int i=0; i<(int)(b); i++)
#define REP(i,a,b) for(int i=(a); i<(int)(b); i++)
#define BREP(i,a,b) for(int i=(a)-1; i>=(b); i--)
#define FE(i,X) for(typeof((X).begin()) i=(X).begin(); i!=(X).end(); ++i)

#define INF 1000000000
#define MP make_pair
#define FI first
#define SE second

int main(){
	int TC;scanf("%d ",&TC);
	RE(tc,TC){
		printf("Case #%d: ",tc+1);
		int N;
		scanf("%d ",&N);
		if(N==0){
			printf("INSOMNIA\n");
			continue;
		}
		int X = 0;
		bool A[10];
		fill_n(A,10,0);
		for(LL a = N; ;a+=N){
			LL b = a;
			while(b){
				X+=!A[b%10];
				A[b%10]=true;
				b/=10;
			}
			if(X==10){
				printf("%lld\n",a);
				break;
			}
		}
	}
	return 0;
}
