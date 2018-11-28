#include<cstdio>
using namespace std;
int rows[102];
int cols[102];
int T[102][102];
int main(){
	int z,n,m;
	scanf("%d", &z);
	for(int k=1; k<=z; k++){
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; i++){
			int M=0;
			for(int j=0; j<m; j++){
				scanf("%d", &T[i][j]);
				if(T[i][j]>M)M=T[i][j];
			}
			rows[i]=M;
		}
		for(int j=0; j<m; j++){
			int M=0;
			for(int i=0; i<n; i++)
				if(M<T[i][j])M=T[i][j];
			cols[j]=M;
		}
	
		bool ok = true;
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(!(T[i][j]>=rows[i] || T[i][j]>=cols[j])){
					ok=false;
					break;
				}
			}
			if(!ok)break;
		}
		printf("Case #%d: ",k); 
		if(ok)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
