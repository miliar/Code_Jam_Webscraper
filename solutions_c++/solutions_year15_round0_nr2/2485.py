#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int ix=0;ix<T;ix++)
	{
		printf("Case #%d: ",ix+1);
		int n;
		scanf("%d",&n);
		vector<int> arr;
		int max = 0;
		for(int i=0;i<n;i++)
		{
			int x;
			scanf("%d",&x);
			if(x>max)
				max = x;
			arr.push_back(x);
		}
		int ans = 100000000;
		for(int i=1;i<=max;i++)
		{
			int temp_ans = 0;
			for(int j=0;j<arr.size();j++)
			{
				if(arr[j]%i==0)
					temp_ans+=arr[j]/i-1;
				else
					temp_ans+=arr[j]/i;
			}
			temp_ans+=i;
			if(temp_ans<ans)
				ans = temp_ans;
		}
		printf("%d\n",ans);

	}
	return 0;
}