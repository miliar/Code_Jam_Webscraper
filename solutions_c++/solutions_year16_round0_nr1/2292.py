#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<ctime>
#include<vector>
#include<queue>
#include<stack>
#include<map>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define LD long double
#define pb push_back
#define x first
#define y second
#define PII pair<int,int>
#define PLI pair<LL,int>
#define PIL pair<int,LL>
#define PLL pair<LL,LL>
#define PDD pair<LD,LD>

int TC,ans,n,cnt[10];
FILE *OUT;

void update(int x) {
	while (x) {
		cnt[x % 10]++;
		x /= 10;
	}
}

bool ok(int x) {
	FOE(i,0,9) if (!cnt[i]) return 0;
	return 1;
}

int main (int argc, char** argv) {
	
	OUT = fopen(argv[1],"w"); 
	
	scanf("%d",&TC);
	
	FOE(ttt,1,TC) {
		
		
		ans = -1; 
		SET(cnt,0);
		
		
		printf("Working on Case #%d...\n",ttt);
		
		
		scanf("%d",&n);
		FOE(i,1,1000) {
			update(i * n);
			if (ok(i * n)) {
				ans = i * n;
				break;
			}
		}
		
		
		fprintf(OUT,"Case #%d: ",ttt);
		if (ans == -1)
			fprintf(OUT,"INSOMNIA\n");
		else
			fprintf(OUT,"%d\n",ans);
		
	}
	
	return 0;
}

