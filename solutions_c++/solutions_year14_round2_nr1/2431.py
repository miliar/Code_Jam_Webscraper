#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>

using namespace std;

typedef long long num;
typedef long double flt;

int main ()
{
	freopen ("in.txt", "r", stdin);
	//freopen ("out.txt", "w", stdout);

	int testCases;
	cin >> testCases;

	for (int testCase = 0; testCase < testCases; ++testCase)
	{
		cout << "Case #" << testCase+1 << ": ";

		int N;
		cin >> N;

		vector<string> strings;
		for (int i = 0; i < N; ++i)
		{
			string temp;
			cin >> temp;
			strings.push_back (temp);
		}

		//sort (strings.begin(), strings.end());
		unsigned steps = 0;

		vector<vector<pair<char, int> > > strDetails;

		for (int  i = 0; i < strings.size(); ++i)
		{
			strDetails.push_back(vector<pair<char,int>> (0));

			for (int j = 0; j < strings[i].size(); ++j)
			{
				if (j==0 || (j!=0 && strings[i][j-1]!=strings[i][j]))
				{
					strDetails[i].push_back (make_pair(strings[i][j], 1));
				}
				else
				{
					strDetails[i][strDetails[i].size()-1].second++;
				}
			}
		}

		bool won = false;

		int thisSize = strDetails[0].size();

		for (int i = 1; i < strDetails.size(); ++i)
		{
		
			unsigned thisSize = strDetails[0].size();
			if (thisSize != strDetails[i].size())
			{
				won=true;
				break;
			}
		}

		if (!won)
		for (int i = 0; i < strDetails[0].size(); ++i)
		{
			char thisChar;
			//int thisCount;
			thisChar = strDetails[0][i].first;
			//thisCount = strDetails[0][i].second%2;


			for (int j = 0; j < strDetails.size(); ++j) //for each word
			{
				if (thisChar != strDetails[j][i].first)// || thisCount != strDetails[j][i].second%2)
				{
					won=true;
					break;
				}
			}
		}

			if (won)cout << "Fegla Won\n";
			else
			{
				//vector<vector<pair<char, int> > > strDetails;

				for (int i = 0; i < strDetails[0].size(); ++i)//Go through each character column
				{
					
					double average;
					int total = 0;

					for (int j = 0; j < strDetails.size(); ++j)
					{
						total+= strDetails[j][i].second;
					}
					average = total/(double)strDetails.size();
					int averageI = ((average-(int)average)<0.5) ? (int)average:(int)average+1; //round

					
					for (int j = 0; j < strDetails.size(); ++j)
					{
						steps+= ((strDetails[j][i].second-averageI)<0)? -(strDetails[j][i].second-averageI):strDetails[j][i].second-averageI;
					}
				}
				cout<<steps<<"\n";
			}



	}

}