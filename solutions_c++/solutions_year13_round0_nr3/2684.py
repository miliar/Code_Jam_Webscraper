#include <stdio.h>
#include <math.h>

int n,count=1;
int start,end;

bool isFair(int x)
{
  if(x<10) return true;
  int base = 1;
  int sq = x;
  int t = sq;
  while(t>=10)
    {
      base*=10;
      t/=10;
    }

  while(sq>=10)
    {
      int high = sq/base;
      int low = sq%10;
      if(high!=low) return false;
      sq -= (sq/base)*base;
      sq /= 10;
      base/=100;
    }
  return true;
}
int main()
{
  scanf("%d",&n);
  while(count<=n)
    {
      scanf("%d%d",&start,&end);
      int front = sqrt(start);
      int rear = sqrt(end);
      int ans = 0;
      for(int i=front;i<=rear;i++)
	{
	  int t=i*i;
	  if(t>=start&&t<=end&& isFair(i)&&isFair(t) )
	      {
		//	printf("%d & %d\n",i,i*i);
		ans++;
	      }
	}
      //printf("from:%d %d\n",start,end);
      printf("Case #%d: %d\n",count++,ans);
    }
  return 0;
}
