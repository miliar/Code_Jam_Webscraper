#include <cstdio>
void printR(int t,bool flag){
	if(flag)
		printf("Case #%d: GABRIEL\n",t);
	else
		printf("Case #%d: RICHARD\n",t);
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,x,r,c;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		scanf("%d%d%d",&x,&r,&c);
		if(x==1) printR(i,1);
		else if(x==2){
			if((r*c) % 2 ==0) printR(i,1);
			else printR(i,0);
		}
		else if(x==3){
			if((r*c) % 3 ==0){
				if(r==1 || c==1) printR(i,0);
				else printR(i,1);
			}
			else printR(i,0);
		}
		else if(x==4){
			if(r==4 && c==4) printR(i,1);
			else if(r*c==12) printR(i,1);
			else printR(i,0);
		}
	}
	return 0;
}