#include<iostream>
#include<cstdio>
#include<cmath>


using namespace std;

int main(){
	int t,x,r,c,max;
	scanf("%d",&t);
	for (int i=1;i<=t;i++){
		
		scanf("%d%d%d",&x,&r,&c);
		max = (r>c)?r:c;
		if(x==1)
			printf("Case #%d: GABRIEL\n",i);
		else if (x==2){
			if((r*c)%2==0)
				printf("Case #%d: GABRIEL\n",i);
			else
				printf("Case #%d: RICHARD\n",i);
			}	
		else if (x==3){
			if(max<3)
			printf("Case #%d: RICHARD\n",i);
			if(((r==3)&&(c==1))||((r==1)&&(c==3)))
			printf("Case #%d: RICHARD\n",i);
			if(((r==3)&&(c==2))||((r==2)&&(c==3)))
			printf("Case #%d: GABRIEL\n",i);
			if(((r==3)&&(c==3))||((r==3)&&(c==3)))
			printf("Case #%d: GABRIEL\n",i);
			if(((r==4)&&(c==1))||((r==1)&&(c==4)))
			printf("Case #%d: RICHARD\n",i);
			if(((r==4)&&(c==2))||((r==2)&&(c==4)))
			printf("Case #%d: RICHARD\n",i);
			if(((r==4)&&(c==3))||((r==3)&&(c==4)))
			printf("Case #%d: GABRIEL\n",i);
			if(((r==4)&&(c==4))||((r==4)&&(c==4)))
			printf("Case #%d: RICHARD\n",i);
			
			}
			else if(x==4){
			if((r+c)>=7)
				printf("Case #%d: GABRIEL\n",i);
			else
				printf("Case #%d: RICHARD\n",i);
			
		}
	}
return 0;
}
