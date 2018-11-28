#include <cstdio>
#include <cstdlib>
char map[100][101];
bool up[101][101];
bool down[101][101];
bool left[101][101];
bool right[101][101];
int n,m;

int gao(){
	int ans=0;
	bool yes;
	for (int i= 0;i < n;i++) {
		yes =false;
		for (int j=0;j<m;j++) {
			left[i][j]=yes;
			if (map[i][j]!='.')
				yes=true;
		}
		yes = false;
		for (int j=m-1;j>=0;j--) {
			right[i][j]=yes;
			if (map[i][j]!='.') yes=true;
		}
	}
	for (int j=0;j<m;j++) {
		yes =false;
		for (int i=0;i<n;i++) {
			up[i][j]=yes;
			if (map[i][j]!='.') yes=true;
		}
		yes = false ;
		for (int i=n-1;i>=0;i--) {
			down[i][j]=yes;
			if (map[i][j]!='.') yes=true;
		}
	}
	for (int i=0;i<n;i++) {
		for (int j=0;j<m;j++) {
			if (map[i][j]!='.') {
				if ( !left[i][j] && !right[i][j] && !up[i][j] && !down[i][j] ) return -1;
				if ((map[i][j]=='^' && !up[i][j])
						or (map[i][j]=='v' && !down[i][j])
						or (map[i][j]=='<'&& !left[i][j])
						or (map[i][j]=='>'&& !right[i][j]) )
					ans++;
			}
		}
	}
	return ans;
}

int main() {
	int T,i;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) scanf("%s",map[i]);
		int ans=gao();
		printf("Case #%d: ",cs);
		if (ans==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
