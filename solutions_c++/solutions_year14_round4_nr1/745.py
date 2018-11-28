#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAXN = 10010;
int v[MAXN];
bool picked[MAXN];

int main()
{
  int t;
  scanf("%d",&t);
  for(int case_num = 1; case_num <= t; case_num++)
    {
      printf("Case #%d: ",case_num);
      int n,c;
      scanf("%d%d",&n,&c);
      for(int i = 0; i < n; i++) scanf("%d",&v[i]);

      memset(picked,false,sizeof(picked));
      
      sort(v,v + n);

      int ans = 0;
      for(int i = n-1; i >= 0; i--)
	if (!picked[i])
	  {
	    ++ans;
	    
	    int j;
	    for(j = i-1; j >= 0; j--)
	      if (!picked[j] && v[i] + v[j] <= c)
		{
		  picked[j] = true;
		  break;
		}
	  }

      printf("%d\n",ans);
    }
  return 0;
}
