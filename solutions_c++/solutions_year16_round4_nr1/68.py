#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

int tt;
int p,r,s,n;
string ans[13][3]; //psr
int res[13][3][3]; 

void gen() {
	memset(res,0,sizeof(res));
	res[0][0][0]=1;
	res[0][1][1]=1;
	res[0][2][2]=1;
	ans[0][0]="P";
	ans[0][1]="S";
	ans[0][2]="R";
	for (int i=1;i<=12;++i) {
		for (int j=0;j<3;++j) {
			res[i][0][j]=res[i-1][0][j]+res[i-1][2][j];
			res[i][1][j]=res[i-1][0][j]+res[i-1][1][j];
			res[i][2][j]=res[i-1][1][j]+res[i-1][2][j];
		}
		ans[i][0]=min(ans[i-1][0]+ans[i-1][2],ans[i-1][2]+ans[i-1][0]);
		ans[i][1]=min(ans[i-1][0]+ans[i-1][1],ans[i-1][1]+ans[i-1][0]);
		ans[i][2]=min(ans[i-1][1]+ans[i-1][2],ans[i-1][2]+ans[i-1][1]);
	}
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);

	gen();
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d%d%d",&n,&r,&p,&s);
		printf("Case #%d: ",ii);
		bool flag=false;
		for (int j=0;j<3;++j)
			if (res[n][j][0]==p && res[n][j][1]==s && res[n][j][2]==r) {
				cout << ans[n][j] << endl;
				flag=true;
			}
		if (!flag) cout << "IMPOSSIBLE\n";
	}
}