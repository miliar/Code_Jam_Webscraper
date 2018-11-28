#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define FOREACH(I,A)  for(__typeof(A.begin()) I = A.begin(); I != A.end(); ++I)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAIN(A,X)  (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong Infinity = 1000000100;
const ldouble Epsilon = 1e-9;




bool check(vector<int> X){
	
}

vector<int> V[80];

int O[80];
void dfs(int a, int &x, int &y){
	O[a] = 1;
	x++;
	for(int v : V[a]) if(!O[v]) dfs(v,y,x);
}

void test(){
	int n;
	scanf("%d",&n);
	FOR(i,1,n*2){
		V[i].clear();
		O[i] = 0;
	}
	int k = 0;
	FOR(i,1,n){
		FOR(j,1,n){
			char c;
			scanf(" %c", &c);
			if(c == '1'){
				V[i].PB(j+n);
				V[j+n].PB(i);
				k++;
			}
		}
	}

	vector<pair<int,int> > X;
	int ans = 0;
	FOR(i,1,n*2){
		if(!O[i]){
			int a=0,b=0;
			dfs(i,a,b);
			if(a == b) {
				ans += a*b;
				continue;
			}
			if(i <= n) X.PB({a,b});
			else X.PB({b,a});
		}
	}
	sort(ALL(X));
	int ans2 = 1000000;

	do{
		int tmp = 0;
		int a=0,b=0;
		for(auto x : X){
			a += x.X;
			b += x.Y;

			if(a == b){
				tmp += a*a; 
				a=0;
				b=0;
			}
		}
		ans2 = min(tmp,ans2);
	}while(next_permutation(ALL(X)));
	printf("%d\n", ans2+ans-k);

}

int main(){
	int T;
	scanf("%d",&T);
	FOR(i,1,T){
		printf("Case #%d: ", i);
		test();
	}
}
