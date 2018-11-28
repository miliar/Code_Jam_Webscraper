#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
bool flag[10];
const int N = 1000005;
LL ans[N];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//const int N = 1000005;
	for (int i=0;i<N;i++)
	{
		memset(flag,0,sizeof(flag));
		int len = 10;
		for (int j=1;j<=N;j++)
		{		
			LL k = i * j;
			LL tmp = k;
			do
			{
				if (flag[k % 10]==false) len--;
				flag[k % 10] = true;
				k/=10;
			}
			while (k > 0);
			if (len == 0) 
			{
				ans[i] = tmp;
				break;
			}
		}	
	}
	int n;
	scanf("%d",&n);
	for (int i=0;i<n;i++)
	{
		int tmp;
		scanf("%d",&tmp);
		printf("Case #%d: ",i+1);
		if (tmp == 0) printf("INSOMNIA\n");
		else printf("%d\n",ans[tmp]);
	}	
} 
