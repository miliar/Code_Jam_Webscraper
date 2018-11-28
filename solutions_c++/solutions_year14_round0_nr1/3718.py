#include<stdio.h>



 int check(int a[], int b, int *ptr)
 {
   for(int k=0; k<4;k++)
   {
      if(a[k]==b)
      {
	 *ptr=a[k];
	 ptr=ptr;
	 return(1);
      }
   }
   return 0;
 }



int main()
{
  int t,i,a1, a2, b, j, a[4], at[4],fa, ptr;

  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {

    fa=0;
    scanf("%d",&a1);
    for(j=1;j<=4;j++)
    {
      if(j==a1)
	scanf("%d %d %d %d",&a[0], &a[1], &a[2], &a[3]);
      else
	scanf("%d %d %d %d",&at[0], &at[1], &at[2], &at[3]);

    }
    scanf("%d",&a2);
    for(j=1;j<=16;j++)
    {
      if( (j <= a2 * 4) && (j > ((a2-1)*4)))
      {
	scanf("%d",&b);
	fa+=check(&a[0],b,&ptr);

      }
      else
	scanf("%d",&at[0]);
    }
    switch(fa)
    {
      case 1 :
	printf("Case #%d: %d\n", i, ptr);
	break;
      case 0 :
	printf("Case #%d: Volunteer cheated!\n", i);
	break;
      default :
	printf("Case #%d: Bad magician!\n", i);
	break;
    }
  }
  return 0;
}
