#include <cstdio>
const int N =110;
char grid[N][N];

bool check(int i,int j,int R,int C,int& ans){
	int u=0,d=0,l=0,r=0;
	for(int k=0;k<R;k++){
		if(k<i && grid[k][j]!='.')u++;
		else if(k>i && grid[k][j]!='.')d++;
	}
	for(int k=0;k<C;k++){
		if(k<j && grid[i][k]!='.')l++;
		else if(k>j && grid[i][k]!='.')r++;
	}
	if(u+d+l+r==0)return false;
	char now = grid[i][j];
	if(now=='^' &&u>0) return true;
	if(now=='v' &&d>0) return true;
	if(now=='<' &&l>0) return true;
	if(now=='>' &&r>0) return true;
	ans++;return true;

}
int main(){
	int T;
	scanf("%d",&T);
	int r,c;
	int count = 0;
	while(count++ <T){
		scanf("%d %d",&r,&c);
		for(int i=0;i<r;i++){
			scanf("%s",grid[i]);		
		}
		int ans = 0;
		bool w = true;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(grid[i][j] != '.'){
					w = check(i,j,r,c,ans);
					if(!w) break;
				}
			}
			if(!w)break;
		}
		printf("Case #%d: ",count);
		if(w)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	
	}

}
