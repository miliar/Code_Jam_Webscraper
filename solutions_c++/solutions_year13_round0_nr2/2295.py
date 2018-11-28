#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int n,m,a[105][105],b[105][105];

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				scanf("%d",&a[i][j]);
				b[i][j]=100;
			}
		}
		bool change=true;
		while (change){
			change=false;
			for (int i=0;i<n;++i){
				int mini=-1;
				for (int j=0;j<m;++j){
					mini=max(a[i][j],mini);
				}
				bool ok=true;
				for (int j=0;j<m;++j){
					if (mini>b[i][j]){
						ok=false;
					}
				}
				if (ok){
					for (int j=0;j<m;++j){
						change|=(b[i][j]!=mini);
						b[i][j]=mini;
					}
				}
			}
			for (int j=0;j<m;++j){
				int mini=-1;
				for (int i=0;i<n;++i){
					mini=max(a[i][j],mini);
				}
				bool ok=true;
				for (int i=0;i<n;++i){
					if (b[i][j]<mini){
						ok=false;
					}
				}
				for (int i=0;i<n && ok;++i){
					change|=(b[i][j]!=mini);
					b[i][j]=mini;
				}
			}
			/*puts("");
			for (int i=0;i<n;++i){
				for (int j=0;j<m;++j){
					printf("%d ",b[i][j]);
				}
				puts("");
			}*/
		}
		
		bool same=true;
		for (int i=0;i<n;++i){
			for (int j=0;j<m;++j){
				same&=a[i][j]==b[i][j];
			}
		}
		printf("Case #%d: %s\n",test,same?"YES":"NO");
	}
	return 0;
}
