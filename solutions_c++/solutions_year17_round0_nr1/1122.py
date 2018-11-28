#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1005;

char s[maxn];
int m;
int main()
{
	int t,cs=0;scanf("%d",&t);
	while(t--)
	{
		scanf("%s%d",s,&m);
		int cnt = 0;
		int error = 0;
		int l = strlen(s);
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				if(i+m>l)
					error = 1;
				else
				{
					cnt++;
					for(int j=0;j<m;j++)
						if(s[i+j]=='-')
							s[i+j] = '+';
						else
							s[i+j] = '-';
				}
			}
		}
		printf("Case #%d: ",++cs);
		if(error)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",cnt);
	}

}