#include <iostream>
#include <queue>
using namespace std;
queue<int>q;
long long int arr[10000000];
int rev(int x)
{
	int res = 0;
	while (x !=0)
	{
		res = res* 10 + (x % 10);
		x /= 10;
	}
	return res;
}

int main()
{
	freopen ("a.in", "r", stdin);
   freopen ("output.txt", "w", stdout);
     int i,j,t;
	arr[1] = 1;
	q.push(1);
	while (!q.empty())
	{
		int i = q.front();
		q.pop();
		if (i + 1 < 1000001 and arr[i+ 1] == 0)
		{
			arr[i + 1] = arr[i] + 1;
			q.push(i+ 1);
		}
		if (rev(i) < 1000001 and arr[rev(i)] == 0)
		{
			arr[rev(i)] = arr[i] + 1;
			q.push(rev(i));
		}
	}
	int t1;
	scanf("%d",&t1);
	for (int t = 1; t <= t1; t++)
	{
		long long int n;
		scanf("%lld",&n);
		printf("Case #%d: %lld\n", t, arr[n]);
	}
	return 0;
}
