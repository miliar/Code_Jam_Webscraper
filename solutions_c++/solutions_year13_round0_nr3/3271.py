#include<cstdio>
#include<algorithm>

using namespace std;

int m;

int main()
{
	int r, i , j;
	int t;
	int a,b;
	int sum = 0;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("2.txt","w",stdout);	
	scanf("%d",&t);
	for(r = 0 ; r < t ; r++)
	{
		scanf("%d %d",&a,&b);
		sum = 0;
		for(i =a ; i<= b ; i++)
		{
			if(i == 1 || i == 4 || i == 9 || i == 121 || i == 484)
				sum++;
		}
		
		printf("Case #%d: %d\n",r+1,sum);
		
	}
	return 0;
}
