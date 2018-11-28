#include <stdio.h>
#include <string.h>

using namespace std;

int t;
int r,c;

char M[120][120];
int cr[120],cc[120];

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt){
		printf("Case #%d: ",tt);
		scanf("%d%d\n",&r,&c);
		for(int i=0;i<r;++i){
			scanf("%s",M[i]);
		}
		memset(cr,0,sizeof(cr));
		memset(cc,0,sizeof(cc));
		int res=0;
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				if (M[i][j]=='>'){
					int k=j+1;
					while(k<c&&M[i][k]=='.') ++k;
					if (k==c){
						res++;
					}
				} else if (M[i][j]=='<'){
					int k=j-1;
					while(k>=0&&M[i][k]=='.') --k;
					if (k==-1){
						res++;
					}
				} else if (M[i][j]=='^'){
					int k=i-1;
					while(k>=0&&M[k][j]=='.') --k;
					if (k==-1){
						res++;
					}
				} else if (M[i][j]=='v'){
					int k=i+1;
					while(k<r&&M[k][j]=='.') ++k;
					if (k==r){
						res++;
					}
				}
				if (M[i][j]!='.'){
					cr[i]++;
					cc[j]++;
				}
			}
		}
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				if (M[i][j]!='.'&&cr[i]==1&&cc[j]==1){
					res=-1;
				}
			}
		}
		if (res==-1) puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
	return 0;
}
