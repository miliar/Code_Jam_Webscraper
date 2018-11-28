#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int N, M, tot, ans;
	char c, s[1010];

	scanf("%d\n", &N);
	for(int k=0; k<N; k++)
	{
		tot = 0;
		ans = 0;
		scanf("%d %[^\n]", &M, s);
		//printf("%d %s\n", M, s);
		
		for(int i=0; i<=M; i++)
		{	
			if(i==0)
				tot = (int) s[i] - '0';
			else
			{
				if(tot < i)
				{
					ans += i-tot;
					tot = i + ((int) s[i] - '0');
				}
				else
				{
					tot += ((int) s[i] - '0');
				}
			}
		}
		printf("Case #%d: %d\n", k+1, ans);
		//cout << "Case #" << k+1 << ": " << ans << endl;
	}
	return 0;
}
