#include <cstdio>

bool visit[10];
int digit;
inline void init()
{
	digit = 0;
	for(int i=0;i<10;i++)
		visit[i] = false;
}
inline void doing(unsigned long long now)
{
	do{
		if( !visit[now%10] )
			visit[now%10] = true , digit++;
	}while(now/=10);
}

int main (void)
{
	freopen("A-large.in","r",stdin);
	freopen("bigout.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++){
		init();
		
		unsigned long long N;
		scanf("%llu",&N);
		if( N==0 ){
			printf("Case #%d: INSOMNIA\n",kase);
			continue;
		}
		unsigned long long ans = N;
		while( digit<10 ){
			doing(ans);
			if(digit==10) break;
			ans += N;
		}
		printf("Case #%d: %llu\n",kase,ans);
	}
	
	return 0;
}
