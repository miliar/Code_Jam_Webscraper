#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

#define U8  uint8_t	
#define U16 uint16_t	
#define U32 uint32_t	
#define U64 uint64_t

#define S8  int8_t
#define S16 int16_t
#define S32 int32_t
#define S64 int64_t

U32 motes[101];
U32 ate[101];

U32 d;

void eat(U32 list[101], U64 &Cur, U32 N)
{
  int q = 0;

  for (U32 c = 0;c < N;c++)
    {
      if ((Cur > list[c]) && (list[c] != 0))
        {
          Cur += list[c];
          list[c] = 0;
          q++;
        }
    }

  //repeat
  while (q > 0)
    {
      q = 0;
      for (U32 c = 0;c < N;c++)
        {
          if ((Cur > list[c]) && (list[c] != 0))
            {
              Cur += list[c];
              list[c] = 0;
              q++;
            }
        }
    }
}

U32 left(U32 list[101], U32 N)
{
  U32 q = 0;
  for (U32 c = 0;c < N;c++)
    if (list[c] > 0) q++;

  return q;
}


U32 findbig(U32 list[101], U32 N)
{
  U32 tempval, temploc;

  tempval = 0;
  temploc = 0;


  for (U32 c = 0;c < N;c++)
    {
      if ((list[c] > tempval) && (list[c] != 0))
        {
          tempval = list[c];
          temploc = c;
        }
    }

  return temploc;
}


void printlist(U32 list[101], U32 N)
{
  printf("#%I32u#:", N);
  for (U32 c = 0;c < N;c++)
    printf("%I32u,", list[c]);
  printf("\n");
}

int dfs(U32 list[101], U64 Size, U32 N)
{
  U32 templist[101];
  U32 retbig, retsmall;


  d++;
//  printf("d=%I32u:", d);
//  printf("S=%I64u", Size);
//  printlist(list, N);
  eat(list, Size, N);
//  printf("S=%I64u", Size);
//  printlist(list, N);


  if (left(list, N) == 1)
    {
      d--;
      return 1;
    }

  if (left(list, N) > 0)
      {
//        printf("left=%I32u:", left(list, N));
        //remove biggest
        memcpy(templist, list, sizeof(templist));
        templist[findbig(templist, N)] = 0;

//        printf("big:%I32u", temploc);
//        printf("call big..");
        retbig = dfs(templist, Size, N);
//        printf(".end big = %I32u\n", ret1);

        //compare to add smallest
        //restore old val
        memcpy(templist, list, sizeof(templist));
        templist[N] = Size-1;
        if (Size > 1)
          retsmall = dfs(templist, Size, N+1);
        else retsmall = retbig+1;

        if (retbig > retsmall)
          {
            d--;
            return (retsmall+1);
          }
        else
          {
            d--;
            return retbig+1;
          }
      }

    d--;
    return 0;
}


int main()
{

    int Z, C;
    U64 A, ans;
    U32 N;

    scanf("%i\n", &Z);
//    printf("Count: %I32u\n", Z);

    for (C = 1;C <= Z;C++)
    {
        scanf("%I64u %I32u\n", &A, &N);

        memset(motes, 0, sizeof(motes));
        memset(ate, 0, sizeof(ate));

//        printf("S = %I64u, N = %I32u\n", A, N);

        for (U32 c = 0;c < N;c++)
          scanf("%I32u\n", &motes[c]);

        eat(motes, A, N);

        if(left(motes, N) > 0)
          {
            ans = dfs(motes, A, N);
          } else ans = 0;


        printf("Case #%I32u: %I64u\n", C, ans);

    }


    return 0;
}
