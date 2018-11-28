#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int max_n=100010;

int n,T,x;
int a[max_n];
bool done[max_n];

int main()
{
	scanf("%d",&T);

	multiset<int> S;
	for(int z=0; z<T; z++)
	{
		scanf("%d%d",&n,&x);
		for(int i=0; i<n; i++)
		{
			scanf("%d",&a[i]);
			S.insert(-a[i]);
		}

		sort(a,a+n);

		int res=0;
		while(!S.empty())
		{
			int y=-(*(S.begin()));
			S.erase(S.begin());
			if(!S.empty())
			{
				multiset<int>::iterator it=S.lower_bound(y-x);
				if(it!=S.end())
					S.erase(it);
			}
			res++;
		}


		printf("Case #%d: %d\n",z+1,res);
	}

	return 0;
}