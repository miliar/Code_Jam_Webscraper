#include <cstdio>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdlib>

using namespace std;

int count_set(int bitvector[])
{
	int count=0;
	for(int i=0;i<10;i++)
		if(bitvector[i]!=0)
			count++;
	return  count;
}

int main()
{
	int t;
	scanf("%d",&t);
	int count=1;
	while(t--)
	{
		long long int n;
		scanf("%lld",&n);
		int bitvector[10]={0};
		int flag=0;
		long long int N=0;
		if(n!=0)
		{
			for(int i=1;flag!=1;i++)
			{
				N=n*i;
				stringstream convert;
				convert << N;
				string N_str=convert.str();
				for(int j=0;j<N_str.size();j++)
				{
					int index=(int)(N_str[j]-'0');
					bitvector[index]++;
				}	
				if(count_set(bitvector)==10)
					flag=1;
			
			}
			printf("Case #%d: %lld\n",count++,N);
		}
		else
			printf("Case #%d: INSOMNIA\n",count++);	
	}
}