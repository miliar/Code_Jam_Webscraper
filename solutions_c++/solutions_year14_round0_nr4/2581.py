#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <stdint.h>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <stdio.h>

using namespace std;


int main()
{
	int T;
	cin >> T;
	
	for (int t=1; t<=T; t++)
	{
		int N;
		double temp;
		vector<double> s1, s2;
		cin >> N;
		
		int score1=0, score2=0;
		for (int i=0; i<N; i++)
		{
			cin >> temp;
			s1.push_back(temp);
		}
		for (int i=0; i<N; i++)
		{
			cin >> temp;
			s2.push_back(temp);
		}
		
		sort(s1.begin(), s1.end());
		sort(s2.begin(), s2.end());
		
		vector<double> S1=s1, S2=s2;
		for (int i=0; i<s1.size(); i++)
		{
			double a=s1[i];
			//cout << "A " << a << " " << s1[i] << endl;
			bool found=false;
			for (int j=0; j<s2.size(); j++)
			{
				if (s2[j]>s1[i])
				{
					s2.erase(s2.begin()+j);
					score1++;
					found=true;
					break;
				}
			}
			if (!found)
			{
				s2.erase(s2.begin());
			}
		}

		for (int i=0; i<S2.size(); i++)
		{
			double B=S2[i];
			for (int j=0; j<S1.size(); j++)
			{
				if (S1[j] > S2[i])
				{
					S1.erase(S1.begin()+j);
					score2++;
					break;
				}
			}
		}
		
		printf("Case #%d: %d %d\n", t, score2, N-score1);
	}
}
