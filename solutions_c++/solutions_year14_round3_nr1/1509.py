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

int t;
ll a,b, bla, ble;
int resp[1010][1010];

/*
3/4 -> 6/4 -> 2/4+4/4
1/4 -> 2/4 -> 0/4+2/4

123/31488 -> 246/31488
246/31488 -> 492/31488
492/31488
984/31488
1968/31488
3936/31488
7872/31488
15744/31488

1/6 -> 0/6+2/6
2/6 -> 0/6+4/6
4/6 -> 3/6+5/6
5/6 -> 4/6+6/6
fail


0/1 1/1
1/2
1/4 3/4
1/8 3/8 5/8 7/8
1/16

100
001 -> 010
010 -> 100
011 -> 110 -> 010 -> 100

1000
0011 -> 0110 -> 0100+0010

//*/

ll gcd(ll a, ll b){
	while(b) swap(a,b), b=b%a;
	return a;
}

int af(ll a){
	int ret=0;
	while(a)ret++, a-=a&-a;
	return ret;
}

int sacadinha(ll a){
	printf("sac %lld: ",a);
	int ret=0;
	while((a&1LL)==0LL) ret++, a>>=1;
	printf("%d\n",ret);
	return ret;
}

int porraentendierrado(ll a, ll b){
	int ret=0;
	while(a<b) ret++, a<<=1;
	return ret;
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%lld/%lld",&a,&b);
	
		ll g = gcd(a,b);
		a/=g, b/=g;
		
		if(af(b)>1) printf("Case #%d: Impossible\n",_++);
		else {
			int resp=0;
		//	printf("a %lld b %lld\n",a,b);
	
			if(a && b) {
		/*		int xa = sacadinha(a);
				int xb = sacadinha(b);
				resp = xb-1-xa;
				if(resp == 1 && af(a)>1) resp++;//*/
				resp = porraentendierrado(a,b);
			}
			printf("Case #%d: %d\n",_++,resp);
		}
		
		
		//*/
		
	
	//	if(resp[a][b]<=40) printf("Case #%d: %d\n",_++,resp[a][b]);
	//	else printf("Case #%d: Impossible\n",_++);
	}//*/
	return 0;
}
