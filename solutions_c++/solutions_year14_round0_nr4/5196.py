/*
	Accepted.
		http://acmp.ru/index.asp?main=task&id_task=114

		Очень простое решение.
*/

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <stack>

using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	cin >>tc;

	for (int cc = 0;cc < tc;cc++)
	{
		int n;
		cin >>n;
		vector<double> N(n);
		vector<double> K(n);
		for (int i = 0;i < n;i++)
			cin >>N[i];
		for (int i = 0;i < n;i++)
			cin >>K[i];


		sort(N.begin(), N.end());
		sort(K.begin(), K.end());

		//for (int i = 0;i < n;i++)
		//	cout <<N[i] <<" " ;
		//cout <<endl;

		//for (int i = 0;i < n;i++)
		//	cout <<K[i] <<" " ;
		//cout <<endl;


		int war = 0, deceitful = 0;

		for (int i = 0, j = 0;i < n;i++)
		{
			bool beaten = false;
			for (;j < n;j++)
				if (K[j] > N[i])
				{
					beaten = true;
					break;
				}
			if (!beaten)
			{
				war = n - i;
				break;
			}
			j++;
		}

		for (int i = 0;i < n;i++)	// removing i largest by i smallest
		{
			int win = 0;

			for (int k = i;k < n;k++)
				win += N[k] > K[k - i];

			deceitful = max(deceitful, win);
		}
		

		cout <<"Case #" <<cc+1 <<": " <<deceitful <<" "<< war <<endl;
	}

	return 0;
}
