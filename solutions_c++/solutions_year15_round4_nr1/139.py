#include<stdio.h>
#include<algorithm>
using namespace std;
char str[120][120];
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
char dir[6]="v>^<";
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++)scanf("%s",str[i]);
		int ret=0;
		bool ok=true;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if(str[i][j]=='.')continue;
				int type=-1;
				for(int k=0;k<4;k++){
					int row=i;
					int col=j;
					bool OK=false;
					while(1){
						row+=dx[k];
						col+=dy[k];
						if(row<0||row>=a||col<0||col>=b)break;
						if(str[row][col]!='.'){OK=true;break;}
					}
					if(OK){
						if(str[i][j]==dir[k])type=0;
						else if(type==-1)type=1;
					}
				}
			//	printf("%d %d: %d\n",i,j,type);
				if(type==-1)ok=false;
				else ret+=type;
			}
		}
		printf("Case #%d: ",t);
		if(!ok){
			printf("IMPOSSIBLE\n");
		}else printf("%d\n",ret);
	}
}