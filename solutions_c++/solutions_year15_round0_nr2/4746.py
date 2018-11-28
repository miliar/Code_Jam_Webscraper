#include<cstdio>
#include<algorithm>
using namespace std;

int main() {
	int Z;
	scanf("%d", &Z);
	for(int z=1;z<=Z;z++)
	{
		int n, m = 0;
		scanf("%d", &n);
		int arr[n];
		for(int i=0;i<n;i++)
		{
			scanf("%d", arr+i);
			m = max(m, arr[i]);
		}
		int res = m;
		for(int k=1;k<=m;k++)
		{
			int t = 0;
			for(int i=0;i<n;i++)
			{
				t += (arr[i]+k-1)/k - 1;
			}
			res = min(res, t+k);
		}
		printf("Case #%d: %d\n", z, res);
	}
	return 0;
}