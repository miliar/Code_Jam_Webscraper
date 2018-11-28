#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> pii;

int n;
vector<double> naomi,ken;

int playWar()
{
  pii naomiP=pii(0,n-1),kenP=pii(0,n-1);
  int ans = 0;
  for(int i = n-1; i >=0;i--)
    {
      if(naomi[naomiP.second] > ken[kenP.second])
	{
	  kenP.first++;
	  naomiP.second--;
	  ans++;
	}
	else
	  {
	    naomiP.second--;
	    kenP.second--;
	  }
    }
  return ans;
}

int playDW()
{
  pii naomiP=pii(0,n),kenP=pii(0,n);
  int ans = 0;
  for(int i = 0; i < n;i++)
    {
      if(naomi[naomiP.first] < ken[kenP.first])
	{
	  kenP.second--;
	  naomiP.first++;
	}
	else
	  {
	    naomiP.first++;
	    kenP.first++;
	    ans++;
	  }
    }
  return ans;
}
int main()
{
  int T;
  scanf(" %d",&T);
  for(int t = 1; t <= T;t++)
    {
      naomi.clear();
      ken.clear();
      scanf("%d",&n);
      ken.resize(n);
      naomi.resize(n);
      for(int i = 0; i < n;i++)
	scanf("%lf",&naomi[i]);
      for(int i = 0; i < n;i++)
	scanf("%lf",&ken[i]);

      sort(naomi.begin(),naomi.end());
      sort(ken.begin(),ken.end());

      printf("Case #%d: %d %d\n",t,playDW(),playWar());
    }
  return 0;
}
