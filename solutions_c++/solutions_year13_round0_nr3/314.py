
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <NTL/ZZ.h>

typedef NTL::ZZ BigInt;

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64_t;

BigInt  N, M;
BigInt  fair_sq[50000];
int  fair_sq_count = 0;

int CountUntil(BigInt n)
{
    int low = 0;
    int high = fair_sq_count - 1;
    while(low <= high)
    {
        int mid = (low + high)/2;
        if (fair_sq[mid] > n)
            high = mid - 1;
        else if (fair_sq[mid] < n)
            low = mid + 1;
        else
            return mid;
    }

    return high;
}

int gen[101];

void print_gen(int digit)
{
    for(int i=0; i<digit/2; i++)
        printf("%d", gen[i]);
    if (digit%2 == 1)
        printf("%d", gen[digit/2]);
    for(int i=0; i<digit/2; i++)
        printf("%d", gen[digit/2-1-i]);
    printf("\n");
}

void AddFairSq(int digit)
{
    BigInt  num;
    num = 0;
    for(int i=0; i<digit/2; i++)
        num = num*10 + gen[i];
    if (digit%2 == 1)
        num = num*10 + gen[digit/2];
    for(int i=0; i<digit/2; i++)
        num = num*10 + gen[digit/2-1-i];
    fair_sq[fair_sq_count] = num*num;
    fair_sq_count++;
}


void build(int digit, int remain)
{
    //print_gen(digit);
    AddFairSq(digit);
    if (digit%2 == 1 && gen[digit/2] == 1 && remain >= 3)
    {
        gen[digit/2] = 2;
        //print_gen(digit);
        AddFairSq(digit);
    }
}

#define  FOR(N1,N)  for(int a##N=0; a##N<2; a##N++) \
    { \
        int ck##N = ck##N1 - a##N;\
        if (d > N*2+1)\
            ck##N -= a##N;\
        if (ck##N < 0)\
            break;\
        gen[N] = a##N;\
        if (d <= N*2+2)\
        {\
            build(d, ck##N);\
            continue;\
        }

#define  ENDFOR   }

void BuildFairSq()
{
    gen[0] = 0;
    build(1, 0);
    gen[0] = 1;
    build(1, 8);
    gen[0] = 3;
    build(1, 0);
    gen[0] = 1;
    build(2, 7);
    gen[0] = 2;
    build(2, 5);
    
    for(int d=3; d<=50; d++)
    {
        for(int a0=1; a0<2; a0++)
        {
            int ck0 = 9 - a0*2;
            gen[0] = a0;
//            for(int a1=0; a1<2; a1++)
//            {
//                int ck1 = ck0 - a1;
//                if (d > 1*2+1)
//                    ck1 -= a1;
//                if (ck1 < 0)
//                    break;
//                gen[1] = a1;
//                if (d <= 1*2+2)
//                {
//                    build(d, ck1);
//                    continue;
//                }
            FOR(0,1)
            FOR(1,2)
            FOR(2,3)
            FOR(3,4)
            FOR(4,5)
            FOR(5,6)
            FOR(6,7)
            FOR(7,8)
            FOR(8,9)
            FOR(9,10)
            FOR(10,11)
            FOR(11,12)
            FOR(12,13)
            FOR(13,14)
            FOR(14,15)
            FOR(15,16)
            FOR(16,17)
            FOR(17,18)
            FOR(18,19)
            FOR(19,20)
            FOR(20,21)
            FOR(21,22)
            FOR(22,23)
            FOR(23,24)
            ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR
            ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR
            ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR
            ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR  ENDFOR
        }
        gen[0] = 2;
        for(int i=1; i<d/2+1; i++)
            gen[i] = 0;
        build(d, 1);
        if (d%2 == 1)
        {
            gen[d/2] = 1;
            build(d, 0);
        }
    }
}

int main()
{
    fgets(buf, 1024, stdin);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
    BuildFairSq();
    
   
	for(int i=1; i<=ncase; i++)
	{
        // input data
        std::cin >> N >> M;
 
        // go
        int ans = CountUntil(M) - CountUntil(N-1);

		printf("Case #%d: %d", i, ans);

		printf("\n");
	}
  
	return  0;  
}
