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

const int MAXN=220;

double P[MAXN];

double ans;
int N,K;

bool ch[MAXN];
double res[MAXN];
void go() {
	for(int i=0;i<N;i++)
		res[i]=0;
	res[0]=1;
	for(int i=0;i<N;i++)
		if(ch[i]) {
			for(int k=N;k>0;k--)
				res[k]=res[k-1]*P[i]+res[k]*(1-P[i]);
			res[0]=res[0]*(1-P[i]);
		}
	ans=max(ans,res[K/2]);
}

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		scanf("%d%d",&N,&K);
		for(int i=0;i<N;i++)
			scanf("%lf",P+i);
		sort(P,P+N);
		ans=0.0;
		for(int j=0;j<=K;j++) {
			fill(ch,ch+N,false);
			for(int i=0;i<j;i++)
				ch[i]=1;
			for(int i=N-(K-j);i<N;i++)
				ch[i]=1;
			go();
		}
		printf("Case #%d: ",num_kase);
		printf("%.10f\n",ans);
	}
	return 0;
}
