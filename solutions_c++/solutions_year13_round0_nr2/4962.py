#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define rp(a,c) fr(a,0,c)
#define fr_(a,b,c) for( int a = b ; a > c ; --a )
#define rp_(a,b) fr_(a,b,-1)

#define cl(a,b) memset((a),(b), sizeof(a))
#define db(x) cerr << #x " == " << x << "\n"
#define _ << ", " <<
#define INF 0x3f3f3f3f

typedef long long 			ll;
typedef unsigned long long 	ull;
typedef vector<int> 		vi;
typedef pair<int,int> 		pii;

#define maxn 0

int n, m, t, ok;
int g[100][100], opa[100][100];
int main(){
	scanf("%d", &t);
	while(t--){
		ok=1;
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d", &g[i][j]);
			}
		}
		cl(opa,0);
		for(int i=0;i<n;i++){
			int s=0;
			for(int j=0;j<m;j++){
				s=max(s,g[i][j]);
			}
			for(int j=0;j<m;j++){
				if(s > g[i][j])opa[i][j]++;
			}
		}
		for(int j=0;j<m;j++){
			int s=0;
			for(int i=0;i<n;i++){
				s=max(s,g[i][j]);
			}
			for(int i=0;i<n;i++){
				if(s > g[i][j])opa[i][j]++;
				if(opa[i][j] == 2)ok=0;
			}
		}
		
		static int caso=1;
		if(ok){
			printf("Case #%d: YES\n", caso++);
		}else printf("Case #%d: NO\n", caso++);
	}
	
	return 0;
}
