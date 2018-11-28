#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int T = 0;
  scanf("%d", &T);
  for (int casei = 1; casei <= T; casei++)
	{
	  int n = 0;
	  scanf("%d", &n);
	  vector<int> original;
	  for (int i = 0; i < n; i++)
		{
		  int x;
		  scanf("%d", &x);
		  original.push_back(x);
		}

	  int bestans = 10000;
	  for (int t = 1; t <= 1000; t++)
		{
		  // everyone's eating for t time at most
		  int nsplits = 0;
		  for (int i = 0; i < original.size(); i++)
			{
			  // no need to split?
			  if (original[i] <= t)
				continue;
			  if (original[i] % t != 0)
				{
				  nsplits += original[i]/t;
				}
			  else
				{
				  nsplits += original[i]/t - 1;
				}
			}
		  bestans = min(bestans, t + nsplits);
		}

	  printf("Case #%d: %d\n", casei, bestans);
	}

  return 0;
}
