#include <cstdio>
#include <algorithm>
using namespace std;
int T,TC=1,n,m,a[101][101],d[101][101],ch,M;
int main(void){
	freopen("B-small-attempt3.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d %d",&n,&m);
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++)
				scanf("%d",&a[i][j]);
		}
		M=a[0][0];
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				M=max(M,a[i][j]);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				d[i][j]=M;
		for(int i=0; i<n; i++){
			ch=0;
			for(int j=0; j<m-1; j++){
				if(a[i][j]!=a[i][j+1]){
					ch=1;
					break;
				}
			}
			if(ch==0){
				for(int j=0; j<m; j++){
					d[i][j]=min(d[i][j],a[i][0]);
				}
			}
		}
		for(int i=0; i<m; i++){
			ch=0;
			for(int j=0; j<n-1; j++){
				if(a[j][i]!=a[j+1][i]){
					ch=1;
					break;
				}
			}
			if(ch==0){
				for(int j=0; j<n; j++){
					d[j][i]=min(d[j][i],a[0][i]);
				}
			}
		}
		ch=0;
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(a[i][j]!=d[i][j]){
					ch=1;
					break;
				}

			}
		}
		printf("Case #%d: ",TC);
		if(!ch)
			puts("YES");
		else puts("NO");
		TC++;
	}

	return 0;
}