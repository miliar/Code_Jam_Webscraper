#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXS 2002

int cas,T,cnt[26],num[10];
char S[MAXS];

int main()
{
	freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		memset(S, 0, sizeof(S));
		scanf("%s", S);
		
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < (int)strlen(S); ++i)
		{
			++cnt[S[i]-'A'];
		}
		
		num[0] = cnt[25];
		cnt[4] -= cnt[25];
		cnt[14] -= cnt[25];
		cnt[17] -= cnt[25];
		cnt[25] = 0;
		
		num[2] = cnt[22];
		cnt[14] -= cnt[22];
		cnt[19] -= cnt[22];
		cnt[22] = 0;
		
		num[4] = cnt[20];
		cnt[5] -= cnt[20];
		cnt[14] -= cnt[20];
		cnt[17] -= cnt[20];
		cnt[20] = 0;
		
		num[6] = cnt[23];
		cnt[8] -= cnt[23];
		cnt[18] -= cnt[23];
		cnt[23] = 0;
		
		num[8] = cnt[6];
		cnt[4] -= cnt[6];
		cnt[7] -= cnt[6];
		cnt[8] -= cnt[6];
		cnt[19] -= cnt[6];
		cnt[6] = 0;
		
		num[7] = cnt[18];
		cnt[4] = cnt[4] - cnt[18]*2;
		cnt[13] -= cnt[18];
		cnt[21] -= cnt[18];
		cnt[18] = 0;
		
		num[5] = cnt[21];
		cnt[4] -= cnt[21];
		cnt[5] -= cnt[21];
		cnt[8] -= cnt[21];
		cnt[21] = 0;
		
		num[1] = cnt[14];
		cnt[13] -= cnt[14];
		cnt[4] -= cnt[14];
		cnt[14] = 0;
		
		num[3] = cnt[19];
		cnt[4] = cnt[4] - cnt[19]*2;
		cnt[7] -= cnt[19];
		cnt[17] -= cnt[19];
		cnt[19] = 0;
		
		num[9] = cnt[13]/2;
		
		printf("Case #%d: ", cas);
		for (int i = 0; i < 10; ++i)
		{
			if(num[i] > 0)
			{
				for(int j = 0; j < num[i]; ++j)
				{
					printf("%d", i);
				}
			}
		}
		printf("\n");
	}
	
	return 0;
}