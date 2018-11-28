#include<cstdio>
#include<algorithm>
#define N 100
using namespace std;
int a[N][N];
int o[N][N];
int main(){
	int t;scanf("%d",&t);
	for(int caso=1;caso<=t;++caso){
		int n,m;scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",a[i]+j),o[i][j]=100;

		for(int r=0;r<n;++r){
			int q=0;
			for(int c=0;c<m;++c)
				q=max(q,a[r][c]);
			for(int c=0;c<m;++c)
				o[r][c]=min(q,o[r][c]);
		}
		for(int c=0;c<m;++c){
			int q=0;
			for(int r=0;r<n;++r)
				q=max(q,a[r][c]);
			for(int r=0;r<n;++r)
				o[r][c]=min(q,o[r][c]);
		}
		bool ok=1;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				ok&=a[i][j]==o[i][j];
		printf("Case #%d: %s\n",caso,(ok)?"YES":"NO");
	}
	return 0;
}
