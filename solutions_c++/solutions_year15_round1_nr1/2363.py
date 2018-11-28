#include <stdio.h>
#include <algorithm>
#define N 1000 
using namespace std;

int m[N+5]; 
int main()
{
	int t;
	scanf("%d",&t);
	int teste = 0;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		for (int i = 1; i <= n; i++)
			scanf("%d",&m[i]);
		int y = 0;
		for (int i = 1; i < n; i++)
			if (m[i+1] < m[i])
				y += m[i] - m[i+1];
		int maior = 0;
		for (int i = 1; i < n; i++)
			if (m[i+1] < m[i])
				maior = max(maior, m[i] - m[i + 1]);
		int z = 0;
		for (int i = 1; i < n; i++)
			z += min(m[i], maior);	
		
		teste++;
		printf("Case #%d: %d %d\n",teste,y,z);
	}
	return 0;
}