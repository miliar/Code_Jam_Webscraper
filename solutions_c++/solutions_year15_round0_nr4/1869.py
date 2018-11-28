#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;
int main(){
	freopen("E:D-small-attempt0.in","r",stdin);
	freopen("E:D-small-attempt0.out","w",stdout);
	int i,j,n,m,T,vcase=0,x,r,c;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",++vcase);
		if(x==1) printf("GABRIEL\n");
		else if(x==2){
			if(r*c%2) printf("RICHARD\n");
			else printf("GABRIEL\n");
		}
		else if(x==3){
			if(r*c%3==0 && r!=1 && c!=1) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else{
			if(r*c==16 || r*c==12) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
	}
	return 0;
}