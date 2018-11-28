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

LL mod = 7420738134810;

LL A[20];

LL interpret(LL c, int b){
	LL r = 0;
	while(c){
		r*=b;
		r+=c&1;
		r=r%mod;
		c/=2;
	}
	return r;
}

bool pr(LL c, int b){
	for(LL m = 2; m*m<=c && m<=40; m++)
		if(c%m==0){
			A[b]=m;
			return true;
		}
	return false;
}

int main(){
	int TC;scanf("%d ",&TC);
	RE(tc,TC){
		printf("Case #%d:\n",tc+1);
		int J,N;scanf("%d %d ",&J,&N);
		int X = 0;
		for(LL a = 0; X<N; a++){
			LL c = (LL)1+((LL)1<<(J-1))+(a<<2);
			bool ok = true;
			for(int b = 2; b<=10; b++)
				if(!pr(interpret(c,b),b)){
					ok = false;
					break;
				}
			if(ok){
				string s;
				while(c){
					s+=(c&1)?'1':'0';
					c/=2;
				}
				assert(s.length()==J);
// 				reverse(s.begin(),s.end());
				printf("%s",s.c_str());
				for(int b = 2; b<=10; b++)
					printf(" %lld",A[b]);
				printf("\n");
				X++;
			}
		}
	}
	return 0;
}
