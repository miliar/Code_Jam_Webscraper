#include<cstdio>
#include<cstring>
int n;
double f[1<<20];
double pp(int x){
	if(f[x]>-0.5)return f[x];
	f[x]=0;
	for(int i=0,j;i<n;++i){
		for(j=0;j<n;++j)
			if(x&1<<(j+i)%n)break;
		f[x]+= pp(x^1<<(j+i)%n)+n-j;
	}
	f[x]/=n;
	return f[x];
}
int main(){
	int T;
	scanf("%d ",&T);
	for(int ti=1;ti<=T;++ti){
		char s[32];
		n = strlen(gets(s));
		int x = 0;
		for(int i=0;i<n;++i)
		if(s[i]=='.')x|=1<<i;
		for(int i=1;i<1<<n;++i)f[i]=-1;
		printf("Case #%d: %.12lf\n",ti,pp(x));
	}
}
