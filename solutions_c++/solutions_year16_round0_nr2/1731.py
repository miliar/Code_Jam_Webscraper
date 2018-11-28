#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int n,len,cnt;
	char str[300];
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&n);
	for (int x=1;x<=n;x++)
	{
		printf("Case #%d: ",x);
		scanf(" %s",str);
		strcat(str,"+");
		len = strlen(str);
		cnt = 0;
		for (int i=1;i<len;i++)
			if (str[i]!=str[i-1])
				cnt++;
		printf("%d\n",cnt);
	}
	return 0;
}