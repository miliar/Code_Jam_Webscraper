#include<stdio.h>
long long gcd(long long x,long long y){
	return x%y==0?y:gcd(y,x%y);
}
bool is2(long long x){
	if(x==1)return true;
	if(x%2==1)return false;
	return is2(x>>1);
}
int pow(long long x){
	if(x==1)return 0;
	return pow(x>>1)+1;
}
int main()
{
	int T,q;
	freopen("A-large.in","r",stdin);
	freopen("A-output.txt","w",stdout);
	scanf("%d",&T);
	for(q=1;q<=T;q++){
		long long x,y;
		scanf("%lld/%lld",&x,&y);
		printf("Case #%d: ",q);
		long long d=gcd(x,y);
		x/=d;y/=d;
		if(!is2(y)){printf("impossible\n");continue;}
		int p=pow(y);
		int pp=pow(x);
		printf("%d\n",p-pp);
	}
	return 0;
}