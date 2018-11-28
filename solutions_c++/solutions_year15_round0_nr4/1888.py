#include <stdio.h>

using namespace std;

int main(){
	int t;
	int x,r,c;
	bool b;
	int k;
	scanf("%i",&t);
	for(int i=1 ; i<=t ; i++){
		scanf("%i%i%i",&x,&r,&c);
		if(r>c){
			r=r+c;
			c=r-c;
			r=r-c;
		}
		
		if(x==1){
			printf("Case #%i: GABRIEL\n",i);	
		}
		else if(x==2){
			if(r%2==0 || c%2==0){
				printf("Case #%i: GABRIEL\n",i);	
			}
			else{
				printf("Case #%i: RICHARD\n",i);
			}
		}
		else if(x==3){
			if( (r==2 && c==3) || (r==3 && c==3) || (r==3 && c==4) ){
				printf("Case #%i: GABRIEL\n",i);
			}
			else{
				printf("Case #%i: RICHARD\n",i);
			}
		}
		else{
			if( r>=3 && c==4 ){
				printf("Case #%i: GABRIEL\n",i);
			}
			else{
				printf("Case #%i: RICHARD\n",i);
			}
		}
	}
}
