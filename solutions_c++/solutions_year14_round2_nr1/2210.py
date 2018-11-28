#include<stdio.h>
#include<math.h>
#include<cmath>
using namespace std;


int nod;
char dis[100];

bool update_freq(char s[], int fr[]);
bool update_freq(char s[], int fr[])
{
  if(s[0] != dis[0])
    return false;
  char *p = &s[1];
  int n = 1;
  fr[n-1]++;
  while(*p)
    {
      if(*p != dis[n-1])
	{
	  if(*p != dis[n])
	    return false;
	  n++;
	}
	fr[n-1]++;
	p++;
    }
  return n==nod;  
}


int main()
{
  int t, T;
  scanf("%d", &T);
  for(t=0;t<T;t++)
    {
      int N, i, j, k, freq[102][102]={0};
      char str[101][101];
      scanf("%d", &N);
      for(i=0;i<N;i++)
	{
	  scanf("%s", str[i]);
	}
      nod = 1;
      dis[0] = str[0][0];
      char *p = &str[0][1];
      while(*p)
	{
	  if(*p != dis[nod-1])
	    {
	      dis[nod] = *p;
	      nod++;
	    }
	  p++;
	}
      bool flag = true;
      for(i=0;i<N;i++)
	{
	  flag = flag && update_freq(str[i], freq[i]);
	  if(!flag)
	    break;
	}
      if(!flag)
	{
	  printf("Case #%d: Fegla Won\n", t+1);
	  continue;
	}


      // printf("%d\n", N);
      // for(i=0;i<N;i++)
      // 	{
      // 	  for(j=0;j<nod;j++)
      // 	    {
      // 	      for(k=0;k<freq[i][j];k++)
      // 		{
      // 		  printf("%c", dis[j]);
      // 		}
      // 	    }
      // 	  printf("\n");
      // 	}

      for(i=0;i<N;i++)
      	{
      	  for(j=0;j<nod;j++)
      	    {
      	      freq[N][j] += freq[i][j];
      	    }
      	}

      for(j=0;j<nod;j++)
	freq[N+1][j] = round((double)freq[N][j]/double(N));
      int ans = 0;
      for(j=0;j<nod;j++)
	{
	  for(i=0;i<N;i++)
	    {
	      ans += abs(freq[i][j] - freq[N+1][j]);
	    }
	}
      printf("Case #%d: %d\n", t+1, ans);
    }
}
