#include<cstdio>
#include<algorithm>
using namespace std;

int p;
int ctIntersection(int arr1[], int arr2[])
{
  int i = 0, j = 0,ctr=0;
  while(i < 4 && j < 4)
  {
    if(arr1[i] < arr2[j])
      i++;
    else if(arr2[j] < arr1[i])
      j++;
    else /* if arr1[i] == arr2[j] */
    {
      ctr++;
	  p = arr2[j++];
      i++;
    }
  }
  return ctr;
}

int main()
{
 int t;
 scanf("%d",&t);
 for(int k=1;k<=t;k++)
 {
   int n,a[4][4],b[4],c[4];
   scanf("%d",&n);
   for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
	  scanf("%d",&a[i][j]);
	for(int i=0;i<4;i++)
	  b[i]=a[n-1][i];
	scanf("%d",&n);
	for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
	  scanf("%d",&a[i][j]);
	for(int i=0;i<4;i++)
	   c[i]=a[n-1][i];
	   sort(b,b+4);
	   sort(c,c+4);
	 n= ctIntersection(b,c);
	switch(n)
	{
	  case 0: printf("Case #%d: Volunteer cheated!\n",k);break;
	  case 1: printf("Case #%d: %d\n",k,p);break;
	  default: printf("Case #%d: Bad magician!\n",k);break;
	  }
	  }
	  return 0;
	  }
