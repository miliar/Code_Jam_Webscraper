#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	freopen("D-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,x,r,c;
	scanf("%d",&T);
	for(int t=1;t<=64;t++){
		scanf("%d%d%d",&x,&r,&c);
		if(r>c)swap(r,c);
		if(x==1){
			printf("Case #%d: GABRIEL\n",t);
		}
		else if(x==2){
			if((r*c)%2==0){
				printf("Case #%d: GABRIEL\n",t);
			}
			else{
				printf("Case #%d: RICHARD\n",t);
			}
		}
		else if(x==3){
			if(r==2&&c==3||r==3&&c==3||r==3&&c==4){
				printf("Case #%d: GABRIEL\n",t);
			}
			else{
				printf("Case #%d: RICHARD\n",t);
			}
		}
		else{
			if(r==3&&c==4||r==4&&c==4){
				printf("Case #%d: GABRIEL\n",t);
			}
			else{
				printf("Case #%d: RICHARD\n",t);
			}
		}
	}
}
