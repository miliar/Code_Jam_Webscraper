#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main() {

	int t,n,k,count,i,j,count1;
	float A[1005],B[1005];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		count=0;
		count1=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%f",&A[i]);
		for(i=0;i<n;i++)
		scanf("%f",&B[i]);
		sort(A,A+n);
		sort(B,B+n);
		for(i=n-1,j=n-1;i>=0;i--)
		{if(A[i]>B[j])
			count++;
			else j--;
		}
		for(i=n-1,j=n-1;i>=0;i--)
		{  while(j>=0)
			{if(A[i]>B[j]) {count1++; j--; break;}
              else j--;
			}
        }printf("Case #%d: %d %d\n",k,count1,count);
	}return 0;}
