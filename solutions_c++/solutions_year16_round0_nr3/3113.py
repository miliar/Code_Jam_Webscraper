#include<stdio.h>
#include<math.h>
#define TRUE 1
#define FALSE 0

int f(long n, long *num)
{
  long j;
  for(j=2;j<=sqrt(n);j++)
  {
     if(n%j==0)
     {
       *num = j;
       return TRUE; 
     }
  }
  return FALSE;
}

void get_coin(int n, int j, char soln[], int k, long b2,long b3,long b4,long b5,long b6,long b7,long b8,long b9,long b10, int *count)
{
   if(*count ==j )
   {
     return;
   }
   else if(n==k)
   {
     int i,j;
     int is_exist=TRUE;
     long num2 = 0;
     long num3 = 0;
     long num4 = 0;
     long num5 = 0;
     long num6 = 0;
     long num7 = 0;
     long num8 = 0;
     long num9 = 0;
     long num10 = 0;

//       printf("%s %ld %ld %ld %ld %ld %ld %ld %ld %ld\n",soln,b2,b3,b4,b5,b6,b7,b8,b9,b10);
       #if 1
     if(f(b2,&num2) && f(b3,&num3) && f(b4,&num4) && f(b5,&num5) && f(b6,&num6) && f(b7,&num7) && f(b8,&num8) && f(b9,&num9) && f(b10,&num10))
     {
       soln[k]=0;
       printf("%s %ld %ld %ld %ld %ld %ld %ld %ld %ld ",soln,num2,num3,num4,num5,num6,num7,num8,num9,num10);
       printf("\n");
       (*count)++;
     }
     #endif
   }
   else
   {
     if( (k==0) || (k == n-1) )
     {
       soln[k]='1';
       get_coin(n,j,soln,k+1,
                b2+(pow(2,n-1-k)*1),
                b3+(pow(3,n-1-k)*1),
                b4+(pow(4,n-1-k)*1),
                b5+(pow(5,n-1-k)*1),
                b6+(pow(6,n-1-k)*1),
                b7+(pow(7,n-1-k)*1),
                b8+(pow(8,n-1-k)*1),
                b9+(pow(9,n-1-k)*1),
                b10+(pow(10,n-1-k)*1),count
	       );
     }
     else
     {
       soln[k]='0';
       get_coin(n,j,soln,k+1,
                b2+(pow(2,n-1-k)*0),
                b3+(pow(3,n-1-k)*0),
                b4+(pow(4,n-1-k)*0),
                b5+(pow(5,n-1-k)*0),
                b6+(pow(6,n-1-k)*0),
                b7+(pow(7,n-1-k)*0),
                b8+(pow(8,n-1-k)*0),
                b9+(pow(9,n-1-k)*0),
                b10+(pow(10,n-1-k)*0),count
	       );
       soln[k]='1';
       get_coin(n,j,soln,k+1,
                b2+(pow(2,n-1-k)*1),
                b3+(pow(3,n-1-k)*1),
                b4+(pow(4,n-1-k)*1),
                b5+(pow(5,n-1-k)*1),
                b6+(pow(6,n-1-k)*1),
                b7+(pow(7,n-1-k)*1),
                b8+(pow(8,n-1-k)*1),
                b9+(pow(9,n-1-k)*1),
                b10+(pow(10,n-1-k)*1),count
	       );
     }
   }
}
main()
{
  int t;
  int n,j;
  int count=0;
  FILE *fp=fopen("abc","r");
  fscanf(fp,"%d",&t);
  fscanf(fp,"%d",&n);
  fscanf(fp,"%d",&j);
  char soln[n];
  printf("Case #1:\n");
  get_coin(n,j,soln,0 , 0,0,0,0,0,0,0,0,0, &count);
}
