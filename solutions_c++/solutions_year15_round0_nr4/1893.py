#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int T; scanf("%d",&T);
	for(int Case=1; Case<=T; ++Case){
		int X,R,C; scanf("%d%d%d",&X,&R,&C);
		if(X==1 || X==2){
			if( (R*C)%X==0 && (R%X==0 || C%X==0) )
				printf("Case #%d: GABRIEL\n",Case);
			else
				printf("Case #%d: RICHARD\n",Case);
		}
		else if(X==3){
			if(R==1 || C==1)
				printf("Case #%d: RICHARD\n",Case);
			else if( (R*C)%X==0 )
				printf("Case #%d: GABRIEL\n",Case);
			else
				printf("Case #%d: RICHARD\n",Case);
		}
		else{
			if(R*C==12 || R*C==16)
				printf("Case #%d: GABRIEL\n",Case);
			else
				printf("Case #%d: RICHARD\n",Case);
		}
	}
	return 0;
}
