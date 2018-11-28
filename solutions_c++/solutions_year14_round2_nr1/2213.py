#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int T, N, len, my_min, my_max, rez, sum;
char s[105][105];
int a[105][105];

void clear()
{
	for(int i=0; i<105; ++i)
		for(int j=0; j<=105; ++j)
			s[i][j] = -1;
	rez = 0;
	sum=0;
}

int main()
{	int tt, i, j, k, f, l;
	char str[105];

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for(tt=0; tt<T; ++tt)
	{
		scanf("%d", &N);
		clear();
		for(i=0; i<N; ++i)
		{
			scanf("%s", str);
			f=1;
			s[i][0] = str[0];
			for(k=0; k<i; ++k)					
				if(s[i][0] != s[k][0])
				{
					f=0;
					break;
				}
			a[i][0] = 1;
			l=1;
			len = strlen(str);
			j=0;
			while(f && l<len)
			{
				if(str[l] == str[l-1])
					a[i][j]++;
				else
				{
					++j;
					s[i][j] = str[l];
					for(k=0; k<i; ++k)					
						if(s[i][j] != s[k][j])
						{
							f=0;
							break;
						}
					a[i][j] = 1;
				}
				++l;
			}
			if(!f || (i>0 && s[i-1][j+1] != -1))
			{
				f=0;			
				break;
			}
		}
		if(!f)
			printf("Case #%d: Fegla Won\n", tt+1);
		else
		{
			for(i=0; i<=j; ++i)
			{
				my_min = 1000;
				my_max = 0;
				rez=0;
				for(k=0; k<N; ++k)
				{
					my_min = min(my_min, a[k][i]);
					my_max = max(my_max, a[k][i]);
				}
				rez = max(rez, my_max-my_min);
				sum += rez;
			}
			printf("Case #%d: %d\n", tt+1, sum);
		}
	}
	return 0;
}