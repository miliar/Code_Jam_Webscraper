#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int tick[2507];

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
	int Test,k=0;
	cin>>Test;
	while(Test--)
	{
		int N,i,j,x;
		vector<int> V;
		cin>>N;
		for(i=0;i<=2501;i++)
		   tick[i]=0;
		for(i=0;i<N;i++)
		{
			for(j=0;j < (2*N-1) ;j++)
			{
				cin>>x;
				tick[x]++;
			}
		}
		printf("Case #%d: ",++k);
		for(i=0;i<=2500;i++)
			if(tick[i]%2==1)
				V.push_back(i);
		for(i=0;i<V.size();i++)
			printf("%d ",V[i]);
		printf("\n");
	}
	fclose(stdout);
	return 0;
}
