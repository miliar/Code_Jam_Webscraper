#include<bits/stdc++.h>
using namespace std;

#define MAXN 1006

char str[MAXN];
deque < char > DQ;

int main()
{
	// freopen("data.txt", "r", stdin);
	freopen("Alarge.in", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	int t,T,i;
	scanf("%d", &T);
	for (t=1; t<=T; ++t)
	{
		scanf("%s", str);
		while (!DQ.empty()) DQ.pop_back();
		for (i=0; str[i]; ++i)
		{
			if (DQ.empty()) DQ.push_back(str[i]);
			else
			{
				if (str[i] >= DQ.front()) DQ.push_front(str[i]);
				else DQ.push_back(str[i]);
			}
		}
		printf("Case #%d: ", t);
		while (!DQ.empty())
		{
			putchar(DQ.front());
			DQ.pop_front();
		}
		puts("");
	}
	return 0;
}