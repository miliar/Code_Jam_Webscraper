#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
using namespace std;
int T,caseNo;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Aoutput.txt","w",stdout);
	for (scanf("%d", &T), caseNo=1; caseNo<=T; caseNo++)
	{
		int n, sum = 0, ans = 0;
		char ch;
		scanf("%d%c", &n, &ch);
		for (int i=0; i<=n; i++)
		{
			scanf("%c", &ch);
			if (sum<i) {ans += (i-sum); sum = i;}
			sum += (ch-'0');
//			printf("%d\n", sum);
		}
		printf("Case #%d: %d\n", caseNo, ans);
		scanf("%c", &ch);
	}
//	system("pause");
	return 0;
}
