#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXN = 1010;
double ma[MAXN],mb[MAXN];

bool used[MAXN];

int main()
{
  int case_tot;
  scanf("%d",&case_tot);
  for(int case_i = 1; case_i <= case_tot; case_i++)
    {
      printf("Case #%d: ",case_i);

      int n;
      scanf("%d",&n);
      
      for(int i = 0; i < n; i++) scanf("%lf",&ma[i]);
      for(int i = 0; i < n; i++) scanf("%lf",&mb[i]);
      sort(ma,ma + n);
      sort(mb,mb + n);

      int ans = 0;
      for(int d = 0; d < n; d++)
	{
	  int res = 0;
	  for(int i = n - 1,j = n - 1 - d; j >= 0; i--,j--)
	    if (ma[i] > mb[j]) ++res;
	  ans = max(ans,res);
	}
      
      int ansWar = 0;
      memset(used,false,sizeof(used));
      for(int i = 0,j,mp = 0; i < n; i++)
	{
	  for(; mp < n && used[mp]; ++mp);
	  for(j = mp; j < n && (used[j] || mb[j] < ma[i]); j++);
	  if (j == n)
	    {
	      used[mp] = true;
	      ++ansWar;
	    }
	  else
	    {
	      used[j] = true;
	    }
	}

      printf("%d %d\n",ans,ansWar);
    }
  return 0;
}
