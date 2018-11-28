#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ll;

vector<bool> sieve(1e7,true);

void siever()
{
	sieve[1]=sieve[2]=false;
	int sq = sqrt(1e7);
	for(int i=0;i<=1e7;i++)
	{
		if(sieve[i])
		{
			for(int j=i*i;j<=1e7;j+=2)
			{
				sieve[j]=false;
			}	
		}
	}
}

ll p(ll base, ll power)
{
	ll res=1;
	while(power>0)
	{
		if(power&1)
			res= res*base;
			power>>=1;
		base = base * base;
	}
	return res;

}

ll finder(int set_size, ll st,int  counter)
{
	for(int j = 0; j < set_size; j++)
       	{	
       	   if(counter & (1<<j))
				st |= 1 << j;
       	}
		st ^= (1 << set_size); 
		//	cout<<st<<endl; //print it
		return st;
}

void convert(int set_size, int a[], ll st)
{
	for(int i=2;i<=10;i++)
		{
			ll num = 0;
			bool m=0;
			ll temp= st;
			//printf("%llu\n", st);
			for(int j=0;j<=set_size;j++)
			{
				m = temp & 1;
				if(m)
					num +=  p(i,j) ;
				temp>>=1;
		//		printf("%llu ",num);
		//			getchar();
			} //conversion of number
			//cout<<endl;
			if(!sieve[num])
			{
				for(int x=2;x*x<=num;x++)
				{
					if(sieve[x])
					{
						if(num%x==0)
						{
							a[i]=x;
							break;
						}
					}
				}	
			}
		} //convert and check if the number is prime and find one of it's divisor
}

void code(int set_size, int end)
{
    unsigned int pow_set_size = 1<<set_size;
    int counter, j;
    for(counter = 0; counter < pow_set_size; counter++)
    {
		ll st = 0;
	
		if(end==0) //if j numbers have been found then just break it
		{
			break;
		}
	
		st= finder(set_size, st, counter);
		//creating one of the possible numbers
     	

		int a[11]={0};

		convert( set_size, a, st )	;	

			int flag=0;
		for(int i=2;i<=10;i++)
				if(a[i]==0)
					flag=1;
		if(!flag)
		{
			end--;
			cout<<st<<" ";
			for(int i=2;i<=10;i++)
			{
				printf("%d ", a[i]);
			}
			cout<<endl;	
		}
    }
}

int main()
{
	siever();
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;x++)
	{
		int n,ji;
		scanf("%d %d", &n, &ji);
		printf("Case #%d: \n", x);
		code(n-1,ji);
		//cout<<p(2,8)<<endl;
	}
	return 0;
}