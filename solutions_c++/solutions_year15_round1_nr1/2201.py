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
	int T,i,n,m[1005],one,count=0;
	float rate,r,two;
	scanf("%d",&T);
	while(T--)
	{
		count++;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&m[i]);
		printf("Case #%d: ",count);	
		one=0;	
		for(i=1;i<n;i++)
		{
			if(m[i-1]>m[i])
				one+=m[i-1]-m[i];
		}	
		rate=-1;
		for(i=1;i<n;i++)
		{
			r=0;
			if(m[i-1]>m[i])
				r=(m[i-1]-m[i])/10.0;
			if(r>rate)
				rate=r;	
		}	
		two=0;
		for(i=1;i<n;i++)
		{
			if(rate*10>=m[i-1])
				two+=m[i-1];
			else
				two+=rate*10.0;	
		}
		printf("%d %.0f\n",one,two);
		
		
	}
	return 0;
}
