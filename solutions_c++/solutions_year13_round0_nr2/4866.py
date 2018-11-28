#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int n,m,a[111][111],r[111],c[111];
void Max(int& a,int b){a=(b>a)?b:a;}
string solve(){
	memset(r,0,sizeof(r));
	memset(c,0,sizeof(c));
	scanf("%d%d",&n,&m);
	rep(i,n) rep(j,m) scanf("%d",&a[i][j]);
	rep(i,n) rep(j,m) Max(r[i],a[i][j]),Max(c[j],a[i][j]);
	rep(i,n) rep(j,m) if (min(r[i],c[j])!=a[i][j]) return "NO";
	return "YES";
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i;
	for(scanf("%d",&T),i=1;i<=T;i++) printf("Case #%d: %s\n",i,solve().c_str());
	return 0;
}
