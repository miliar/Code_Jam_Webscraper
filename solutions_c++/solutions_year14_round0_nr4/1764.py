/*#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

pair<int,int> getScore(vector<double>& a,vector<double>& b)
{

	int len = a.size();
	int ascore = 0, bscore = 0;
	
	for(int i=0;i<len;i++)
	{
		if(a[i] < b[i])
		{
			bscore++;
		}
		else
		{
			ascore++;
		}
	}
	return make_pair(ascore,bscore);
}

int main()
{
	int T,c=1;
	
	scanf("%d",&T);
	
	while(T--)
	{
		int N;
		scanf("%d",&N);

		vector<double> Naomi;
		vector<double> Ken;
		int maxA=0,maxB=0;

		for(int i=0;i<N;i++)
		{
			double a;
			scanf("%lf",&a);
			Naomi.push_back(a);
		}
		for(int i=0;i<N;i++)
		{
			double a;
			scanf("%lf",&a);
			Ken.push_back(a);
		}

		sort(Naomi.begin(),Naomi.end());

		do 
		{
			pair<int,int> temp = getScore(Naomi,Ken);

			if(maxA < temp.first)
			{
				maxA = temp.first;
			}
			if(maxB < temp.second)
			{
				maxB = temp.second;
			}
		} while (next_permutation(Naomi.begin(),Naomi.end()));


		
		printf("Case #%d: %d %d\n",c++,maxA,N-maxB);
	}
	return 0;
}*/

#include <stdio.h>
#include <algorithm>
#include <deque>
#include <xfunctional>

using namespace std;



int cantargetWin(double a, deque<double>& target)
{

	int len = target.size();

	for(int i=0;i<len;i++)
	{
		if(a<target[i])
		{
			return 1;
		}
	}
	return 0;
}

int main()
{
	int T,c=1;

	scanf("%d",&T);

	while(T--)
	{
		int N;
		scanf("%d",&N);

		deque<double> Naomi;
		deque<double> Ken;
		int maxA=0,maxB=0;

		for(int i=0;i<N;i++)
		{
			double a;
			scanf("%lf",&a);
			Naomi.push_back(a);
		}
		for(int i=0;i<N;i++)
		{
			double a;
			scanf("%lf",&a);
			Ken.push_back(a);
		}

		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end(),greater<double>());

		deque<double> tempNaomi = Naomi;

		for(int i=0;i<Ken.size();i++)
		{
			if(cantargetWin(Ken[i],tempNaomi))
			{
				maxA++;
				tempNaomi.pop_back();
			}
			else
			{
				tempNaomi.pop_front();
			}
		}

		sort(Ken.begin(),Ken.end());
		sort(Naomi.begin(),Naomi.end(),greater<double>());
		deque<double> tempKen = Ken;

		for(int i=0;i<Naomi.size();i++)
		{
			if(cantargetWin(Naomi[i],tempKen))
			{
				maxB++;
				tempKen.pop_back();
			}
			else
			{
				tempKen.pop_front();
			}
		}

		printf("Case #%d: %d %d\n",c++,maxA,N-maxB);
	}
	return 0;
}