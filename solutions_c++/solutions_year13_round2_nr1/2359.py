#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	int t;
	freopen("aa.txt", "r", stdin);
	freopen("aaout.txt", "w", stdout);
	scanf("%d\n",&t);
//	printf("%d\n",t);
	int y = t;
	while( t--)
	{
           int a,n;
           int c,d,swap , length , op=0,xx=0;
           int array[10];
           scanf("%d %d\n", &a,&n);
          // printf("%d %d\n",a,n);
           length =a;
           for( int i= 0; i<n; i++)
           {
           scanf("%d ",&array[i]);
//           printf("%d ",array[i]);
           }
           scanf("\n");
         //  printf("\n");
           for (c = 0 ; c < ( n - 1 ); c++)
           {
            for (d = 0 ; d < n - c - 1; d++)
                {
                  if (array[d] > array[d+1]) /* For decreasing order use < */
                   {
                      swap       = array[d];
                      array[d]   = array[d+1];
                      array[d+1] = swap;
                      }
                 }
              }
             // for( int i= 0; i<n; i++)
      //    {
           //scanf("%d ",&array[i]);
        //   printf("%d ",array[i]);
     //      } 
        //   printf("\n");
        for( int i=0; i<n; i++)
        {     // printf(" value of length is : %d \n",length);
               if( length > array[i] )
               {  xx = 0;
               length += array[i];
               }
               else  
               {      //printf(" incresing OP  and new length is : %d ",length*2-1);
                      length = length + length -1 ;  op++; i--; xx++;
                     // printf(" comparing %d with %d \n",xx, n-i-1);
                      if( xx > (n-i-1) )
                      {     op--;
                             break; }
               }
        }
        op = op>n?n:op;
       printf("Case #%d: %d\n", y-t , op);
       }
}              
               
