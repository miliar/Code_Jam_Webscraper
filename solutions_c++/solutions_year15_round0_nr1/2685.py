#include <stdio.h>
#include <vector>
#include <algorithm>

int main()
{
  int T, t;
  scanf("%d", &T);
  for(t=1; t<=T; t++)
    {
      int N, i, before_aud=0, added_aud=0;
      char S[1002];
      scanf("%d %s", &N, S);
      for(i=0; i<=N; i++)
	{
	  if(before_aud < i)
	    {
	      added_aud += (i-before_aud);
	      before_aud = i;
	    }
	  before_aud += S[i]-'0';
	}
      printf("Case #%d: %d\n", t, added_aud);
    }
}
