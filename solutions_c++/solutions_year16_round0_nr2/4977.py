#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#define CL(x,y) memset(x,y,sizeof(x))
#define pb(x) push_back(x)
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(e);i++)
#define x first
#define y second
#define MAX 105
#define INF 1<<29

using namespace std;

int T,TC,N;
bool f[105];
char s[MAX];

void flip(int y){
	for (int i=0;i<=(0+y)/2;i++){
		int j=y-(i-0);
		bool t = !f[i];
		f[i] = !f[j];
		f[j] = t;
	}
}

int check(){
	for (int i=1;i<=N;i++) if (f[i]!=f[i-1]) return i-1;
	return -1;
}

int main(){
	scanf("%d",&T);
	while (T--){
		scanf("%s",s);
		N = strlen(s);
		for (int i=0;i<N;i++) f[i]=s[i]=='+';
		f[N]=true;
		int ans=0,ind;
		while ((ind=check())!=-1) ans++,flip(ind);

		printf("Case #%d: %d\n", ++TC, ans);
	}
}
