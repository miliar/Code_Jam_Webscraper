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
#define rF(a,b,c) for( int a = c-1 ; a >= b ; --a )
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

#define N 5010

int t,a,b,k, cnt[N];


int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%d%d%d",&a,&b,&k);
		CL(cnt,0);
		Fr(i,0,a) Fr(j,0,b) cnt[i&j]++;
		ll resp=0;
		Fr(i,0,k) resp+=cnt[i];
		printf("Case #%d: %lld\n",_++,resp);
	}
	return 0;
}
