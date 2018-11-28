#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int T,D,sol,temp,psize;
vector<int> P;

int solution(int Top)
{
	if (Top <= 0) return 0;
	psize = P.size();
	int r = sqrt(Top);
	int TopHalf=0 , cnt = 0,minCnt=87654321,minTH=87654321;
	for (int j = r; j >= 2; j--)
	{
		TopHalf = Top / j, cnt = 0;
		if (Top % j != 0) TopHalf += 1;
		for (int i = 0; i < psize; i++)
		{
			if (P[i]>TopHalf)
				cnt += ceil((double)P[i]/TopHalf)-1;
		}
		if (minCnt + minTH > TopHalf + cnt)
			minCnt = cnt, minTH = TopHalf;
	}
	if (Top > minCnt + minTH)
	{
		for (int i = 0; i < psize; i++)
		{
			if (P[i]>minTH)
			{
				r = ceil((double)P[i] / minTH);
				for (int j = r; j >= 2; j--)
				{
					if (P[i] % j != 0)
						P.push_back(P[i]/j+1);
					else
						P.push_back(P[i]/j);
					P[i] -= P[P.size() - 1];
				}
			}
		}
		sort(P.begin(), P.end());
		return  minCnt + solution(P[P.size() - 1]);
	}
	else
	{
		for (int i = 0; i < psize; i++)
			P[i]--;
		return 1 + solution(Top - 1);
	}
}
int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		P.clear();
		cin >> D;
		for (int j = 0; j < D; j++)
		{
			cin >> temp;
			P.push_back(temp);
		}
		sort(P.begin(), P.end());
		cout << "Case #" << i << ": " << solution(P[P.size()-1]) << endl;
	}
}