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

const int MAXN=110;
string G[MAXN],B;

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		int N,L;
		scanf("%d%d",&N,&L);
		for(int i=0;i<N;i++) cin >> G[i];
		cin >> B;
		bool good=1;
		for(int i=0;i<N;i++) 
			if(G[i]==B) {
				good=0;
				break;
			}
		printf("Case #%d: ",num_kase);
		if(!good)
			puts("IMPOSSIBLE");
		else {
			if(L==1) {
				printf("0 ?\n");
			}
			else {
				printf("10?");
				for(int i=0;i<L;i++) printf("10");
				printf(" ");
				for(int i=1;i<L;i++) putchar('?');
				puts("");
			}
		}
	}
	return 0;
}
