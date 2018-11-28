#include<cstdio>
#include<iostream>
using namespace std;
int X,R,C,T;
char ch[2][10]={"GABRIEL","RICHARD"};
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;++test){
		scanf("%d%d%d",&X,&R,&C);
		if(R*C%X!=0){
			printf("Case #%d: %s\n",test,ch[1]);
			continue;
		}
		if(X>2){
			if(min(R,C)<=X-2){
				printf("Case #%d: %s\n",test,ch[1]);
				continue;
			}
		}
		printf("Case #%d: %s\n",test,ch[0]);
	}
	return 0;
} 
