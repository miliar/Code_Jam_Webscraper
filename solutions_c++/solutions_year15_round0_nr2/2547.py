#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int curmin;

int getMinTime(int depth,vector<int> P)
{
	if(depth > curmin)
	{
		return 0x7fffffff;
	}
	bool finished = true;
	for(int i=0;i<P.size();i++)
	{
		if(P[i] != 0)
		{
			finished = false;
			break;
		}
	}
	if(finished)
	{
		return depth;
	}
	int ret;
	int minMoveV = 0x7fffffff;
	sort(P.begin(),P.end());

	int maxV = P[P.size()-1];

	for(int i=1;i<=5;i++)
	{
		vector<int> modifedP = P;
		modifedP[modifedP.size()-1] -= i;
		modifedP.push_back(i);

		int v = getMinTime(depth+1,modifedP);

		if(v < minMoveV)
		{
			minMoveV = v;
			curmin = v;
		}
	}
	//just eat

	for(int i=0;i<P.size();i++)
	{
		if(P[i] != 0)
		{
			P[i]--;
		}
	}
	int valueB = getMinTime(depth+1,P);

	ret = valueB > minMoveV ? minMoveV : valueB;
	
	if( curmin > ret)
	{
		curmin = ret;
	}
	return ret;
}


int main()
{
	int T,c = 1;
	scanf("%d",&T);
	while(T--)
	{
		int D;
		//int P[1001];
		vector<int> P;
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			int tmp;
			scanf("%d",&tmp);
			P.push_back(tmp);
		}
		sort(P.begin(),P.end());
		curmin = P[P.size()-1];
		int v = getMinTime(0,P);
		printf("Case #%d: %d\n",c++,v);
	}
	return 0;
}