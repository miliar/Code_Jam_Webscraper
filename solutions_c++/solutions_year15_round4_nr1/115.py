#include <cstdio>

int T,R,C;
char fld[108][108];
int main() {
	scanf("%d",&T);
	for(int ts=1;ts<=T;ts++) {
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++) scanf("%s",fld[i]);
		int ng=0;
		int sum=0;
		for(int i=0;i<R;i++) {
			for(int j=0;j<C;j++) {
				if(fld[i][j]!='.') {
					int isng=1;
					for(int k=0;k<R;k++) {
						if(i!=k&&fld[k][j]!='.') isng=0;
					}
					for(int k=0;k<C;k++) {
						if(j!=k&&fld[i][k]!='.') isng=0;
					}
					if(isng) ng=1;
					int isout=1;
					if(fld[i][j]=='<') {
						for(int k=0;k<j;k++) {
							if(fld[i][k]!='.') isout=0;
						}
					}
					if(fld[i][j]=='>') {
						for(int k=j+1;k<C;k++) {
							if(fld[i][k]!='.') isout=0;
						}
					}
					if(fld[i][j]=='^') {
						for(int k=0;k<i;k++) {
							if(fld[k][j]!='.') isout=0;
						}
					}
					if(fld[i][j]=='v') {
						for(int k=i+1;k<R;k++) {
							if(fld[k][j]!='.') isout=0;
						}
					}
					sum+=isout;
				}
			}
		}
		if(ng) {
			printf("Case #%d: IMPOSSIBLE\n",ts);
		} else {
			printf("Case #%d: %d\n",ts,sum);
		}
	}
	return 0;
}
