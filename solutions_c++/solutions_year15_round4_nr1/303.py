#include<stdio.h>
char tab[1000][1000];
int n,m;
int find(int tx,int ty,char dir){
	int dx=0,dy=0;
	if( dir == '^' ) dx=-1;
	if( dir == 'v' ) dx=1;
	if( dir == '<' ) dy=-1;
	if( dir == '>' ) dy=1;
	
	for(; ;){
		tx+=dx;
		ty+=dy;
		if( tx<0 || tx>=n || ty<0 || ty>=m ) return 0;
		if( tab[tx][ty] != '.') return 1;
	}
}
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ;e< t ; e++ ){
		scanf("%d %d",&n,&m);
		for(int i = 0 ; i< n ; i++ ){
			scanf("%s",tab[i]);
		}
		int ans = 0;
		int fail = 0;
		for(int i = 0 ; i < n ; i++ ){
			for(int j = 0 ; j< m ; j++ ){
				if( tab[i][j] == '.' ) continue;
				if( find(i,j,tab[i][j]) == 0 ){
					if( find(i,j,'^')
					||  find(i,j,'<')
					||  find(i,j,'>')
					||  find(i,j,'v') ){
						ans++;
					}else{
						fail = 1;
						break;
					}
				}
			}
			if( fail) break;
		}
		printf("Case #%d: ",e+1);
		if( fail ) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
}

