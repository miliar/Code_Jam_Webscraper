#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN 100
#define MAXM 100

int main(){
	int t;
	cin>>t;
	
	for(int tt=1; tt<=t; tt++){
		int n,m,mat[MAXN][MAXM],mat_[MAXN][MAXM],X[MAXN][MAXM];
		cin>>n>>m;
		
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				cin>>mat[i][j];
				mat_[j][i]=mat[i][j];
				X[i][j]=100;
			}
		}
		
		for (int r=0; r<n; r++){
			int z=*max_element(mat[r],mat[r]+m);
			for (int c=0; c<m; c++){X[r][c]=min(X[r][c],z);}
		}
		
		for (int c=0; c<m; c++){
			int z=*max_element(mat_[c],mat_[c]+n);
			for (int r=0; r<n; r++){X[r][c]=min(X[r][c],z);}
		}
		
		bool bad=false;
		
		for(int i=0;i<n&&!bad;i++){
			for(int j=0;j<m;j++){
				if(X[i][j]!=mat[i][j]){
					bad=true;
					break;
				}
			}
		}
		
		printf("Case #%d: %s\n", tt, bad?"NO":"YES");
	}
	return 0;
}