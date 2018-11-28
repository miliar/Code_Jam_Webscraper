#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
using namespace std;
int T,caseNo;
int Max(int a,int b) {return a>b?a:b;}
int Min(int a,int b) {return a>b?b:a;}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Boutput.txt","w",stdout);
	for (scanf("%d", &T), caseNo=1; caseNo<=T; caseNo++)
	{
		int D, MaxP, P[1111], cnt[1111], ans;
		scanf("%d",&D);
		for (int i = 0; i < D; i++)
		{
			scanf("%d", &P[i]);
			MaxP = Max(MaxP, P[i]);
		}
		ans = MaxP;
		for (int i = 1; i < MaxP; i++)
		{
			int sum = 0;
			for (int j = 0 ; j < D; j++)
				sum += ((P[j]-1)/i);
			ans = Min(ans, sum + i);
		}
		printf("Case #%d: %d\n", caseNo, ans);
	}
//	system("pause");
	return 0;
}
