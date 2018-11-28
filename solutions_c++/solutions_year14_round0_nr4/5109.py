#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int n,t,it=1;
	int ans1,ans2;
	bool Naomi[10];
	bool ken[10];
	float Nweight[10];
	float Kweight[10];
	scanf("%d",&t);
	while(t--)
	{
		ans1=0;
		ans2=0;
		scanf("%d",&n);
		for(int j= 0;j<n;j++)
		{
			Naomi[j]=false;
			ken[j]=false;
		}
		for(int j= 0;j<n;j++)
		{
			scanf("%f",&Nweight[j]);
		}
		for(int j= 0;j<n;j++)
		{
			scanf("%f",&Kweight[j]);
		}
		sort(Nweight,Nweight+n);
		sort(Kweight,Kweight+n);
		//ken is choosen and naomi is checked
		for(int i=0;i<n;i++)
		{
			int j=0;
			while(j<n)
			{
				if(Naomi[j]==false)
				{
					if(Nweight[j]>Kweight[i])
					{
						Naomi[j]=true;
						ans1++;
						break;
					}
				}
				j++;
			}
		}
		//naomi is choosen and ken is checked
		for(int i=0;i<n;i++)
		{
			int j=0;
			while(j<n)
			{
				if(ken[j]==false)
				{
					if(Kweight[j]>Nweight[i])
					{
						ken[j]=true;
						ans2++;
						break;
					}
				}
				j++;
			}
		}
		printf("Case #%d: %d %d\n",it,ans1,ans2);
		it++;
	}
	return 0;
}
