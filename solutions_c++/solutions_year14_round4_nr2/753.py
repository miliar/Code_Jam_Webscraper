#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int v[MAXN];
pair<int,int> slst[MAXN];
int rank_seq[MAXN],rank_v[MAXN];


int dp[MAXN][MAXN];

int preSum[MAXN],postSum[MAXN];

int sval[MAXN];

int main()
{
  int t;
  scanf("%d",&t);
  for(int case_num = 1; case_num <= t; case_num++)
    {
      printf("Case #%d: ",case_num);
      int n;
      scanf("%d",&n);
      for(int i = 0; i < n; i++)
	{
	  scanf("%d",&v[i]);
	  slst[i] = make_pair(v[i],i);
	}
      sort(slst,slst + n);
      for(int i = 0; i < n; i++) 
	{
	  rank_v[i] = slst[i].second;
	  v[slst[i].second] = i;
	}

      int ans = 0;
      for(int i = 0; i < n; i++)
	{
	  int s = 0;
	  for(int j = 0; j < i; j++)
	    if (v[j] > v[i]) ++s;
	  preSum[i] = s;

	  s = 0;
	  for(int j = i + 1; j < n; j++)
	    if (v[j] > v[i]) ++s;
	  postSum[i] = s;

	  ans += min(preSum[i], postSum[i]);
	}


      printf("%d\n",ans);
    }
  return 0;
}
