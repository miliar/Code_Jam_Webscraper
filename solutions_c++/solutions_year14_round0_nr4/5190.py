#include <iostream>
#include <algorithm>
int a[10000]={0};
using namespace std;
main()
{
      int b[10000],i,j,k,n,m,q=0;
      scanf("%d%d%d",&i,&j,&k);
      n=i+j+k;
      while(n--)
      {
                scanf("%d",&m);
                if(a[m]==0)
                a[m]=a[m]+1;
                else if(a[m]==1)
                { b[q]=m;
                a[m]=a[m]+1;
                  q++;}}
                  sort(b,b+q);
                  printf("%d\n",q);
                  for(i=0;i<q;i++)
                  printf("%d\n",b[i]);
                  scanf("%d",&i);
                  return 0;
                  }
                  
                  
