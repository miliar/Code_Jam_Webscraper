#include <bits/stdc++.h>

using namespace std;
#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

int main(){
	LL test,A[4][4],B[4][4],r1,r2;
	scanf("%lld",&test);
	FORN(t,test){
		scanf("%lld",&r1);r1--;
		FORN(i,4){
			FORN(j,4){
				scanf("%lld",&A[i][j]);
			}
		}
		scanf("%lld",&r2);r2--;
		FORN(i,4){
			FORN(j,4){
				scanf("%lld",&B[i][j]);
			}
		}
		vector < LL > s;
		FORN(i,4){
			FORN(j,4){
				if(A[r1][i]==B[r2][j]){
					s.PB(A[r1][i]);
					break;
				}
			}
		}
		printf("Case #%lld: ",t+1);
		if(SZ(s)>1){
			printf("%s\n","Bad magician!" );
		}
		else if(SZ(s)==1){
			printf("%lld\n",s[0]);	
		}
		else{
			printf("%s\n","Volunteer cheated!");
		}
	}
	return 0;
}