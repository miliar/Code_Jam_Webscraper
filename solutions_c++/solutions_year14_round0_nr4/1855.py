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
#include <cstring>
#include <fstream>

using namespace std;

vector<double> Romeo, Juliet;
int N;

int solve()
{
	int warRomeo = 0, warJuliet = 0;
	int ind1 = 0, ind2 = 0;

	while( ind1 < N && ind2 < N )
	{
		if( Romeo[ind1] < Juliet[ind2] )
		{
			warJuliet++;
			ind1++, ind2++;
		}
		else
		{
			ind2++;
		}
	}

	return warJuliet;

}

int main()
{

	freopen("input.txt","r",stdin);

	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{

		printf("Case #%d: ",t);

		scanf("%d",&N);

		Romeo.clear();
		Juliet.clear();

		for(int i=0;i<N;i++)
		{
			double x;
			scanf("%lf",&x);
			Romeo.push_back(x);
		}
		for(int i=0;i<N;i++)
		{
			double x;
			scanf("%lf",&x);
			Juliet.push_back(x);
		}

		sort(Romeo.begin(), Romeo.end());
		sort(Juliet.begin(), Juliet.end());

		int y = N-solve();
		swap(Romeo,Juliet);
		int x = solve();

		printf("%d %d\n",x,y);

	}

	return 0;

}
