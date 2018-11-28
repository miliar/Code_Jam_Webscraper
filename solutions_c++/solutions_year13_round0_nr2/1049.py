#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
const int N = 110;
int s[N][N];
bool flag[N][N];
int n,m;
bool check(int x,int y,int h){
	int cnt=0;
	bool f=1;
	for(int i=1;i<=m&&f;i++)
		if(s[x][i]>h)f=0;
	cnt+=f;
	f=1;
	for(int i=1;i<=n&&f;i++)
		if(s[i][y]>h)f=0;
	cnt+=f;
	return cnt;
}
int main(){
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		int maxn=0;
		scanf("%d%d",&n,&m);
		vector< pair<int,int> >pos[N];
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++){
				scanf("%d",&s[i][j]);
				maxn=max(maxn,s[i][j]);
				pos[s[i][j]].push_back(make_pair(i,j));
			}
		bool ok=1;
		for(int i=1;i<=maxn&&ok;i++){
			for(int j=0;j<pos[i].size()&&ok;j++){
				int x=pos[i][j].first,y=pos[i][j].second;
				ok = check(x,y,i);
			}
		}
		printf("Case #%d: %s\n",cas,ok?"YES":"NO");

	}
	return 0;
}
		
