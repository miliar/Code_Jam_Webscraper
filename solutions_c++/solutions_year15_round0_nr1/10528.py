#include <bits/stdc++.h>

using namespace std;

int smash[1010];

int main()
{
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  int T ; cin >> T;
  for(int i = 0 ; i < T ; ++i)
    {
      int n,ans=0; string p; cin >> n >> p;
      memset(smash , 0 , sizeof smash);
      smash[0]  = p[0]-'0';
      for(int k = 1 ; k <= n; ++k)
	{
	  if(k > smash[k-1] and p[k]-'0' != 0)	   //los que faltan
	    {
	      // cout <<"k : " <<  k << smash[k-1] << " de los que entraron" << endl;
	      ans += k-smash[k-1];
	      smash[k] +=  ans;
	    }
	  smash[k] +=  smash[k-1] + p[k] - '0';
	}
      printf("Case #%d: %d\n",i+1,ans);
    }
  return 0;
}
