#include<iostream>
#include<fstream>
using namespace std;

main(){
	int T;
	scanf("%d",&T);
	fstream mf;
	mf.open("D:/seijee.txt");
	for (int cse=1; cse<=T; cse++){
		int N, M;
		scanf("%d%d",&N,&M);
		int grid[N][M];
		int row_max[N];
		int col_max[M];
		
		for (int i=0; i<M; i++) col_max[i]=-1;
		for (int i=0; i<N; i++) row_max[i]=-1;
		
		for (int i=0; i<N; i++){
			for (int j=0; j<M; j++){
				scanf("%d",&grid[i][j]);
				row_max[i] = max(grid[i][j],row_max[i]);
				col_max[j] = max(grid[i][j],col_max[j]);
			}
		}
		bool ans=true;
		for (int i=0; i<N; i++){
			for (int j=0; j<M; j++){
				if (grid[i][j]!=row_max[i] && grid[i][j]!=col_max[j]) {
					ans=false;
				}
			}
		}
		mf<<"Case #"<<cse<<": ";
		if (ans) {
			mf<<"YES\n";
		}else{
			mf<<"NO\n";
		}
	}
	mf.close();
}
