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

#define dbg if(0)

ll PA(ll start,ll qts){
dbg	printf("%lld %lld %lld\n",start,(start+((qts-1)<<2)),qts);
	return ((start+(start+((qts-1)<<2)))*qts)>>1;
}

ll calc(ll raio, ll qts){
	ll start=raio*raio;
	ll ret = start;
	ll dif = (raio+1LL)*(raio+1LL) -start;
	ret+=PA(dif,(qts-1)<<1);
	return ret;
}

int t;
ll r,p;

bool f(ll m){
	m++;
	ll start = m + (r<<1);	//raio do que não consegue
	ll tot = (r<<1)+1LL;
	if((LINF/tot) < m) return 0;
dbg	printf("test %lld %lld (%lld)\n",tot,m,PA(tot,m));
	return PA(tot,m)<=p;
}

int main() {
//	cin.sync_with_stdio(false);

//	while(scanf("%lld%lld",&r,&p)==2) printf("%lld\n",PA(r,p));

/*	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%lld%lld",&r,&p);
		ll resp=0;
		ll at=r, tot=0;
		while(tot<p){
			tot+=(at+1LL)*(at+1LL) - at*at;
			printf("(%lld %lld) tot %lld\n",(at+1LL)*(at+1LL),at*at,tot);
			if(tot<=p) resp++;
			at+=2LL;
		}
		printf("Case #%d: %lld\n",_++,resp);
	}//*/

	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%lld%lld",&r,&p);
		
		ll ini = 0, fim = INF;
		while(ini<fim){
			ll meio=(ini+fim)>>1;
			if(f(meio)) ini=meio+1LL;
			else fim=meio;
		}
		
		printf("Case #%d: %lld\n",_++,ini);
	}//*/
	return 0;
}
