#include <stdio.h>


int main()
{
	int t=0;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		unsigned long long n,tmp,last = 0;
		int mul = 1;
		char digits[10]={0};
		bool flag = false;
		int zero = false;
		scanf("%llu",&n);	
		int total = (9 * (9+1))/2;
		
		
		int curr=0;		
		if ( n ==0 )
			{
				printf("Case #%d: INSOMNIA\n",i);
				//flag = true;
				continue;
			}
			//else
		tmp = n;
		while(!flag)
		{
			

				n *= mul;
				//printf("%llu\n",n);
				while(n>0)
				{
					int digit=(int)n%10;
					//printf("%d\n",(int)n%10);
					n=n/10;
					
					if (zero == false && digit==0)
						zero = true;
					else
					{
						if ( digits[digit]==0)
						{
							//printf("++++Added : %d\n",digit);
							digits[digit]=1;
							curr += digit;
						}
					}
					
					if( curr == total && zero==true)
					{
						flag = true;
						last = tmp * mul;
						//printf("LAST = %llu\n",last);
						break;
					}
					
				}
				mul++;
				n = tmp;
			
		}//while
		
		printf("Case #%d: %llu\n",i,last);
		
	
	}
	return 0;
}
