#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int tc;
	for(tc=1;tc<=t;tc++)
	{
		int a;
		char arr[1111];
		scanf("%d",&a);
		scanf("%s",arr);
		int count=0;
		int l=strlen(arr);
		int ini=arr[0]-48;
		for(int i=1;i<l;i++)
		{
			//printf("--%d\n",ini);
			if(ini<i&&(arr[i]!='0'))
			{
				
				count+=i-ini;
				//printf("%d---here for--%d\n",count,i);
				ini+=count;
			}
			ini+=(arr[i]-48);
		}
		
		printf("Case #%d: %d\n",tc,count);
	}
}