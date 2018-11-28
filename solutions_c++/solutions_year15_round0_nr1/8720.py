#include <cstdio>
using namespace std;
char p[1005];
int main()
{
	 freopen("alarge.in","r",stdin);
	 freopen("0.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)
	{
		int max;
		scanf("%d%s",&max,p);
		int sum = p[0]-'0';
		int cnt = 0;
		for(int j = 0; j < max;j++)
		{
			int add=0;
			if(sum<j+1&&p[j+1]-'0'>0)
			{
				add=j+1-sum;
				cnt+=add;
			}
			sum+=add+p[j+1] - '0';
		}
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}
