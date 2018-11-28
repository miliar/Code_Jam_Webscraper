#include<iostream>
#include<vector>
#include<fstream>
#include <iomanip>
using namespace std;
int main()
{
	char* inputFile = "B-small-attempt0.in";
	char* ouputFile = "outB.txt";
	ifstream cin(inputFile);
	ofstream cout(ouputFile);
	int caseNum = 0;
	double C, F, X, resultC, resultX, result;
	cin >> caseNum;
	for(int i = 0; i < caseNum; i++)
	{
		cin >> C >> F >> X;
		int j = 0;
		resultC = 0;
		resultX = 0;
		result = X / 2;
		while(true)
		{
			j++;
			double temp = C / (2 + F * (j - 1));
			resultC = resultC + temp;
			resultX = X / (2 + F * j);
			if(resultC + resultX < result)
				result = resultC + resultX;
			else
			{
				printf("Case #");
				printf("%d",i+1);
				printf(": ");
				printf("%.7lf",result);
				printf("\n");
				break;
			}
		}
	}
	return 0;
}
