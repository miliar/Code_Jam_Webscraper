#include<cstdio>
int main(){
	long long t,n,i,c=0,j;
	char s[2000];
	scanf("%lld",&t);
	for(j=1;j<=t;j++){long long a[1024]={0};c=0;
		scanf("%lld",&n);
		scanf("%s",s);
		if(n==0)
		printf("Case #%lld: %lld\n",j,0);
		else{
			a[0]=s[0]-48;
		for(i=1;s[i];i++){
			a[i]=s[i]-48+a[i-1];
		}
			for(i=1;s[i];i++){
			if(i>(a[i-1]+c))
			c+=i-(a[i-1]+c);
		}
		
		printf("Case #%lld: %lld\n",j,c);
		
		
		
		
	}
}
}
