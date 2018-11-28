#include<stdio.h>
#include<string>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	long long test;
	cin >> test;
	long long counter =1;
	while(test--)
	{
		long long r , t;
		long long a1 , a2;
		cin >> r >> t;
		long long r2,r1;
		r1=r+1;
		long long rings=0;
		r2=r;
		while(1)
		{
			a2=(r1*r1);
			a1=(r2*r2);
			if((a2-a1)>t)
				break;
			else
			{
				t-=(a2-a1);
				rings++;
			}
			r1+=2;
			r2+=2;
		}
		printf("Case #%lld: %lld\n",counter,rings);
		counter++;
	} 
    return 0;
}
