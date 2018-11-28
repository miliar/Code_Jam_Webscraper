#include<cstdio>
#include<cstring>
bool ehPal(long long x){
	char s[20];
	sprintf(s,"%lld",x);
	int n = strlen(s);
	for(int i=0;i<n;i++)
		if(s[i]!=s[n-i-1])
			return false;
	return true;
}

int main(){
  long long v[39];
	int tv=0,t;
	for(long long i=1;i<=10000000;i++){
		if(ehPal(i) && ehPal(i*i))
			v[tv++]=i*i;
	}
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		long long a,b;
		scanf("%lld %lld",&a,&b);
		int cnt=0;
		for(int i=0;i<tv;i++)
			if(v[i]>=a && v[i]<=b)
				cnt++;
		printf("Case #%d: %d\n",caso,cnt);
	}
	return 0;
}
