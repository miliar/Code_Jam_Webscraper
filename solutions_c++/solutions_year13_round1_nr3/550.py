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

#define N 15

int t,r,n,m,k;
int resp[N],ns[N];

bool checa(int prod){
	Fr(i,0,1<<n){
		int p=1;
		Fr(j,0,n) if(i&(1<<j)) p*=resp[j];
		if(p==prod) return 1;
	}
	return 0;
}

bool test(){
	Fr(i,0,k) if(!checa(ns[i])) return 0;
	return 1;
}

bool bt(int niv){
	if(niv==n) return test();
	Fr(i,2,m+1){
		resp[niv]=i;
		if(bt(niv+1)) return 1;
	}
	return 0;
}

void blah(){
	memset(resp,0,sizeof resp);
	if(bt(0)) return;
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	for(scanf("%d",&t);t--;){
		scanf("%d%d%d%d",&r,&n,&m,&k);
		printf("Case #%d:\n",_++);
		Fr(i,0,r){
			Fr(j,0,k) scanf("%d",&ns[j]);
	//		puts("KAJ");
			blah();
			Fr(j,0,n) printf("%d",resp[j]);
			puts("");
		}
	}
	return 0;
}
