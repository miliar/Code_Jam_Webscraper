# include <cstring>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <map>
# include <iostream>
# include <cmath>
using namespace std;
int main()
{
	int r,c,w,sum,T,x,count=0;
	scanf("%d",&T);
	while(T--)
	{
		count++;
		scanf("%d %d %d",&r,&c,&w);
				printf("Case #%d: ",count);		
		if(c==w)
			{
				printf("%d\n",w);
				continue;
			}
		sum=1;
		x=w;
		while(x+w<c)
		{
			x=x+w;
			sum++;
		}
		sum+=w;	
		sum=sum*r;
		printf("%d\n",sum);
	}
	return 0;
}
