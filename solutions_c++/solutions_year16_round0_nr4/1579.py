
#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

#define pcase(tt)  printf("Case #%d: ", tt)
#define mem(arr,val) memset(arr,val,sizeof arr)
#define loopi(i,val,n) for(i=val;i<=n;i++)
#define loopd(i,val,val2) for(i=val;i>=val2;i--)
#define sz(vec) (int)vec.size()
#define print3(n,m,l) out << n<<" "<<m<< " "<<l<<endl


#define 		mem(arr,val) 						memset(arr,val,sizeof arr)
#define 		FOR(i,val,n) 						for(i=val;i<=n;i++)
#define 		FORD(i,val,val2) 					for(i=val;i>=val2;i--)
#define			iterate(it,data_structure)			for(it=data_structure.begin();it!=data_structure.end();it++)

#define		 	sz(vec) 			(int)vec.size()
#define 		sc(n) 				scanf("%d",&n)
#define 		scl(n) 				scanf("%I64d",&n)
#define 		sc2l(n, m) 			scanf("%I64d %I64d",&n, &m)
#define 		sc8l(n, m, a, b, c, d, e, f) 			scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n, &m, &a, &b, &c, &d, &e, &f)
#define 		sc2(n,m) 			scanf("%d %d",&n,&m)
#define 		sc3(n,m,x) 			scanf("%d %d %d",&n,&m,&x)
#define 		sc3l(n,m,x) 		scanf("%I64d %I64d %I64d",&n,&m,&x)
#define			sc4(n,m,x,y) 		scanf("%d %d %d %d",&n,&m,&x,&y)
#define 		println(n) 			printf("%d\n",n)
#define 		printlnl(n) 		printf("%I64d\n",n)
#define 		line() 				printf("\n")
#define 		print(n) 			printf("%d",n)
#define 		prints(s)			printf("%s",s)
#define			pb					push_back
//#define			mp					make_pair
#define			F					first
#define			S					second
#define 		Map					unordered_map

typedef vector<int> vi;
typedef pair<int, int> pr;
typedef vector<pr> vpr;

#define 		INF 				2000000000
#define 		INFL 				1000000000000000000LL
#define 		EPS 				0.0000001


const char* fin[] = { "a.txt", "b.txt", "c.txt", "d.txt" };
const char* fout[] = { "a.out", "b.out", "c.out", "d.out" };
const int IDX = 3;


int main() {
	freopen(fin[IDX], "r", stdin);
	freopen(fout[IDX], "w", stdout);

	int TC, K, C, S;
	sc(TC);
	for (int tt = 1; tt <= TC; tt++) {
		sc3(K,C,S);
		pcase(tt);

		printf("1");
		for(int i = 2; i<= S; i++){
			printf(" %d", i);
		}
		line();
	}
	return 0;
}

