#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iomanip>
#include<ctime>
#include<cstring>
#include<climits>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<stack>
#include<deque>
#include<list>
#include<vector>
#define LL long long
using namespace std;
int cnt,snt,n,L,m,times;
LL oo=1000000007;
int a[100010];
void work(int lab)
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
	sort(a+1,a+n+1);
	int head=1,tail=n;
	int ans=0;
	while (head<=tail)
	{
		if (head==tail)
		{
			ans++;
			break;
		}
		else 
		{
			if (m>=a[head]+a[tail])
			{
				head++;
				tail--;
				ans++;
			}
			else 
			{
				tail--;
				ans++;
			}
		}
	}
	printf("Case #%d: %d\n",lab,ans);
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&times);
	for (int i=1;i<=times;i++)
	work(i);
	return 0;
}
