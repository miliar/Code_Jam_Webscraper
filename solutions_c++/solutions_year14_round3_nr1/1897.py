#include <stdio.h>
#include <stdlib.h>

int P;
int Q;

void yakbun(){
	int i=9;
	while(i>1){
		if((P%i==0)&&(Q%i==0)){
		P=P/i;
		Q=Q/i;
		
			break;
		}
		i--;
	}
	

}


int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int c=1;
	int T;
	scanf("%d",&T);
	while(T-->0) {

		char C;
		scanf("%d %c %d",&P,&C,&Q);

		int g=0;
		int u=0;
		bool f=false;

		while(g<41){
			g++;
			
			P=P*2;
			yakbun();
			if(P>Q){
				P=P-Q;
				if(u==0){
				u=g;
				}
			}
			
			if(((P==1)&&(Q==1))||(P==Q)){
				f=true;
				break;
			}
			
		}
		if((f)&&(u!=0)){
			g=u;
		}
		if(f){
			printf("case #%d: %d\n",c,g);
		}else{
			printf("case #%d: impossible\n",c);
		}
		c++;
	}
	return 0;
}