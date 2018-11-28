//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>
using namespace std;
typedef long double LD;
const int N = 1003;

int t;
int n;
LD A[N];
LD B[N];

int main()
{
	scanf("%d", &t);
	for(int ti = 1;ti <= t;ti++)
	{
		scanf("%d", &n);
		for(int i = 1;i <= n;i++)
			scanf("%Lf", &A[i]);
		for(int i = 1;i <= n;i++)
			scanf("%Lf", &B[i]);
		sort(A+1,A+n+1);
		sort(B+1,B+n+1);

		int wyn1 = 0;
		{
			deque<LD> DA(A+1,A+n+1);
			deque<LD> DB(B+1,B+n+1);
			for(int i = 1;i <= n;i++)
			{
				if(DA.front() < DB.front())
				{
					DA.pop_front();
					DB.pop_back();
				}
				else
				{
					DA.pop_front();
					DB.pop_front();
					wyn1++;
				}
			}
		}

		int wyn2 = 0;
		{
			for(int i = n, j = n, buf = 0;i >= 1;i--)
			{
				while(j >= 1 && B[j] > A[i]) {j--;buf++;}
				if(buf > 0) buf--;
				else wyn2++;
			}
		}

		printf("Case #%d: %d %d\n", ti, wyn1, wyn2);
	}
	return 0;
}
