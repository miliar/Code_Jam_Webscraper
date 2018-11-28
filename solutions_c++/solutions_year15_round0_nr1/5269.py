#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	long long smax;
	char s[1001];
	for(int t1 = 1;t1<=T;t1++)
	{
		scanf("%lld", &smax);
		scanf("%s", s);
		//cin>>s;
		long long cur = 0;
		long long cnt = 0;
		for(int i=0;i<=smax;i++)
		{
			if(i == 0)
				cur += (s[i] - '0');
			else
			{
				if(cur<i)
				{
					cnt = cnt + (i - cur);
					cur = i;
					cur += (s[i] - '0');
				}
				else
					cur += (s[i] - '0');
			}
		}
		printf("Case #%d: %lld\n", t1, cnt);
	}
	system("Pause");
	return 0;
}
