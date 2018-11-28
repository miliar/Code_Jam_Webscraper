//Bismillaahir Rahmaanir Raheem.

#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	long double Na[1000], sortedNa[1000], Ke[1000], sortedKe[1000], L_Na = 0.0, L_Ke = 0.0, sortedNa2[1000], sortedKe2[1000];
	int i, j, k_Na = 0, k_Ke = 0, N, T, DWscore, t, Wscore;
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\D-large.in", "r", stdin);
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\LargeOutputProbD.txt", "w", stdout);
	cin>>T;
	for(t = 1;t <= T;t++)
	{
		scanf("%d", &N);
	DWscore = 0;
	Wscore = N;
	for(i = 0; i < N; i++)
		scanf("%Lf", &Na[i]);
	for(i = 0; i < N; i++)
		scanf("%Lf", &Ke[i]);
	for(j = 0; j < N; j++)	//Sorts in descending order.
	{
		for(i = 0; i < N; i++)
		{
			if(L_Na < Na[i])
			{
				L_Na = Na[i];
				k_Na = i;
			}
			if(L_Ke < Ke[i])
			{
				L_Ke = Ke[i];
				k_Ke = i;
			}
		}
		sortedNa[j] = L_Na;
		sortedKe[j] = L_Ke;
		Na[k_Na] = 0;
		Ke[k_Ke] = 0;
		L_Na = 0;
		L_Ke = 0;
	}
	for(i = 0; i < N; i++)
	{
		sortedKe2[i] = sortedKe[i];
		sortedNa2[i] = sortedNa[i];
	}
	for(i = N-1; i >= 0; i--)
	{
		for(j = N-1; j >= 0; j--)
		{
			if(sortedKe[j] < sortedNa[i])
			{
				DWscore++;
				sortedKe[j] = 1.5;
				break;
			}
		}
	}
	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			if(sortedNa2[j] < sortedKe2[i])
			{
				Wscore--;
				sortedNa2[j] = 2;
				break;
			}
		}
	}
	cout<<"Case #"<<t<<": "<<DWscore<<" "<<Wscore<<endl;
	}
	return 0;
}