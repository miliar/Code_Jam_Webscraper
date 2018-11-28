#include<stdio.h>
int DO(int n,int r,int p,int s){
	if(n==0){
		if(r+p+s>1) return 0;
		if(r) putchar('R');
		if(p) putchar('P');
		if(s) putchar('S');
		return 1;
	}
	if(n%2==0){
		if(r==p+1&&r==s+1){DO(n-1,r/2,p-p/2,s/2);DO(n-1,r/2,p/2,s-s/2);}
		else if(p==r+1&&p==s+1){DO(n-1,r-r/2,p/2,s/2);DO(n-1,r/2,p/2,s-s/2);}
		else if(s==r+1&&s==p+1){DO(n-1,r/2,p-p/2,s/2);DO(n-1,r-r/2,p/2,s/2);}
		else return 0;
	}
	else{
		if(r==p-1&&r==s-1){DO(n-1,r/2,p-p/2,s/2);DO(n-1,r/2,p/2,s-s/2);}
		else if(p==r-1&&p==s-1){DO(n-1,r-r/2,p/2,s/2);DO(n-1,r/2,p/2,s-s/2);}
		else if(s==r-1&&s==p-1){DO(n-1,r/2,p-p/2,s/2);DO(n-1,r-r/2,p/2,s/2);}
		else return 0;
	}
}
int main(){
	int T,t,n,r,p,s;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d%d%d",&n,&r,&p,&s);
		printf("Case #%d: ",t);
		if(DO(n,r,p,s)==0) printf("IMPOSSIBLE");
		puts("");
	}
}
