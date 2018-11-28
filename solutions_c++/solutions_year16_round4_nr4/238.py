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

const int MAXN=30;
char able[MAXN][MAXN];
int N,ans;

int come[MAXN];
bool used[MAXN];

bool check(int l=0) {
	if(l==N)
		return true;
	bool work=0;
	for(int i=0;i<N;i++)
		if(able[come[l]][i]=='1' && !used[i]) {
			work=1;
			used[i]=1;
			if(!check(l+1)) return false;
			used[i]=0;
		}
	if(!work)
		return false;
	return true;
}

bool good() {
	for(int i=0;i<N;i++)
		come[i]=i;
	fill(used,used+N,false);
	do {
		if(!check())
			return false;
	} while(next_permutation(come,come+N));
	return true;
}

void go(int x,int y,int cost) {
	if(y==N) {
		go(x+1,0,cost);
		return;
	}
	if(x==N) {
		if(good())
			ans=min(cost,ans);
		return;
	}
	go(x,y+1,cost);
	if(able[x][y]=='0') {
		able[x][y]='1';
		go(x,y+1,cost+1);
		able[x][y]='0';
	}
}

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%s",able[i]);
		ans=123456789;
		go(0,0,0);
		printf("Case #%d: ",num_kase);
		printf("%d\n",ans);
	}
	return 0;
}
