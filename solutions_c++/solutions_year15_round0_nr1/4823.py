#include<iostream>
#include<cstdio>
#include<cstdlib>
#include <string.h>
#include<string>
#include<vector>
#include<set>
using namespace std;
typedef long long ll;
char A[1005];
int main()
{
	freopen("in_1_large.txt", "r", stdin);
	freopen("out_1_large.txt", "w", stdout);
	int T,S,sum=0,frnd=0;
	scanf("%d", &T);
	for (int TC = 1; TC <= T;++TC)
	{
		scanf("%d %s", &S,A);
		sum = 0,frnd=0;
		for (int i = 0; i <= S; ++i)
		{
			int a = A[i] - '0';
			if (a == 0)
				continue;
			if ((sum + frnd) >= i){
				sum += a;
			}
			else
			{
				int tt = (i - sum-frnd);
				frnd += tt;
				sum += a;
			}
		}

		printf("Case #%d: %d\n", TC, frnd);

	}
	return 0;
}