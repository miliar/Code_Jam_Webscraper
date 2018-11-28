#include <bits/stdc++.h>
#define REP(a,b) for(int a=0; a<(b); ++a)
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define FWDS(a,b,c,d) for(int a=(b); a<(c); a+=d)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define ALL(a) (a).begin(), (a).end()
#define SIZE(a) ((int)(a).size())
#define VAR(x) #x ": " << x << " "
#define popcount __builtin_popcount
#define popcountll __builtin_popcountll
#define gcd __gcd
#define x first
#define y second
#define st first
#define nd second
#define pb push_back

using namespace std;

template<typename T> ostream& operator<<(ostream &out, const vector<T> &v){ out << "{"; for(const T &a : v) out << a << ", "; out << "}"; return out; }
template<typename S, typename T> ostream& operator<<(ostream &out, const pair<S,T> &p){ out << "(" << p.st << ", " << p.nd << ")"; return out; }

typedef long long int64;
typedef pair<int, int> PII;
typedef long double dd;
typedef vector<int> VI;

const int dx[] = {0,0,-1,1}; //1,1,-1,1};
const int dy[] = {-1,1,0,0}; //1,-1,1,-1};

int n;
int sk[26];
int nsk[26];
char buff[33];
int ord[26];
bool dp[(1<<17)+3];
bool ndp[(1<<17)+3];

bool enough(){
	//printf("checking\n");
	//FWD(i,0,n) printf("%d\n", nsk[i]);
	FWD(i,0,n) ord[i] = i;
	do{
		//printf("new order\n");
		FWD(i,0,(1<<n)) dp[i] = 0;
		dp[0] = 1;
		FWD(_i,0,n){
			int i = ord[_i];
			//printf("%d\n", i);
			FWD(mask,0,(1<<n))
				if(dp[mask] && (nsk[i]&(~mask)) == 0)
					return 0;
			FWD(mask,0,(1<<n))
				ndp[mask] = 0;
			FWD(mask,0,(1<<n))
				if(dp[mask])
					FWD(j,0,n)
						if(nsk[i]&(1<<j))
							ndp[mask|(1<<j)] = 1;
			FWD(mask,0,(1<<n))
				dp[mask] = ndp[mask];
			//FWD(mask,0,(1<<n))
			//	if(dp[mask])
			//		printf("	%d\n", mask);
		}
	}while(next_permutation(ord, ord+n));
	return 1;
}

void solve(){
	scanf("%d", &n);
	FWD(i,0,n){
		scanf("%s", buff);
		sk[i] = 0;
		FWD(j,0,n)
			sk[i] = 2*sk[i] + buff[j]-'0';
	}
	int res = n*n;
	FWD(learn,0,(1 << (n*n))){
		FWD(i,0,n)
			nsk[i] = (sk[i] | ((learn>>(i*n))&((1<<n)-1)));
		if(enough())
			res = min(res, popcount(learn));
	}
	printf("%d\n", res);
}

int main(){
	int zzz;
	scanf("%d", &zzz);
	FWD(zz,1,zzz+1){
		printf("Case #%d: ", zz);
		solve();
	}
	return 0;
}
