#include <bits/stdc++.h>

using namespace std;
// Constants and macros
#define INF 		(int)1e9
#define EPS 		1e-9
#define bitcount 	__builtin_popcount
#define gcd 		__gcd
#define forall(i,a,b) 	for(int i=a;i<b;i++)
#define pb 		push_back
#define mp		make_pair
#define MAX(a,b)	( (a)>(b) ? (a):(b))
#define MIN(a,b)	( (a)<(b) ? (a):(b))
#define s(a)		scanf("%d", &a)
#define ss(a,b)		scanf("%d %d", &a,&b)
#define sss(a,b,c)	scanf("%d %d %d", &a,&b,&c)
#define sl(a)		scanf("%I64d", &a)

int T;
string s;

int main(){
	s(T);
	forall(i,0,T){
		cin >> s;
		vector<int> pc;
		int flip = 0;
		int last = -1;
		forall(i,0, (int) s.length()){
			int p = -1;
			if (s[i] =='+')
				p = 1;
			else if (s[i] =='-')
				p  = 0;
			if (p!=-1 && p!= last){
				last = p;
				pc.pb(p);
			}
		}
		if (pc[0] == 0) flip --;
		forall(i,0, (int) pc.size()){
			if (pc[i] ==0) flip +=2;
		}
		printf("Case #%d: %d\n", i+1, flip);
	}
}
