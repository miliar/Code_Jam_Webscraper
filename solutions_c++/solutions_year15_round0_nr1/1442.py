#include <iostream>
#include <cstdio>

using namespace std;

int T;
int SMAX;
const int MAXN = 1000+10;
int N;

char Buf[MAXN];

int Solve()/////////////////////////////////////
{
	int ans = 0;
	int tmp = 0;

	int len = strlen(Buf);

	for(int i=0;i<=SMAX;i++)
	{
		if(Buf[i]!= '0')
		{
			int t = 0;

			if(tmp < i)
			{
				t = i-tmp;
				ans += t;
			}

			tmp += Buf[i]-'0'+t;
	
		}
	}

	return ans;
}

int main()////////////////////////////////////
{
//	freopen("..\\A-small-attempt0.in","r",stdin);
//	freopen("..\\A-small-attempt0.out","w",stdout);

	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);


	int d = 1;
	cin >> T;

	while(T--)
	{
		cin >> SMAX;
		getchar();

		gets(Buf);

		int ans = Solve();

		printf("Case #%d: %d\n",d++,ans);


	}
	return 0;
}