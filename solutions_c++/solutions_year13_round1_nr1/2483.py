#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
	int n;
	scanf("%d",&n);
	unsigned long long int total;
	unsigned long long int count=1;
	unsigned long long int i,j;
	unsigned long long int r,t;
	unsigned long long int t2;
	while(n--)
	{
        printf("Case #%d: ",count);
		count++;
		scanf("%llu%llu",&r,&t);
		unsigned long long int yes=0;
		while(true)
		{
		    t2=(2*r+1);
		    if(t2<=t)
		    {
		        yes++;
                r+=2;
                t=t-t2;
		    }
		    else
		    {
		        break;
		    }

		}
		printf("%llu\n",yes);
	}
	return 0;
}
