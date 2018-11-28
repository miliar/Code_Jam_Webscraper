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

#define N 20
#define K 230
#define M 1<<N

int t,n,m,start[N],ent[K],ent2[N][K], baus[N][N], cost[N], t1,t2,t3;
map<int,int> mapa;
int mind;
int state[M][N], resp[N], mark[M], caso=0;

void calc(int mask){
	Fr(i,0,mind) state[mask][i]=start[i];
	int tmp=mask;
	for(int i=0; tmp; i++, tmp>>=1) if(tmp&1) {
		Fr(j,0,mind) state[mask][j]+=baus[i][j];
		state[mask][cost[i]]--;
	}
//	printf("Mask: %d\n",mask);
//	Fr(i,0,mind) printf("%d ",state[mask][i]);
//	puts("");
}

bool bt(int mask, int niv){
	if(mark[mask]==caso) return 0;
	if(mask == ((1<<n)-1)) return 1;
	mark[mask]=caso;
	Fr(i,0,n) if(state[mask][cost[i]]){
		resp[niv]=i+1;
		if(bt(mask|(1<<i),niv+1)) return 1;
	}
	return 0;
}

int main() {
//	cin.sync_with_stdio(false);
	int _=1;
	memset(mark,0,sizeof mark);
	for(scanf("%d",&t);t--;){
		scanf("%d%d",&m,&n);
		mapa.clear(); mind=0;
		memset(ent,0,sizeof ent);
		memset(ent2,0,sizeof ent2);
		Fr(i,0,m){
			scanf("%d",&t1);
			ent[t1]++;
		}
		Fr(i,0,n){
			scanf("%d%d",&t1,&t2);
			if(mapa.find(t1)==mapa.end()) mapa[t1]=mind++;
			cost[i]=mapa[t1];
			Fr(j,0,t2){
				scanf("%d",&t3);
				ent2[i][t3]++;
			}
		}
		
		Fr(i,0,K) if(mapa.find(i)!=mapa.end()){
			start[mapa[i]]=ent[i];
			Fr(j,0,n) baus[j][mapa[i]]=ent2[j][i];
		}
		Fr(i,0,1<<n) calc(i);
		
		
		caso++;
		printf("Case #%d:",_++);
		if(bt(0,0)) Fr(i,0,n) printf(" %d",resp[i]);
		else printf(" IMPOSSIBLE");
		puts("");
	}
	return 0;
}
