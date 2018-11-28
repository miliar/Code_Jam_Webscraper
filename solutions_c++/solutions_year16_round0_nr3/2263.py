#include<stdio.h>
#include<math.h>

#include<vector>
using namespace std;

int main()
{

	freopen ("C-small-attempt0.in","r",stdin);
	freopen("C_small_output.out", "w", stdout);
	
	int T, N, J;
	scanf("%d", &T);
	int count=0;
	
	for(int temp=0;temp<T; temp++)
	{
		printf("Case #%d:\n", temp+1);
		scanf("%d %d", &N, &J);
		
		for(int num=(1<<(N-1))+1; num < (1<<N) && count<J ;num+=2)
		{
			long long int numbase[11]= {0};
			bool check[11]={0};
			long long int factors[11]={0};
			bool flag=1;
			
			for(int base=2; base<=10; base++)
			{
				for(int j=0;j<N;j++)
				{
					if(num & (1<<j))
					{
						long long int power=1;
						for(int jj=1;jj<=j;jj++) power*=base;
						numbase[base]+=power;
					}
				}
				
				//Primality testing
				for(long long int i=2;i*i<= numbase[base];i++)
				{
					if((numbase[base]%i)==0)
					{
						factors[base]=i;
						check[base]=1;
						break;
					}
				}
				if(!check[base])
				{
					flag=0;
					break;
				}
			}
			
			if(flag)
			{
				count++;
				//printf("%d ",num);
				vector<int> num2;
				for(int ii=num;ii>0;ii/=2)
				{
					num2.push_back(ii%2);
				}
				for(int ii=num2.size()-1; ii>=0; ii--)
					printf("%d",num2[ii]);
				for(int base=2; base<=10; base++)
				{
					printf(" %lld", factors[base]);
					//printf(" %d: %lld; ",base, numbase[base]);
				}
				printf("\n");
			}
		}	
	}
	
	return 0;

}