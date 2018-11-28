#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
int ps[1010];
bool pls(int i)
{
	char s[100];
	sprintf(s,"%d", i);
	int l = strlen(s),k,p;
	for(k = 0, p = l-1; k <= p; k++, p--)
		if(s[k]!=s[p])
			return 0;
	return 1;
}
int main()
{
	int t;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	for(int i = 1; i<=1000; i++)
	{
		if(pls(i))
		{
			int q = (int)sqrt((double)i);
			if(q*q == i && pls(q))
			{
				ps[0]++;
				ps[ps[0]] = i;
			}
		}
	}
	scanf("%d\n", &t);
	for(int ii = 1; ii<=t; ii++)
	{
		printf("Case #%d: ",ii);
		int a,b, cnt = 0;
		scanf("%d %d\n", &a, &b);
		for(int i = 1; i<=ps[0]; i++)
			if(ps[i] >= a && ps[i] <= b)
				cnt ++;
		printf("%d\n", cnt);
	}
	return 0;
}