#include<bits/stdc++.h>
using namespace std;
int T, x,r,c;
int main(){
	freopen("omin.txt","r",stdin);
	freopen("omout.txt","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %d %d",&x,&r,&c);
		if(x==1){
			printf("Case #%d: GABRIEL\n",i+1);
		} 
		if(x==2){
			if((r*c)%2 == 0)
				printf("Case #%d: GABRIEL\n",i+1);
			else 
				printf("Case #%d: RICHARD\n",i+1);
		}
		if(x==3){
			if((r*c)%3 != 0)
				printf("Case #%d: RICHARD\n",i+1);
			else {
				if(r==1 || c==1)
					printf("Case #%d: RICHARD\n",i+1);
				else 
					printf("Case #%d: GABRIEL\n",i+1);
			}
		}
		if(x==4){
			if((r*c)%4 != 0)
				printf("Case #%d: RICHARD\n",i+1);
			else {
				if((r*c)==4 || (r*c)==8)
					printf("Case #%d: RICHARD\n",i+1);
				else
					printf("Case #%d: GABRIEL\n",i+1);
			}
		}
	}
	return 0;
}
