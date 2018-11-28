#include<iostream>
#include<vector>
#include<fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("outB.txt");
	int caseNum, i, j;
	double C, F, X, resultC, resultX, result;
	cin >> caseNum;
	for(i = 0; i < caseNum; i++)
	{
		cin >> C >> F >> X;
		j = 0;
		resultC = 0;
		resultX = 0;
		result = X / 2;
		while(true)
		{
			j++;
			resultC = resultC + C / (2 + F * (j - 1));
			resultX = X / (2 + F * j);
			if(resultC + resultX < result)
				result = resultC + resultX;
			else
			{
				cout << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(7) <<result << endl;
				break;
			}
		}
	}
	
	cin >> i;
	return 0;
}
