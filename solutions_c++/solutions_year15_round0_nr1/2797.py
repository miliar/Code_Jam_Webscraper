#include <cstdio>
#include <cstring>

int main()
{
  int T = 0;
  scanf("%d", &T);
  for (int casei = 1; casei <= T; casei++)
	{
	  int MINS = 0;
	  char tmps[2000];
	  scanf("%d %s", &MINS, tmps);
	  int n = strlen(tmps);
	  for (int ans = 0; ans <= n; ans++)
		{
		  // we're adding 'ans' extras
		  int sum = ans;
		  int totalCount = 0;
		  for (int i = 0; i < n; i++)
			{
			  totalCount += tmps[i] - '0';
			  if (i <= sum)
				{
				  sum += tmps[i] - '0';
				}
			}
		  if (sum >= totalCount + ans)
			{
			  printf("Case #%d: %d\n", casei, ans);
			  break;
			}
		}
	}

  return 0;
}
