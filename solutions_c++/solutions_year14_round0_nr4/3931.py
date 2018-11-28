#include <iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#define sf scanf
#define pf printf
using namespace std;
int main() {
   int test,counter,opt,dec,n,i,j;
	float arr1[10005],arr2[10005];
	sf("%d",&test);
	for(counter=1;counter<=test;counter++)
	{
		opt=0;
		dec=0;
		sf("%d",&n);
		for(i=0;i<n;i++)
		sf("%f",&arr1[i]);
		for(i=0;i<n;i++)
		sf("%f",&arr2[i]);
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		for(i=n-1,j=n-1;i>=0;i--)
		{if(arr1[i]>arr2[j])
			opt++;
			else j--;
		}for(i=n-1,j=n-1;i>=0;i--)
		{ while(j>=0)
			{if(arr1[i]>arr2[j]) {dec++; j--; break;}
            else j--;
			}
        }pf("Case #%d: %d %d\n",counter,dec,opt);
	}
	return 0;
	}
