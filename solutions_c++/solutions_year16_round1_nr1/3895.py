#include <cstdio>

void print (char *out, int left, int right)
{
  for(int i=left;i<=right;i++)
  {
    printf("%c",out[i]);
  }
  printf("\n");
}

int main()
{
  int T;
  scanf("%d",&T);
  char ch;
  int start = 1000;
  int left = 1000;
  int right = 1000;
  char out[2000];
  scanf("%*c");
  scanf("%c",&ch);

  out[start] = ch;
  for(int i=0;i<T;)
  {


    scanf("%c",&ch);
    if( ch == '\n' || ch == '\r')
    {
      printf("Case #%d: ",i+1);
      print(out,left,right);
      start = 1000;
      left = 1000;
      right = 1000;
      if ( i != T-1){
        scanf("%c",&ch);
        out[start] = ch;
      }
      i++;


    }
    else{
      if( ch >= out[left] )
        out[--left] = ch;
      else
        out[++right] = ch;
    }

  }
  return 0;
}
