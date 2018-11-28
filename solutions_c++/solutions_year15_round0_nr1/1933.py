#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    int T;
    cin >>T;
    for(int iCase=1;iCase<=T;iCase++)
	{
		int n;
		scanf("%d", &n);
		char s[1010];
		scanf("%s", s);
		int sum = 0, ans = 0;
		for(int i=0;i<=n;i++)
		{
            if(sum>=i)
				sum+=s[i] - '0';
			else
			{
				ans += i - sum;
				sum = i+s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", iCase, ans);
	}

    return 0;
}
