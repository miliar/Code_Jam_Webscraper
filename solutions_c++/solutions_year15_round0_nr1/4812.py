#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int T,n,jishu;
int a[2000];
char s[2000];

int main()
{
	scanf("%d" , &T) , jishu = 0;
	
	while (T --)
	{
		jishu ++;
		scanf("%d" , &n);
		scanf(" %s" , &s);
		int len = strlen(s);
		for (int i = 0 ; i < len ; i ++) a[i] = (int) s[i] - (int)'0';
		int ans = 0 , now = 0 , sum = 0; len --;
		while (now <= len)
		{
			while (now <= len && (sum >= now || a[now] == 0)) sum += a[now] , now ++;
			if (now > len) break;
			if (now > sum) ans += now - sum , sum += ans;
		}
		printf("Case #%d: %d\n" , jishu , ans);
	}
	
	return 0;
}
