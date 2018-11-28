#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;
#define LATTE
void main()
{
#ifdef LATTE
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
#endif // LATTE
	int t;
	cin >> t;
	int ian = 0;
	while (t--)
	{
		int N;
		vector<double> woodNaomi, woodKen;
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			double temp;
			cin >> temp;
			woodNaomi.push_back(temp);
		}
		for (int i = 0; i < N; i++)
		{
			double temp1;
			cin >> temp1;
			woodKen.push_back(temp1);
		}
		sort(woodNaomi.begin(), woodNaomi.end());
		sort(woodKen.begin(), woodKen.end());
		vector<double> N1(woodNaomi);
		vector<double> N2(woodNaomi);
		vector<double> K1(woodKen);
		vector<double> K2(woodKen);
		int cntN1=0;
		for (int i = 0;i<N; i++)
		{
			for (int j = 0; j < K1.size(); j++)
			{
				if (N1[0] < K1[j])
				{
					vector<double>::iterator itN = N1.begin();
					N1.erase(itN);
					vector<double>::iterator itK = K1.begin() + j;
					K1.erase(itK);

					break;
				}
				else
					
					continue;
				
			}
		}
		cntN1 = N1.size();
	

		int cntN2 = 0;
		for (int i = 0; i < N; i++)
		{
			if (N2[0] < K2[0])
			{
				vector<double>::iterator itN = N2.begin();
				N2.erase(itN);
				K2.pop_back();
			}
			else
			{
				cntN2++;
				vector<double>::iterator itN = N2.begin();
				vector<double>::iterator itK = K2.begin();
				N2.erase(itN);
				K2.erase(itK);
			}
		}
		ian++;
		cout << "Case #" << ian << ": " << cntN2 << " " << cntN1 << endl;
	}




}