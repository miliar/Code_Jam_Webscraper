#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<stack>
#include<string>
#include<cctype>
#include<list>
#include<set>
#include<deque>
#include<queue>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<ctime>

using namespace std;

int main()
{
	int t,m,n,a[1000],i,j,ans,s,test,curr;
	scanf("%d",&t);test=1;
	while(t--)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
/*		sort(a,a+n);
		s=m;j=0;curr=0;ans=n;
		if(m==1){ans=n;}
		else
		{
		while(j<n)
		{
			if(a[j]<s)
			{
			s=s+a[j];
			j++;
			ans=min(ans,(curr+n-j));//printf("%d ",ans);
			}
			else
			{
				curr++;
				s=s+s-1;
			}
		}
		}*/
		printf("Case #%d: %d\n",test,ans);
		test++;
	}
	return 0;
}	
			


















