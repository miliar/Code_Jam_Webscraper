#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
int main()
{
	freopen("A-small-attempt0.out","w",stdout);
	int T,i,j,k,q,no=1,dir[8][2]={1,0,0,1,-1,0,0,-1,1,1,-1,-1,1,-1,-1,1};
	char a[4][5];
	scanf("%d",&T);
	while(T--){
		for(i=0;i<4;i++)scanf("%4s",a[i]);
		bool f=1,g=1;
		for(i=0;i<4&&f;i++){
			for(j=0;j<4&&f;j++){
				for(k=0;k<8;k++){
					if(a[i][j]=='.'){
						g=0;continue;
					}
					char t=a[i][j];
					int tx=i+dir[k][0];
					int ty=j+dir[k][1];
					bool ff=1;
					for(q=0;q<3;q++){
						if(0<=tx&&tx<5&&0<=ty&&ty<5){
							if(t!=a[tx][ty]&&a[tx][ty]!='T'){
								ff=0;break;
							}
						}
						else{
							ff=0;break;
						}
						tx+=dir[k][0];
						ty+=dir[k][1];
					}
					if(ff){
						f=0;
						printf("Case #%d: %c won\n",no++,t);
						break;
					}
				}
			}
		}
		if(f&&g)printf("Case #%d: Draw\n",no++);
		else if(f)printf("Case #%d: Game has not completed\n",no++);
	}
	return 0;
}