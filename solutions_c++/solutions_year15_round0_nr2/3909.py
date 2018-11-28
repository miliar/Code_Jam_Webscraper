#include <cstdio>
#include <cstdlib>
#include <queue>          // std::priority_queue
#include <vector>         // std::vector
#include <functional>
#include <cmath> 
#include <set>
using namespace std;
#define MAX 1010
int erAr[MAX];

void erast(void)
{
	for (int i = 0; i < MAX; ++i )
		erAr[i] = 1;

	erAr[0] = 0; 
	erAr[1] = 0;
	for (int i = 2; i < MAX; ++i)
	{
		if (erAr[i] == 1)
		{
			for (int j = 2*i; j < MAX; j += i)
			{
				erAr[j] = 0;
			}
		}
	}
}
set<int> getBiggestFactor(int x)
{
	set<int> factors;
	for (int i = 2; i < x; ++i)
	{
		if (erAr[i] && x%i==0)
			factors.insert(i);
	}
	return factors;
}

int recursiveSolver(int i, priority_queue<int> in, int minTime, int tmp, int divisor)
{
	in.push(tmp/divisor);
	in.push(tmp-tmp/divisor);
	if (i + in.top() < minTime)
	{
		//printf("%d\n", i);
		minTime = i + in.top();
	}
	for ( i += 1; i < minTime && in.size() != 0; ++i)
	{
		tmp = in.top();

		//printf("%d\n", tmp);
		in.pop();
		
		if ( tmp == 1)
			break;
		set<int> possible = getBiggestFactor(tmp);
		possible.insert(2);
		possible.insert(3);
		
		int tmp2;
		for (int j: possible)
		{
			
			if ( (tmp2 = recursiveSolver(i, in, minTime, tmp,j)) < minTime)
			{
				minTime = tmp2;
			}
			
		}
		break;

	}

	return minTime;
}
int solve(void)
{
	int count;
	scanf("%d ", &count);
	//printf("%d\n", count);
	int total = 0;
	int neededToAdd = 0;
	int tmp;
	priority_queue<int> in;
	for (int i = 0; i < count;++i)
	{
		scanf("%d",&tmp );
		in.push(tmp);
	}
	int minTime = in.top();
	for (int i = 1; i < minTime && in.size() != 0; ++i)
	{
		
		tmp = in.top();
		//printf("%d\n", tmp);
		in.pop();
		
		if ( tmp == 1)
			break;
		
		set<int> possible = getBiggestFactor(tmp);
		possible.insert(2);
		possible.insert(3);
		
		int tmp2;
		for (int j: possible)
		{
			if ( (tmp2 = recursiveSolver(i, in, minTime, tmp,j)) < minTime)
			{
				minTime = tmp2;
			}
		}
		break;
		//printf("%d\n", minTime);
	}
	return minTime;
}

int main(void)
{
	int count;
	erast();
	scanf("%d ", &count);

	for (int i = 0; i < count;++i)
	{
		printf("Case #%d: %d\n",i+1,solve());
	}
}