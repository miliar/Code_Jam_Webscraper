#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int numCases = 0;
	cin >> numCases;
	for (int a = 0; a < numCases; a++)
	{
		int fAns = 0;
		int sAns = 0;
		int Ans = 0;
		int element;
		cin >> fAns;
		int** fArrange = new int*[4];
		int** sArrange = new int*[4];
		for (int i = 0; i < 4; i++)
		{
			fArrange[i] = new int[4];
			sArrange[i] = new int[4];
		}
		vector<int> first;
		vector<int> second;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (i == fAns-1)
				{
					cin >> fArrange[i][j];
					first.push_back(fArrange[i][j]);
					/*cin >> element;
					fArrange[i].push_back(element);
					first.push_back(element);*/
				}
				else
				{
					cin >> fArrange[i][j];
					/*cin >> element;
					fArrange[i].push_back(element);*/
				} 
			}
		}
		cin >> sAns;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (i == sAns - 1)
				{
					cin >> sArrange[i][j];
					second.push_back(sArrange[i][j]);
					/*cin >> element;
					sArrange[i].push_back(element);
					second.push_back(element);*/
				}
				else
				{
					cin >> sArrange[i][j];
					/*cin >> element;
					sArrange[i].push_back(element);*/
				} 
			}
		}
		/*for (int i = 0; i < 4; i++)
		{
			cout << "value of first: " << i << first[i] << endl;
			cout << "value of second: " << i << second[i] << endl;
			/*for (int j = 0; j < 4; j++)
			{
				cout << "value of fArrange " << fArrange[i][j] << endl;
				cout << "value of sArrange " << sArrange[i][j] << endl;
			}
		}*/
		int matched = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (first[i] == second[j])
				{
					Ans = first[i];
					matched++;
				}
			}
		}
		if (matched == 1)
			cout << "Case #" << a+1 << ": " << Ans << endl;
		else if (matched > 1)
			cout << "Case #" << a+1 << ": " << "Bad Magician!" << endl;
		else if (matched == 0)
			cout << "Case #" << a+1 << ": " << "Volunteer Cheated!" << endl;
		for (int i = 0; i < 4; i++)
		{
			delete[] sArrange[i];
			delete[] fArrange[i];
		}
		delete[] sArrange;
		delete[] fArrange;
	}
	return 0;

}
