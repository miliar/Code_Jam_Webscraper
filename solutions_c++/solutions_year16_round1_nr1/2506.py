#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(void)
{
  char S[1001];
  bool c[1001];
  int t;
  FILE *in = fopen("input.txt","r");
  FILE *out = fopen("output.txt","w");

  fscanf(in,"%d",&t);
  for (int l=0; l<t; l++)
  {
    fscanf(in,"%s",S);
    fprintf(out,"Case #%d: ", l+1);
    int length = strlen(S);
    char head = S[0];
    c[0] = true;
    for (int i=1; i<length; i++)
    {
      if (head <= S[i])
      {
        head = S[i];
        c[i] = true;
      }
      else
      {
        c[i] = false;
      }
    }
    for (int i=length-1; i>=0; i--)
    {
      if (c[i])
      {
        fprintf(out,"%c",S[i]);
      }
    }
    for (int i=1; i<length; i++)
    {
      if (!c[i])
      {
        fprintf(out,"%c",S[i]);
      }
    }
    fprintf(out,"\n");
  }
  return 0;
}
