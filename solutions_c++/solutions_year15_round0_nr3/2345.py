#include <stdio.h>

int main()
{
  int T, t;
  char m[256][256];
  m['i']['i'] = '-';
  m['i']['j'] = 'k';
  m['i']['k'] = 'J';
  m['i']['I'] = '+';
  m['i']['J'] = 'K';
  m['i']['K'] = 'j';
  m['i']['+'] = 'i';
  m['i']['-'] = 'I';

  m['j']['i'] = 'K';
  m['j']['j'] = '-';
  m['j']['k'] = 'i';
  m['j']['I'] = 'k';
  m['j']['J'] = '+';
  m['j']['K'] = 'I';
  m['j']['+'] = 'j';
  m['j']['-'] = 'J';

  m['k']['i'] = 'j';
  m['k']['j'] = 'I';
  m['k']['k'] = '-';
  m['k']['I'] = 'J';
  m['k']['J'] = 'i';
  m['k']['K'] = '+';
  m['k']['+'] = 'k';
  m['k']['-'] = 'K';

  m['I']['i'] = '+';
  m['I']['j'] = 'K';
  m['I']['k'] = 'j';
  m['I']['I'] = '-';
  m['I']['J'] = 'k';
  m['I']['K'] = 'J';
  m['I']['+'] = 'I';
  m['I']['-'] = 'i';

  m['J']['i'] = 'k';
  m['J']['j'] = '+';
  m['J']['k'] = 'I';
  m['J']['I'] = 'K';
  m['J']['J'] = '-';
  m['J']['K'] = 'i';
  m['J']['+'] = 'J';
  m['J']['-'] = 'j';

  m['K']['i'] = 'J';
  m['K']['j'] = 'i';
  m['K']['k'] = '+';
  m['K']['I'] = 'j';
  m['K']['J'] = 'I';
  m['K']['K'] = '-';
  m['K']['+'] = 'K';
  m['K']['-'] = 'k';

  m['+']['i'] = 'i';
  m['+']['j'] = 'j';
  m['+']['k'] = 'k';
  m['+']['I'] = 'I';
  m['+']['J'] = 'J';
  m['+']['K'] = 'K';
  m['+']['+'] = '+';
  m['+']['-'] = '-';

  m['-']['i'] = 'I';
  m['-']['j'] = 'J';
  m['-']['k'] = 'K';
  m['-']['I'] = 'i';
  m['-']['J'] = 'j';
  m['-']['K'] = 'k';
  m['-']['+'] = '-';
  m['-']['-'] = '+';

  scanf("%d", &T);
  for(t=1; t<=T; t++)
    {
      int L, i, j, k, xmd;
      long long X;
      char A[10002], ml='+', xml='+', t1='+';
      bool flag_done = false;
      scanf("%d %lld", &L, &X);
      scanf("%s", A);
      for(i=0; i<L; i++)
	ml = m[ml][A[i]];
      xmd = X%4;
      for(i=0; i<xmd; i++)
	xml = m[xml][ml];
      if(xml != '-')
	printf("Case #%d: NO\n", t);
      else
	{
	  char tofind = 'i';
	  for(i=0; i<12; i++)
	    {
	      for(j=0; j<L; j++)
		{
		  t1 = m[t1][A[j]];
		  if(t1 == tofind)
		    {
		      if(tofind == 'k')
			{
			  flag_done = true;
			  break;
			}
		      else
			{
			  t1 = '+';
			  tofind++;
			}
		    }
		}
	      if(flag_done)
		break;
	    }
	  if(flag_done && i<X)
	    printf("Case #%d: YES\n", t);
	  else
	    printf("Case #%d: NO\n", t);
	}
    }
}
