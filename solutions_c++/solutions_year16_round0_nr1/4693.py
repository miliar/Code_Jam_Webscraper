#include <bits/stdc++.h>

using namespace std;

bool cek[15];

int main()
{
	int t;
	scanf("%d\n",&t);
	for (int c=1;c<=t;c++)
	{
		for (int i=0;i<=9;i++) cek[i]=false;
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",c);
		if (n!=0)
		{
			int cur = n;
			bool finish = false;
			int cnt = 0;
			do
			{
				int temp = cur;
				while (temp>0)
				{
					cek[(temp%10)] = true;
					temp = temp/10;
				}

				finish = true;
				for (int i=0;i<=9;i++)
				{
					if (!cek[i]) finish = false;
				}

				if (!finish) cur+=n;
			}
			while (!finish);

			printf("%d\n",cur);
		}
		else
		{
			printf("INSOMNIA\n");
		}
	}
	return 0;
}