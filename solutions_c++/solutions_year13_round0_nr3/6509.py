#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

long long reverse(long long b)
{
	int i,k,a;
	long long sum,x[1000];

	for(i=1;b>0;i++)
	{
		x[i]=b%10;
		b=b/10;
	}
	sum=0;
	for(k=i-1;k>=1;k--)
	{
		a=pow(10.f,(i-k-1));
		sum=sum+(x[k]*a);
	}
	return sum;
}

int main(int argc, const char *argv[])
{
	string inputFileName = "C-small-attempt0.in";
	string outputFileName = "output.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

	long long test,i,k,a,b,rev,s,count,d,rev_s;

	scanf("%lld",&test);

	for(k=1;k<=test;k++)
	{
		scanf("%lld%lld",&a,&b);

		count=0;

		for(i=a;i<=b;i++)
		{
			rev=reverse(i);

			if(rev==i)
			{
				s=(ceil(sqrt((double)i))*(ceil(sqrt((double)i))));

				if(s==i)
				{
					d=sqrt((double)i);
					rev_s=reverse(d);

					if(rev_s==d)
					{
						count=count+1;
					}
					else
					{
						count=count+0;
					}

				}
				else
				{
					count=count+0;

				}

			}
			else
			{
				count=count+0;
			}
		}
		printf("Case #%lld: %lld\n",k,count);

	}
	return 0;
}

