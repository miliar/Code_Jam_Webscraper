#include <iostream>
#include <cstdio>
using namespace std;

const int N = 105;

char s[N];
int T,n,ans;

int main()
{
	//freopen("1.out","w",stdout);
	int i,j,la;
	scanf("%d",&T);
	for(int t = 1; t <= T; ++ t)
	{
		ans = 0;
		//memset(vis,false,sizeof(vis));
		scanf("%s",s+1); n = strlen(s+1);
		if(s[n] == '-') ans ++;
		for(i = 1; i < n; ++ i)
			if((s[i] == '-' && s[i+1] == '+') ||
			   (s[i] == '+' && s[i+1] == '-'))
			  	++ans;
			
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
