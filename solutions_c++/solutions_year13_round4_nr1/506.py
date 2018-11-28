#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define ph() push_heap(heap.begin(),heap.end(),comp);
#define poph() pop_heap(heap.begin(),heap.end(),comp);

#define MOD 1000002013

vector< pii > heap;

bool comp(pii a, pii b){
	return a.X<b.X;
}

int T,N,M;
int o,e,p;

pii getin[1005];
pii getout[1005];
int pi1,pi2;
ll prevcost;
ll cost;
ll dist;

int main(){
	int t,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		prevcost = cost = 0;
		heap.clear();
		scanf("%d%d",&N,&M);
		for(i=0;i<M;i++){
			scanf("%d%d%d",&o,&e,&p);
			getin[i]=mp(o,p);
			getout[i]=mp(e,p);
			dist = e-o;
			prevcost = (prevcost + (p*((dist*(2*N-dist+1)/2)%MOD)%MOD))%MOD;
		}
		sort(getin,getin+M);
		sort(getout,getout+M);
		pi1 = pi2 = 0;
		while(pi1<M || pi2<M){
			if((pi1<M && pi2<M && getin[pi1].X<=getout[pi2].X) || (pi2>=M && pi1<M)){
			//printf("vstupuji 1: (pi1,pi2): %d %d\n",pi1,pi2);
				heap.pb(getin[pi1]);
				ph();
				pi1++;
				continue;
			}
			if((pi1<M && pi2<M && getin[pi1].X>=getout[pi2].X) || (pi1>=M && pi2<M)){
				//printf("(pi1,pi2): %d,%d, cost %lld, heap[0]: %d,%d\n",pi1,pi2,cost,heap[0].X,heap[0].Y);
				while(getout[pi2].Y>heap[0].Y){
					dist = getout[pi2].X-heap[0].X;
					cost = (cost+((ll)heap[0].Y*(dist*(2*N-dist+1)/2)%MOD)%MOD)%MOD;
					getout[pi2].Y-=heap[0].Y;
					poph();
					heap.popb();
				}
				dist = getout[pi2].X-heap[0].X;
				cost = (cost+((ll)getout[pi2].Y*(dist*(2*N-dist+1)/2)%MOD)%MOD)%MOD;
				heap[0].Y-=getout[pi2].Y;
				pi2++;
			}
		}
		//printf("%lld %lld\n",prevcost,cost);
		printf("Case #%d: %lld\n",t,(prevcost-cost+MOD)%MOD);

	}

	return 0;
}
