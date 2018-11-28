#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		int N;
		cin >> N;
		vector<double> naomi(N);
		vector<double> ken(N);
		
		for(int j=0; j<N; j++) 
		cin >> naomi[j];
		for(int j = 0; j<N; j++)
		cin >> ken[j];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int countdc = 0;
		
		int np = 0, kp = 0;
		while(1)
		{
			if(naomi[np] > ken [kp] )
			{
				countdc ++;
				np ++;
				kp ++;
			}
			else
			{
				np ++;
			}
			if(np == N || kp == N) break;
		}
		np = 0; kp = 0;
		int lc = 0;
		while(1)
		{
			if(naomi[np] < ken[kp])
			{
				lc ++;
				np ++;
				kp ++;
			}
			else
			{
				kp ++;
			}
			if(np == N || kp == N) break;
		}
		
		int DWscore, Wscore;
		DWscore = countdc;
		Wscore = N -lc;
		cout << "Case #"<<i<<": "<<DWscore<<" "<<Wscore<<endl; 
	}
}
