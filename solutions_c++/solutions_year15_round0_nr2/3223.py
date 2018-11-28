#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int Count[1024], Rec[1024];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int n;
	int cas, t;
	scanf("%d", &t);
	for(cas = 1; cas <= t; cas ++)
	{
		scanf("%d", &n);
		int ans = 0;
		memset(Count, 0, sizeof(Count));
		for(int i= 0; i < n; i ++)
		{
			int d;
			scanf("%d", &d);
			Count[d] ++;
			ans = max(ans, d);
		}
		
		for(int i = 1000; i >= 1; i --)Rec[i] = Count[i];
		for(int i = 1000; i >= 1; i --)
		{
            if(i >= ans)continue;
            for(int j = 1000; j >= 1; j --)Count[j] = Rec[j];
            int step = 0;
            for(int j = 1000; j > i; j --)
            {
                while(Count[j] > 0)
                {
				    Count[j] --;
				    Count[i] ++;
				    Count[j-i] ++;
				    step ++;
			    }
            }
            //printf("%d %d\n", i, step);
            ans = min(ans, i+step);
		}
		
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
