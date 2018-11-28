#include<cstdio>
#include<algorithm>
using namespace std;

#define DB if(0)

int D, tab[1003];



int minutes(int a)
{
	int ret = 0;
	for (int i = 0; i < D; i++)
	{
		if (tab[i] > a && tab[i]%a != 0)
			ret += tab[i]/a;
		else if (tab[i] > a)
			ret += tab[i]/a-1;
	}
	return ret;
}



int main ()
{
	int T,mx = 0, ans;
	scanf ("%d", &T);
	for (int q = 1; q <= T; q++)
	{
		mx = 0;
		ans = 1003;
		scanf ("%d", &D);
		for (int i = 0; i < D; i++)
		{
			scanf ("%d", &tab[i]);
			mx = max(mx, tab[i]);
		}
		for  (int i = 1; i <= mx; i++)
		{
			ans = min(ans, i + minutes(i));
			DB printf("i: %d ans: %d minutes: %d\n", i, ans, minutes(i));
			
		}
		printf("Case #%d: %d\n", q, ans);
	}
	return 0;
}