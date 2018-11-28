#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
#define debug printf("DEBUG: On Line #: %d\n", __LINE__);
#define max(x,y) (x>y?x:y)
#define min(x,y) (x<y?x:y)

int main()
{
	
	int t;
	scanf("%d",&t);
	int cas = 1;
	while (t--)
	{
		int a,b,k;
		scanf("%d%d%d",&a,&b,&k);
		int i,j;
		int ans = 0;
		for (i=0;i<a;i++)
		{
			for (j=0;j<b;j++)
				if ( (i&j) < k)
					ans++;
		}
		printf("Case #%d: %d\n",cas++, ans);
		
	}
	
	return 0;
}
