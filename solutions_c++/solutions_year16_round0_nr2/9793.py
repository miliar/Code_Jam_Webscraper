#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<int,int> pii;

char str[105];

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		int ans = 0;
		scanf("%s",str);		
		
		int n = strlen(str);
		bool up = true;
		for (int i = 0; i < n; ++i)
		{
			if (str[i] == '-')
			{
				if (up == true)
				{
					if (i != 0)
						++ans;
						
					++ans;
				}
					
				up = false;
			}
			else
				up = true;
		}
		
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
