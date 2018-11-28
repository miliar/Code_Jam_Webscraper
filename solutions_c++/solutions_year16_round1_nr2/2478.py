#include <bits/stdc++.h>

using namespace std;
int n, tc;
int col[55], row[55];
int arr[150][55];
int grid[55][55];
bool trytofit(int nowpaper) {
	if(nowpaper == 2*n) {
		//check row
	//	printf("nah");
		int cek[150];
		memset(cek,0,sizeof cek);
		for(int i=1;i<=n;i++) {
			int stat=0;
			for(int j=1;j<=2*n-1;j++) {
				if(cek[j]!=1)
				for(int k=1;k<=n;k++) {
					if(grid[k][i]!=arr[j][k]) {
						break;
					}
					if(k==n) {
						cek[j]=1;
						stat=1;
					}
				}
				if(stat)break;
				if(j==2*n-1) {
//					printf("lala");
					for(int k=1;k<=n;k++) {
						printf(" %d", grid[k][i]);
					}
					printf("\n");
					return true;
				}
			}
		}
//		printf("noh %d", cek[3]);
		//check col
			for(int i=1;i<=n;i++) {
			int stat=0;
			for(int j=1;j<=2*n-1;j++) {
				if(cek[j]!=1) 
				for(int k=1;k<=n;k++) {
					if(grid[i][k]!=arr[j][k]) {
						break;
					}
					if(k==n) {
						cek[j]=1;
						stat=1;
					}
				}
				if(stat)break;
				//printf("lah");
				if(j==2*n-1) {
					//printf("lala");
					for(int k=1;k<=n;k++) {
						printf(" %d", grid[i][k]);
					}
					printf("\n");
					return true;
				}
			}
		}
			
	}
	//row
	for(int a=1;a<=n;a++) {
		if(!row[a])
		for(int i=1;i<=n;i++) {
			if(grid[i][a]==0) {
				//fit
				int simp[55];
				memset(simp,0,sizeof simp);
				for(int j=i;j<=n;j++) {
					if(grid[j][a]==0)simp[j]=1;
					else if(grid[j][a]!=arr[nowpaper][j])break;
					grid[j][a] = arr[nowpaper][j];
				}
	//			if(tc==5) {
/*					printf("%d1:\n",nowpaper);
					for(int j=1;j<=n;j++) {
						for(int k=1;k<=n;k++) {
							printf("%d ",grid[j][k]);
						}
						printf("\n");
					}
					printf("\n");
*/	//			}
				row[a]=1;
				//recurse
				bool tes = trytofit(nowpaper+1);
				row[a]=0;
				
				if(tes) return true;
				//unfit
				for(int j=i;j<=n;j++) {
					if(simp[j])
					grid[j][a] = 0;
				}
	//			return false;
			}
			if(i==n && grid[i][a]==arr[nowpaper][i]) {
				row[a]=1;
				bool tes = trytofit(nowpaper+1);
				row[a]=0;
				
				if(tes) return true;
				
			}
			if(grid[i][a]!=arr[nowpaper][i]) {
				break;
			}
			
		}
	}
//	printf("duh");
	
	//col
	for(int a=1;a<=n;a++) {
		if(!col[a])
		for(int i=1;i<=n;i++) {
			if(grid[a][i]==0) {
				//fit
				int simp[55];
				memset(simp,0,sizeof simp);
				for(int j=i;j<=n;j++) {
					if(grid[a][j]==0)simp[j]=1;
					else if(grid[a][j]!=arr[nowpaper][j])break;
					grid[a][j] = arr[nowpaper][j];
				}
	//			if(tc==5) {
/*					printf("%d:\n",nowpaper);
					for(int j=1;j<=n;j++) {
						for(int k=1;k<=n;k++) {
							printf("%d ",grid[j][k]);
						}
						printf("\n");
					}
					printf("\n");
*/	//			}
				//recurse
				col[a]=1;
				bool tes = trytofit(nowpaper+1);
				col[a]=0;
				if(tes) return true;
				//unfit
				for(int j=i;j<=n;j++) {
					if(simp[j])
					grid[a][j] = 0;
				}
				return false;
			}
			if(i==n && grid[a][i]==arr[nowpaper][i]) {
				col[a]=1;
				bool tes = trytofit(nowpaper+1);
				col[a]=0;
				
				if(tes) return true;
			}
			else if(grid[a][i]!=arr[nowpaper][i]) {
				break;
			}
			
		}
	}
	return false;
}

int main() {
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	for(tc = 1; tc <= test; tc++) {
		scanf("%d",&n);
		memset(grid,0,sizeof grid);
		memset(arr,0,sizeof arr);
		memset(col,0,sizeof col);
		memset(row,0,sizeof row);
		for(int i = 1; i <=2*n-1; i++) {
			for(int j = 1; j <= n; j++) {
				scanf("%d",&arr[i][j]);
			}
		}
		for(int i=1;i<=2*n-1;i++) {
			int temp = i;
			while(temp!=1) {
//				printf("%d\n",temp);
				for(int j=1;j<=n;j++) {
					if(arr[temp][j]<arr[temp-1][j]) {
						for(int j=1; j<=n; j++) {
							swap(arr[temp][j], arr[temp-1][j]);
						}
//						printf("waca");
						temp--;
						break;
					}
					else if(j==n) goto notswap;
					else if(arr[temp][j]==arr[temp-1][j]) continue;
					else goto notswap;
				}
			}
			notswap:;
		}
//		if(tc==5) {
/*		for(int i=1;i<=2*n-1;i++) {
			for(int j=1;j<=n;j++) {
				printf("%d ", arr[i][j]);
			}
			printf("\n");
		}
		printf("\n");
*/		for(int i=1;i<=n;i++) {
			grid[1][i] = arr[1][i];
		}
//		for(int i=1;i<=n;i++) {
//			grid[i][1] = arr[2][i];
//		}
/*		for(int i=1;i<=n;i++) {
			for(int j=1;j<=n;j++) {
				printf("%d ",grid[i][j]);
			}
			printf("\n");
		}
*/		printf("Case #%d:", tc);
		trytofit(2);
//		}
	}
	return 0;
}
