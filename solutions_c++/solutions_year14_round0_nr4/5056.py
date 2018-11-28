//siddharth prasad

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
 int t,T;
 cin>>t;
 for(t=1;T<=t;T++)
 {
  double n,k,i,j,x=1,d=0,c=0;
  cin>>n;
  double a1[n],a2[n];
  for(i=0;i<n;i++)
  {
  cin>>a[i];
  }
  for(i=0;i<n;i++)
  {
  cin>>b[i];
  }
  sort(a,a+n);
  sort(b,b+n);
  i = j = 0;
  while(j < n) {
			if(a2[j] > a1[i]) {
				c++;
				i++;
				j++;
			}
			else {
				j++;
			}
		}
		i = j = 0;
		while(j < n) {
			if(a1[j] > a2[i]) {
				d++;
				i++;
				j++;
			}
			else {
				j++;
			}
		}
		printf("Case #%d: %lf %lf\n",x,d,n-c);
 }
 return 0;
}
