#include<stdio.h>
#include<algorithm>
using namespace std;
char ret[11000];
void fill(int a,int b,int p,int r,int s){
	if(a+1==b){
		if(p)ret[a]='P';
		else if(r)ret[a]='R';
		else ret[a]='S';
		return;
	}
	int m=(a+b)/2;
	if(p%2){
		fill(a,m,p/2+1,r/2,s/2);
		fill(m,b,p/2,(r+1)/2,(s+1)/2);
	}else{
		fill(a,m,p/2,r/2+1,s/2);
		fill(m,b,(p+1)/2,r/2,(s+1)/2);
	}
}
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;
		int r,p,s;
		scanf("%d%d%d%d",&a,&r,&p,&s);
		printf("Case #%d: ",t);
		if(max(r,max(p,s))-min(r,min(p,s))>=2){
			printf("IMPOSSIBLE\n");continue;
		}
		ret[1<<a]=0;
		fill(0,1<<a,p,r,s);
		printf("%s\n",ret);
	}
}