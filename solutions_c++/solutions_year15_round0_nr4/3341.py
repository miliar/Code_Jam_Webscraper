#include<stdio.h>

int main(){
	int T,n,add,i,j,r,c,k=0;
	
	freopen("D-small-attempt3.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&T);
	
	while(T--){
	
		scanf("%d%d%d",&n,&r,&c);
		
		add=0;
		
		if((r*c) % n!=0){
			printf("Case #%d: RICHARD\n",++k);
			continue;
		}
		
		if(n==1 || n==2){
			printf("Case #%d: GABRIEL\n",++k);
			continue;
		}
		else if(n==3){
			if(r*c == 6 || r*c == 9 || r*c == 12) printf("Case #%d: GABRIEL\n",++k);
			else printf("Case #%d: RICHARD\n",++k);
			continue;
		}
		else if(n==4){
			if(r*c == 16 || r*c == 12) printf("Case #%d: GABRIEL\n",++k);
			else printf("Case #%d: RICHARD\n",++k);
		}
	}

	return 0;
}
