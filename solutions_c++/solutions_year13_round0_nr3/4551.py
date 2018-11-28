#include <iostream>

using namespace std;

int temp[110];

bool check(int now)
{
	int co = 0;
	while(now)
	{
		temp[co++] = now % 10;
		now /= 10;
	}
	for(int i = 0; i <= co / 2 && i < co; ++i)
		if(temp[i] != temp[co - 1 - i])
			return false;
	return true;
}

int main(void)
{
	int t, a, b;
	//freopen("D:\C-small-attempt0.in", "r", stdin);
	//freopen("D:\C-ans.out", "w", stdout);
	int Ca = 0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %d", &a, &b);
		int sa, sb, be, en;
		sa = sqrt(a * 1.0);
		if(sa * sa >= a)
			be = sa;
		else be = sa + 1;
		sb = sqrt(b * 1.0);
		if(sb * sb <= b)
			en = sb;
		else
			en = sb - 1;
		int cnt = 0;
		for(int i = be; i <= en; ++i)
		{
			if(check(i) && check(i * i))
				cnt++;
		}
		printf("Case #%d: ", ++Ca);
		printf("%d\n", cnt);
	}
	return 0;
}