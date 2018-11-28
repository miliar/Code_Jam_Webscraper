#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int testcases,row,tmp;
	scanf("%d",&testcases);
	for(int T=1;T<=testcases;++T)
	{
		vector<int> first;
		vector<int> second;
		vector<int> final;
		scanf("%d",&row);
		for(int i=0 ;i <4;++i)
			for(int j=0 ;j <4;++j)
			{
				scanf("%d",&tmp);
				if(i==row-1)
				{
					first.push_back(tmp);
				}
			}
		scanf("%d",&row);

		for(int i=0 ;i <4;++i)
			for(int j=0 ;j <4;++j)
			{
				scanf("%d",&tmp);
				if(i==row-1)
				{
					second.push_back(tmp);
				}
			}
			
		sort(second.begin(),second.end());
		sort(first.begin(),first.end());
		set_intersection(first.begin(),first.end(),second.begin(),second.end(),back_inserter(final));
		if(final.size()==1)
		{
			printf("Case #%d: %d\n",T,final[0]);
		}
		else if(final.size()==0)
		{
			printf("Case #%d: %s",T,"Volunteer cheated!\n");
		}
		else
		{
			printf("Case #%d: %s",T,"Bad magician!\n");
		}
			
	}
	return 0;
}
