// Only for small
#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MAXN=1050;

struct PT {
	int x,y,z;
}p[MAXN],v[MAXN];

double dis(const PT& a,const PT& b) {
	int dx=abs(a.x-b.x);
	int dy=abs(a.y-b.y);
	int dz=abs(a.z-b.z);
	int sum=dx*dx+dy*dy+dz*dz;
	return sqrt((double)sum);
}

const double INF=1e10;
double re[MAXN];
int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		int N,S;
		scanf("%d%d",&N,&S);
		for(int i=0;i<N;i++)
			scanf("%d%d%d%d%d%d",&p[i].x,&p[i].y,&p[i].z,&v[i].x,&v[i].y,&v[i].z);
		for(int i=0;i<N;i++) re[i]=INF;
		re[0]=0;
		bool done[MAXN]={0};
		while(1) {
			int t=-1;
			for(int i=0;i<N;i++)
				if(!done[i] && (t==-1 || re[i]<re[t]))
					t=i;
			done[t]=1;
			if(t==-1) break;
			for(int i=0;i<N;i++)
				re[i]=min(re[i],max(re[t],dis(p[t],p[i])));
		}
		printf("Case #%d: ",num_kase);
		printf("%.10f\n",re[1]);
	}
	return 0;
}
