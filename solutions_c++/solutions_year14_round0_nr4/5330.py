#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

void mergesort(float a[],int low,int mid,int high)
{int i,m,k,l;
float* temp=new float[1000];
l=low;
i=low;
m=mid+1;
while((l<=mid)&&(m<=high))
{if(a[l]<=a[m])
{temp[i]=a[l];
l++;
}
else
{temp[i]=a[m];
m++;
}
i++;
}
if(l>mid)
{for(k=m;k<=high;k++)
{temp[i]=a[k];
i++;
}
}
else
{for(k=l;k<=mid;k++)
{temp[i]=a[k];
i++;
}
}
for(k=low;k<=high;k++)
a[k]=temp[k];
}
void partition(float a[],int l,int h)
{int mid,i;
if(l<h)
{mid=(l+h)/2;
partition(a,l,mid);
partition(a,mid+1,h);
mergesort(a,l,mid,h);
}	
}


int main()
{int t,m,n,i,j,r,k,z;
 float* A=new float[1000];
  float* B=new float[1000];
scanf("%d",&t);
for(k=1;k<=t;k++)
{m=0,n=0;
scanf("%d",&r);
for(j=0;j<r;j++)
scanf("%f",&A[j]);
partition(A,0,r-1);
for(j=0;j<r;j++)
scanf("%f",&B[j]);
partition(B,0,r-1);
i=0;j=0;
while(i<r)
{if(B[j]<A[i])
{m++;
i++;
j++;
}
else 
i++;
}
i=0;
j=0;
while(i<r)
{if(B[i]>A[j])
{i++;
j++;
n++;
}
else
i++;
}
z=r-n;
printf("Case #%d: %d %d\n",k,m,z);

}
return 0;
}
