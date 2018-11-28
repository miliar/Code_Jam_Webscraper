#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <list>
#include <queue>
#include <ctime>
#include<cstdlib>
#include<cmath>
#include <cstdarg> 
#include <iomanip>

#include<unordered_map>
//#include<unordered_set>
//#include <array>

//#define  NDEBUG
#include <assert.h>

using namespace std;

#define dprint(Exp,...) if(Exp){fprintf(stderr, __VA_ARGS__);}
#define printe(...) fprintf(stderr, __VA_ARGS__);
#define PrtExp(_Exp)  cerr<< #_Exp <<" = "<< (_Exp)
#define PrtExpN(_Exp)  cerr<< #_Exp <<" = "<< (_Exp) <<"\n"

#define SINT(n) scanf("%d",&n);
#define SINT2(n,m) scanf("%d %d",&n,&m);
#define SINT3(n,m,o) scanf("%d %d %d",&n,&m,&o);
#define SINT4(n,m,o,p) scanf("%d %d %d %d",&n,&m,&o,&p);
#define SINT5(n,m,o,p,q) scanf("%d %d %d %d %d",&n,&m,&o,&p,&q);
//#define SLL(n) scanf("%I64d",&n);
#define SLL(n) scanf("%lld",&n);
#define SLL2(n,m) scanf("%lld %lld",&n,&m);
#define SLL3(n,m,o) scanf("%lld %lld %lld",&n,&m,&o);
#define SST(s) scanf("%s",s);
#define SCH(c) scanf("%c",&c);

#define GC() getchar();

#define PINT(n) printf("%d",(int)(n));
#define PINT2(n,m) printf("%d %d",(int)(n),(int)(m));
#define PINT3(n,m,l) printf("%d %d %d",(int)(n),(int)(m),(int)(l));
//#define PLL(n) printf("%I64d",(long long)(n));
#define PLL(n) printf("%lld",(long long)(n));
#define PST(s) printf("%s",(s));
#define PCH(s) printf("%c",(s));

#define PINTN(n) printf("%d\n",(int)(n));
#define PINT2N(n,m) printf("%d %d\n",(int)(n),(int)(m));
#define PINT3N(n,m,l) printf("%d %d %d\n",(int)(n),(int)(m),(int)(l));
//#define PLLN(n) printf("%I64d\n",(long long)(n));
#define PLLN(n) printf("%lld\n",(long long)(n));
#define PSTN(s) printf("%s\n",(s));
#define PCHN(s) printf("%c\n",(s));

#define PSP() printf(" ");
#define PN() printf("\n");

#define PC(c) putchar(c);
#define CSP (' ')
#define SN ("\n")

#define rep(i,a) for(i=0;i<a;i++)
#define reP(i,a) for(i=0;i<=a;i++)
#define Rep(i,a) for(i=a-1;i>=0;i--)
#define ReP(i,a) for(i=a;i>=0;i--)

#define rEp(i,a) for(int i=0;i<a;i++)
#define rEP(i,a) for(int i=0;i<=a;i++)
#define REp(i,a) for(int i=a-1;i>=0;i--)
#define REP(i,a) for(int i=a;i>=0;i--)

#define repft(i,a,b) for(i=a;i<b;i++)
#define repfT(i,a,b) for(i=a;i<=b;i++)
#define Repft(i,a,b) for(i=a-1;i>=b;i--)
#define RepfT(i,a,b) for(i=a;i>=b;i--)



#define foreach(a,it) for(auto it = a.begin(); it != a.end(); ++it)

#define FILL(a,v) fill(begin(a),end(a), v)
#define FILL0(a) memset(a,0,sizeof(a))
#define FILL1(a) memset(a,-1,sizeof(a))

typedef long long ll;
typedef unsigned long ul;
typedef pair<int, int> Pi;
typedef pair<ll, ll>   Pl;
typedef signed char schar;

const int INF = 0x1f1f1f1f;//522,133,279
const ll INFLL = 0x1f1f1f1f1f1f1f1fLL;

template <class A, class B> inline ostream& operator<<(ostream& st, const pair<A, B>& P) { return st << "(" << P.first << "," << P.second << ")"; };

#define prtA(A,st,a) do{int i;rep(i,a){st <<(A[i])<<"\n";}}while(false);
#define prtAi(A,st,a) do{int i;rep(i,a){if(i <= 9){ st << "[ "; } else{ st << "["; }st << i << "] ";st<<(A[i])<<"\n";}}while(false);
#define prtAc(A,st,a) do{int i;rep(i,a){st << ((i%10==0)?((i==0)?"":", "):",") <<(A[i]);}}while(false);
#define prtAw(A,st,a,w) do{int i;rep(i,a){st << ((i%10==0)?((i==0)?"":", "):",") << setw(w)<<(A[i]);}}while(false);

#define prtA2(A,st,b,a) do{int j;rep(j,b){if(j<=9){st << "[ "; } else{st << "[";}st<< j << "] ";prtAc((A[j]),st,a);st<<"\n";}}while(false);
#define prtA2i(A,st,b,a) do{int i,j;rep(j,b){rep(i,a){st <<((j<=9)?"[ ":"[")<<j<<((i<=9)?" ,":",")<<i<<"] "<<(A[j][i])<<"\n";}}}while(false);
#define prtA2c(A,st,b,a) do{int j;rep(j,b){if(j<=9){st << "[ "; } else{st << "[";}st<< j << "] ";prtAc((A[j]),st,a);st<<"\n";}}while(false);
#define prtA2w(A,st,b,a,w) do{int j;rep(j,b){if(j<=9){st << "[ "; } else{st << "[";}st<< j << "] ";prtAw((A[j]),st,a,w);st<<"\n";}}while(false);

#define prtAb(A,st,a) do{int i;rep(i,a){if(i%10==0&&i!=0){st << " ";}st <<((A[i])?"#":".");}}while(false);
#define prtA2b(A,st,b,a) do{int j;rep(j,b){if(j<=9){st << "[ "; } else{st << "[";}st<< j << "] ";prtAb((A[j]),st,a);st<<"\n";}}while(false);

#define prtAn(A,st,a) do{int i;rep(i,a){if(i%10==0&&i!=0){st<<" ";}st<<(((A[i])<1)?(((A[i])<0)?(((A[i])<-1)?'=':'-'):'.'):((A[i])<=9)?(char)((A[i])+'0'):(A[i]<36)?(char)((A[i])-10 +'a'):(A[i]<=300)?((char)((A[i]-1)/10-3+'A')):('#'));}}while(false);
#define prtA2n(A,st,b,a) do{int j;rep(j,b){if(j<=9){st << "[ "; } else{st << "[";}st<< j << "] ";prtAn(A[j],st,a);st<<"\n";}}while(false);



char S[10010];
char memo[10010];


//1,2,3,4 -1,-2,-3,-4
const int calcret[4][4] = {
	{1, 2, 3, 4},
	{2,-1, 4,-3},
	{3,-4,-1, 2},
	{4, 3,-2,-1}
};


int calc(int a, int b) {
	int s = 1;
	//printf("calc %d %d\n", a, b);
	if(a < 0){
		a = -a; s = -s;
	}
	if(b < 0){
		b = -b; s = -s;
	}
	a--; b--;
	return calcret[a][b]*s;
}

int L, X;


int main() {
	int T, t, r, i, j;
	bool f;
	SINT(T);
	repfT(t,1, T) {
		r = 0;
		FILL0(S);
		FILL0(memo);
		f = false;
		
		SINT2(L, X);
		SST(S);

		rep(i, L) {
			S[i] -= ('i'-2);
		}

		repft(i,1, X) {
			rep(j, L) {
				S[i*L + j] = S[j];
			}
		}
		//rep(i, L*X)printe("S[%d]=%d\n", i, S[i]);
		S[L*X] = 0;

		int a = 1,b;

		memo[L*X] = 1;
		Rep(i, L*X) {
			memo[i] = calc(S[i], memo[i + 1]);
		}
		a = 1;

		rep(i, L*X) {
			a = calc(a, S[i]);
			//printf("%d:a=%d\n", i,a);
			if(a == 2){	//i
				//printf("find i at:%d\n", i);
				b = 1;
				repft(j, i+1, L*X) {
					b = calc(b, S[j]);
					//printf("%d:b=%d\n", j, b);
					if(b == 3){
						//printf("find j at:%d\n", j);
						if(memo[j + 1] == 4){

							//printf("find!!\n");
							f = true; break;
						}
					}
				}
				if(f)break;
			}

		}
		

		if(f){
			printf("Case #%d: YES\n", t);
		} else{
			printf("Case #%d: NO\n", t);
		}
		



		//rintf("Case #%d: %d\n", t,r);
	}



	return 0;
}