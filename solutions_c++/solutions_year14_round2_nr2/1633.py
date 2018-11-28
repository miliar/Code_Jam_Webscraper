#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, tc;
	int A, B, K;
	int ans;
	int i ,j;
	
	cin >> T;
	
	for(tc=1;tc<=T;tc++)
	{
		cin >> A>> B >> K;
		
		ans = 0;
		for(i=0;i<A;i++)
		{
			for(j=0;j<B;j++)
			{
				int temp = i&j;
				if(temp < K) ans++;
			}
		}
		
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}
