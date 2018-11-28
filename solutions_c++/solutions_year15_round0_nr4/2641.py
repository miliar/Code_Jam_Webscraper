#include<cstdio>
#include<iostream>
using namespace std;
int main(){
long int t,x,r,c,caseno=1;
scanf("%ld",&t);
	while(t--){
			bool gabri=false;
			scanf("%ld",&x);
			scanf("%ld",&r);
			scanf("%ld",&c);
			
			if(x>r && x>c)
				gabri = false;
			else if((x-1>r) || (x-1>c))
				gabri = false;
			else if(r*c % x != 0)
				gabri = false;
			else if(x%2==0 && r%2==1 && c%2==1)
				gabri=false;				
			else {
				gabri = true;
			}
			
			printf("Case #%ld: ",caseno++);
			if(gabri)printf("GABRIEL\n");
			else printf("RICHARD\n");
			
	}
}
