#include<stdio.h>
#define MAX_NUM 1000
int an1, n;

void insertion_sort(double temp, double a[],  int j)
{
  int m=0,m2;
  while(m<j)
  {
    if(a[m]> temp)
      break;
    m++;
  }
  if(m<j)
  {
    m2=j;
    while(m2>=m)
    {
      a[m2 +1]=a[m2];
      m2--;
    }
  }
  a[m]=temp;
}

int search1 ( double a, double b[], int &j)
{
  while(j<n)
  {
    if(a < b[j])
    {
      an1++;
      return 1;
    }
    j++;
  }
  return 0;
}


int main()
{
  int t,i,j,k;
  double a[MAX_NUM],b[MAX_NUM],temp;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    scanf("%d",&n);
    for(j=0;j<n;j++)
    {
      scanf("%lf",&temp);
      insertion_sort(temp,&a[0],j);
    }
    for(j=0;j<n;j++)
    {
      scanf("%lf",&temp);
      insertion_sort(temp,&b[0],j);
    }
    an1=0; k=0; j=0;
    while(k<n)
    {
      if(a[k]>b[j])
      {
        j++;
      }
      k++;
    }
    printf("Case #%d: %d ",i , j);

    k=0;j=0; an1=0;
    while(j < n)
    {
      search1(a[k], &b[0], j);
      {
	j++;
      }
      k++;
    }
    printf("%d\n", (n-an1));

  }
  return 0;
}
