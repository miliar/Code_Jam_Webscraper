#include<stdio.h>
int tcn,tc;
int n,m;
char map[110][110];
int ans;
int main(){
	int i,j,k,p;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%s",map[i]);
		}
		p=0;
		ans=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(map[i][j]!='.'){
					p=0;
					for(k=0;k<n;k++){
						if(map[k][j]!='.')p++;
					}
					for(k=0;k<m;k++){
						if(map[i][k]!='.')p++;
					}
					if(p==2){
						break;
					}
					if(map[i][j]=='>'){
						for(k=j+1;k<m;k++){
							if(map[i][k]!='.')break;
						}
						if(k==m)ans++;
					}
					if(map[i][j]=='<'){
						for(k=0;k<j;k++){
							if(map[i][k]!='.')break;
						}
						if(k==j)ans++;
					}
					if(map[i][j]=='v'){
						for(k=i+1;k<n;k++){
							if(map[k][j]!='.')break;
						}
						if(k==n)ans++;
					}
					if(map[i][j]=='^'){
						for(k=0;k<i;k++){
							if(map[k][j]!='.')break;
						}
						if(k==i)ans++;
					}
				}
			}
			if(p==2)break;
		}
		printf("Case #%d: ",tc);
		if(p==2){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n",ans);
		}
	}
}