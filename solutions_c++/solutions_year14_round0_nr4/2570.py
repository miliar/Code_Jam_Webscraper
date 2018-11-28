#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int p[] = {0,1,0,1,0,1,2,2};
const int q[] = {0,0,1,1,2,2,0,1};

double naomi[1111];
double ken[1111];

int main(void)
{
	int T = 0;
	scanf("%d",&T);
	int TK = 0;
	while(T--)
	{
		printf("Case #%d: ",++TK);
		int N = 0;
		scanf("%d",&N);
		for(int i = 0;i < N;i++) scanf("%lf",&naomi[i]);
		for(int i = 0;i < N;i++) scanf("%lf",&ken[i]);

		sort(naomi,naomi+N);
		sort(ken,ken+N);
		for(int i = N;i >= 0;i--)
		{
			bool okay = true;
			for(int j = 0;j < i;j++)
			{
				if(naomi[N-i+j] < ken[j])
				{
					okay = false;
					break;
				}
			}
			if(okay) { printf("%d ",i); break; }
		}

		reverse(naomi,naomi+N);
		reverse(ken,ken+N);
		int l1 = 0;
		int l2 = 0;
		for(int i = 0;i < N;i++)
		{
			if(naomi[i] > ken[l1]) l2++;
			else l1++;
		}
		printf("%d\n",l2);
	}
	while(getchar() != EOF);
	return 0;
}