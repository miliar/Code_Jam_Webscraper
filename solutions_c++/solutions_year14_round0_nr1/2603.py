#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " : " << x << endl;
#define REP(i,a) for (int i = 0; i < (a); ++i)
#define FOR(i,a,b) for (int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define FOREACH(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define  pb push_back
#define  pu push
#define SA(a,x) memset(a,x,sizeof(a))

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;
typedef pair<int ,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
///////////////////////////////////////////////////////////////////////////

int T,f,s,dump;
int r1[16];
int N,C,ans;



int main()
{
int C = 1;
scanf("%d",&T);
while(T--){	
	N = 0;
	SA(r1,0);

	scanf("%d",&f);
	f--;
	REP(i,4){
		if(i!=f) {
			REP(j,4) scanf("%d",&dump);
		} else {
			REP(j,4) {
				scanf("%d",&dump);
				r1[dump-1]=1;
			}
		}
	}
//	REP(i,16) printf("%d : %d\n",i,r1[i]);
		
	scanf("%d",&s);
	s--;
	REP(i,4){
		if(i!=s) {
			REP(j,4) scanf("%d",&dump);
		} else {
			REP(j,4) {
				scanf("%d",&dump);
				dump--;
	//			DEBUG(dump);
				if(r1[dump]) {
					N++;
					ans = dump;
				}
			}
		}
	}
	printf("Case #%d: ",C++);
	if(N==0)  	printf("Volunteer cheated!\n");
	else if(N==1) printf("%d\n",ans+1);
	else printf("Bad magician!\n");

}
return 0;
}
