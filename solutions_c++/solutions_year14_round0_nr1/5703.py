#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int v[20];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Count; cin >> Count;
	for(int T = 1; T <= Count; ++T)
	{
		memset(v, 0 ,sizeof(v));
		int k; cin >> k;
		for(int i = 1; i <= 4; ++i)
			for(int j = 1; j <= 4; ++j)
			{
				int x;
				cin >> x;
				if(i == k) ++v[x];
			}
		cin >> k;
		for(int i = 1; i <= 4; ++i)
			for(int j = 1; j <= 4; ++j)
			{
				int x;
				cin >> x;
				if(i == k) ++v[x];
			}
		int ans = -1;
		for(int i = 1; i <= 16; ++i)
			if(v[i] == 2)
				if(ans < 0)
					ans = i;
				else
					ans = 0;
		printf("Case #%d: ",T);
		if(ans == 0)
			printf("Bad magician!\n");
		else if(ans < 0)
			printf("Volunteer cheated!\n");
		else
			printf("%d\n",ans);
	}
}
