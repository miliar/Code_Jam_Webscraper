#include <cstdio>
#include <cstring>
#include <algorithm>
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

bool used[11];
bool a[11][11];
int T,n,ans;

bool Get() {
	char c=getchar();
	while (c!='1' && c!='0') c=getchar();
	return c=='1';
}

bool Dfs2(int k) {
	if (k>n) return true;
	int ret=0;
	bool flag=false;
	for (int i=1;i<=n;++i)
		if (!used[i] && a[k][i]) {
			used[i]=true;
			if (!Dfs2(k+1)) return false;
			used[i]=false;
			flag=true;
		}
	return flag;
}

void Dfs1(int p,int q, int tot) {
	if (p>n) {

		memset(used,0,sizeof(used));
		if (Dfs2(1))
			ans=min(ans,tot);
		return;
	} else
	if (q>n) {
		Dfs1(p+1,1,tot);
	} else {
		if (a[p][q])
			Dfs1(p,q+1,tot);
		else {
			Dfs1(p,q+1,tot);
			a[p][q]=true;
			Dfs1(p,q+1,tot+1);
			a[p][q]=false;
		}
	}
}

int main() {
	freopen("1.in","r",stdin);
	scanf("%d",&T);
	REP(T_T,T) {
		scanf("%d",&n);
		REP(i,n) REP(j,n) a[i][j]=Get();
		ans=n*n;
		Dfs1(1,1,0);
		printf("Case #%d: %d\n",T_T,ans);
	}
	return 0;
}