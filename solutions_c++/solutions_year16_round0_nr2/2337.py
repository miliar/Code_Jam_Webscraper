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

int TC,ans,n;
FILE *OUT;
char s[155];

int main (int argc, char** argv) {
	
	OUT = fopen(argv[1],"w"); 
	
	scanf("%d",&TC);
	
	FOE(ttt,1,TC) {
		
		
		ans = 0; int tmp = 0;
		
		
		printf("Working on Case #%d...\n",ttt);
		
		
		scanf("%s",s);
		n = strlen(s);
		
		int p = n - 1;
		while (p >= 0 && s[p] == '+') p--;
		
		if (p >= 0) 
			FOE(i,0,p) ans += s[i] != s[i-1];
		
		
		fprintf(OUT,"Case #%d: %d\n",ttt,ans);
		// be careful with the datatype  ^^^^^^^
	}
	
	return 0;
}

