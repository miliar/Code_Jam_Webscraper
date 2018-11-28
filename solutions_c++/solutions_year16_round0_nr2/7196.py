#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
	int cases;
	char s[1005];
	scanf("%d",&cases);
	for (int ca=1;ca<=cases;ca++)
	{
		int ans=0;
		int flip;
		int l;
		scanf("%s",s);
		l=strlen(s);
		flip=1;
		
		for (int i=l-1;i>=0;i--)
		if ((s[i]=='+' && flip>0)||(s[i]=='-' && flip<0))
			continue;
		else
		{
			flip=-flip;
			ans++;
		}
		
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
