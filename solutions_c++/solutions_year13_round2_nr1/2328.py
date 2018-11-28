#include <stdio.h>
#include <stdlib.h>

int motes[256];

int compare_ints(const void* a, const void* b)
{
  const int *c = (const int *)a;
  const int *d = (const int *)b;
  if(*c < *d) return -1;
  if(*c > *d) return 1;
  return 0;
}

int add(int tam, int i, int n)
{
  if(i == n)
    return 0;

  if(tam > motes[i])
  {
    return add(tam+motes[i], i+1, n);
  }

  if(tam == 1)
  {
    return add(tam, i+1, n)+1;
  }

  int oper = add(tam+(tam-1), i, n)+1;
  int operrem = add(tam, i+1, n)+1;

  if(operrem < oper)
    oper = operrem;
  return oper;
}

//int remove(int tam, int i, int n)
//{
//  if(i == n)
//    return 0;

//  if(tam > motes[i])
//  {
//    return remove(tam+motes[i], i+1, n);
//  }

//}

int main(void)
{
  int t;
  scanf("%d",&t);

  for(int c(0); c < t; ++c)
  {
    printf("Case #%d: ",c+1);

    int a, n;
    scanf("%d %d", &a, &n);

    for(int i(0); i < n; ++i)
    {
      scanf("%d", &motes[i]);
    }

    qsort(motes, n, sizeof(motes[0]), compare_ints);

    int oper = 0;

    int i;
    for(i = 0; i < n; ++i)
    {
      if(a > motes[i])
      {
        a += motes[i];
      }
      else
      {
        break;
//        if(a+(a-1) > motes[i])
//        {
//          oper++;
//          a += (a-1);
//          a += motes[i];
//        }
//        else
//        {
//          oper++;
//        }
      }
    }


    //int operadd = add(a, i, n);

    oper = add(a, i, n);
    //if(operadd < oper)
      //oper = operadd;
//    if(a == 1)
//      oper = n;
//    else
//    {
//      for(int j(0); j < n-i; ++j)
//      int j = 0;
//      {
//        int k = 0;
//        katam[j][k] = a;
//        opers[j][k] = 0;
//        while(a < motes[i])
//        {
//          katam[j][++k] = a+(a-1);
//          opers[j][k] = opers[j][k-1];
//          a += (a-1);
//        }
//      }
//      for(int j(1); j < n-i; ++j)
//      {
//        for(int k(0); k < 20; ++k)
//        {
//          if(katam[j-1][k] > )
//        }
//      }
//    }

    printf("%d", oper);

    printf("\n");
  }

  return 0;
}
