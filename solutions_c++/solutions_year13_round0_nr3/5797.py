#include<stdio.h>
#include<string.h>
#include<math.h>

long reverseNumber(long num_)
{
	long inv; inv = 0;

	while (num_>0)
	{
		inv = inv * 10 + (num_%10);
		num_ = num_ / 10;
	}

	return inv;
}

int main()
{
	freopen("in_c.txt","r",stdin);

	freopen("C:\\Users\\Rana\\Desktop\\codejam first round\\out_c_small.txt","w",stdout);

	long cc,cas;
	long A,B;
	const long max=1000;
	long i;

	int isSqPal[max+1];

	scanf("%ld",&cas);

	for(cc=1;cc<=cas;cc++)
	{
		scanf("%ld %ld",&A,&B);

		//set all to zero
		//for(i=1;i<=B;i++)
		//{
			//isSqPal[i]=0;
		//}

		//precalculation
		long count=0;
		for(i=A;i<=B;i++)
		{
			//if((i*i)>max)
			//{
				//break;
			//}
			//if(i*i<=max)
			//{
			long temp=sqrtl(i);

			if(temp*temp==i)
			{
				if((i)==reverseNumber(i) && (temp)==reverseNumber(temp))
				{
					count++;
				}
			}
			//}
			//printf("%ld %ld %ld\n",i,i*i,count);
			//isSqPal[i*i]=count;

		}

		printf("Case #%ld: %d\n",cc,count);
	}

	return 0;
}
