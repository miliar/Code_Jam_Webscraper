//

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#define db(x) cout << #x " == " << x << endl
//#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
#define CL(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef map<int,int> mii;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define ULMAX 0xffffffffffffffffULL
#define y1 Y1

#define N 110
int t,_=1;
int n,m, gr[N][N];

int main() {
//	cin.sync_with_stdio(false);
	for(scanf("%d",&t);t--;){
		scanf("%d%d",&n,&m);
		Fr(i,0,n) Fr(j,0,m) scanf("%d",&gr[i][j]);
		bool resp=1;
		Fr(i,0,n) Fr(j,0,m){
			bool ok=1;
			Fr(k,0,n) ok&= gr[k][j]<=gr[i][j];
			if(!ok){
				ok=1;
				Fr(k,0,m) ok&= gr[i][k]<=gr[i][j];
			}
			resp&=ok;
		}
		
		printf("Case #%d: ",_++);
		if(resp) puts("YES");
		else puts("NO");
	}
	return 0;
}
