#include <cstdio>
#include <cstring>

char S[110];
int ans;
inline void init()
{
	ans = 0;
}
void count(int len)
{
	for(int i=0;i<len;i++){
		while( i+1<len && S[i]==S[i+1] ) i++;
		ans++;
	}
}


int main (void)
{
	freopen("B-large.in","r",stdin);
	freopen("bigout.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++){
		init();
		
		scanf("%s",S);
		int len = strlen(S);
		count(len);
		if(S[len-1]=='+') ans--;
		printf("Case #%d: %d\n",kase,ans);
	}
	
	return 0;
}
