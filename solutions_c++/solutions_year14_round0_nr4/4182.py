#include <cstdio>
#include <algorithm>

double naomi[1004];
double ken[1004];

using namespace std;

int main()
{
	freopen("in41.txt","r",stdin);
	freopen("out41.txt","w",stdout);
	
	int testCase;
	int N,warNaomi = 0,warKen = 0;
	int temp = 0;
	
	scanf("%d",&testCase);
	
	
	
	for(int test = 1; test <= testCase; test++)
	{
		warNaomi = 0;warKen = 0;temp = 0;
		scanf("%d",&N);
		for(int i = 0; i < N; i++)
		{
			scanf("%lf",&naomi[i]);			
		}
		
		for(int i = 0; i < N; i++)
		{
			scanf("%lf",&ken[i]);			
		}
		
		sort(naomi,naomi+N);
		sort(ken,ken+N);
		
		
		for(int i = 0; i < N; i++)
		{
			for(int j = temp; j < N; j++)
			{
				temp++;
				if(ken[i]<naomi[j])
				{
					warNaomi++;
					break;					
				}
				
			}
		}
		temp = 0;
		for(int i = 0; i < N; i++)
		{
			for(int j = temp; j < N; j++)
			{
				temp++;
				if(naomi[i]<ken[j])
				{
					warKen++;					
					break;					
				}
				
			}
		}
		
		printf("Case #%d: %d %d\n",test,warNaomi,(N-warKen));
	}
	
	return 0;
}
