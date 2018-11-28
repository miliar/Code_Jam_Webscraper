#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define MAX_N 20000
int S[MAX_N];
int main()
{
  int _T;
  scanf("%d",&_T);
  for(int _t = 1; _t <= _T;_t++)
    {
      int N,X;
      scanf("%d %d",&N,&X);
      for(int i = 0; i < N;i++)
	{
	  scanf("%d",&S[i]);
	}

      sort(S,S+N);
      int i = 0,j=N-1;
      int ans = 0;
      while(i <= j)
	{
	
	  if(S[i]+S[j] <= X)
	    i++;
	  ans++;
	  j--;
	}
      printf("Case #%d: %d",_t,ans);
      printf("\n");
    }
  return 0;
}
