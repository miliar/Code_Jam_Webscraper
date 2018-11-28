#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++)
	{
		int n;
		cin >> n;

		string temp;
		getline(cin, temp);

		bool fegla_won = false;

		string *strings = new string[n];
		for(int j = 0; j < n; j++)
		{
			getline(cin, strings[j]);
		}

		string *process = new string[n];
		vector<int> *countarray = new vector<int>[n];
		for(int j = 0; j < n; j++)
		{
			process[j] = strings[j][0];
			int count = 1;
			for(int k = 1; k < strings[j].length(); k++)
			{
				if(process[j][process[j].length() - 1] == strings[j][k])
				{
					count++;
				}
				else
				{
					process[j] += strings[j][k];
					countarray[j].push_back(count);
					count = 1;
				}
			}
			countarray[j].push_back(count);
		}

		for(int j = 1; j < n; j++)
		{
			if(process[0].length() != process[j].length() || process[0].compare(process[j]) != 0)
			{
				fegla_won = true;
				break;
			}
		}

		cout << "Case #" << (i + 1) << ": ";
		if(fegla_won)
		{
			cout << "Fegla Won";
		}
		else
		{
			vector<int> sumarray (process[0].length(), 0);
		    	vector<int> avgarray;
			for(int j = 0; j < n; j++)
			{
				for(int k = 0; k < process[0].length(); k++)
				{
					sumarray[k] += countarray[j][k];
				}
			}

			for(int k = 0; k < process[0].length(); k++)
			{
				avgarray.push_back(round(float(sumarray[k])/float(n)));
			}

			int count = 0;
			for(int j = 0; j < n; j++)
			{
				for(int k = 0; k < process[0].length(); k++)
				{
					count += abs(avgarray[k] - countarray[j][k]);
				}
			}
			cout << count;
		}
		cout << endl;
		delete[] countarray;
		delete[] process;
		delete[] strings;
	}
	return 0;
}
