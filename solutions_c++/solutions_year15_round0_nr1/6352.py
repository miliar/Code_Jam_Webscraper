#include <bits/stdc++.h>

using namespace std;

int ft[1001];

int query(int pos)
{
	int ans = 0;
	while(pos)
	{
		ans+=ft[pos];
		pos-=pos&(-pos);
	}
	return ans;
}

void upd(int pos, int val)
{
	while (pos <= 1000)
	{
		ft[pos]+=val;
		pos+=pos&(-pos);
	}
}

int main()
{
	int t, tc = 1;
	int len, i;
	char str[1001];
	int ans;
	int p;
	int zero;
	int q;
	
	scanf("%d", &t);
	
	while(tc <= t)
	{
		ans = 0;
		memset(ft, 0, sizeof(ft));
		
		scanf("%d", &len);
		len++;
		scanf("%s", str);
		
		
		for (i = 0; i < len; i++)
		{
			p = (str[i]-'0');
			if (i == 0)
				zero = p;
			else
				upd(i, p);
				
		}
		
		for (i = 1; i < len; i++)
		{
			if (str[i] != '0')
			{
				q = query(i-1) + zero;
				if(q < i)
				{
					ans += i-q;
					zero += i-q;
				}
			}
		}
		printf("Case #%d: %d\n",tc, ans);
	
		
		
		tc++;
	}
	return 0;
}
