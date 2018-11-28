#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ofstream fsout("result.txt");

	int number1[4][4],number2[4][4];

	string solution[100];			//restore the output

	int caseTime = 0;
	cin>>caseTime;
	for (int times = 0;times < caseTime;times++)
	{

		int solution1 = 0,solution2 = 0;
		int answer = -1; //0
		int cases = 0;  //0 means bad job,1 means solution,>1 means multiple

		cin>>solution1;
		for (int row = 0;row < 4;row++)
			for (int column = 0;column < 4;column++)
			{
				cin>>number1[row][column];
			}

		cin>>solution2;
		for (int row = 0;row < 4;row++)
			for (int column = 0;column < 4;column++)
			{
				cin>>number2[row][column];
			}

			for (int i = 0;i < 4;i++)
			{
				for (int j =0;j < 4;j++)
				{
					if (number1[solution1-1][i] == number2[solution2-1][j])
					{
						answer = number1[solution1-1][i];
						cases++;
					}
				}
			}

			if (cases == 0)
			{
				char temp[10];
				itoa(times+1,temp,10);
				solution[times] = "Case #"+ (string)temp +": Volunteer cheated!";
			}
			else if (cases == 1)
			{
				char temp[10],temp2[10];
				itoa(times+1,temp,10);
				itoa(answer,temp2,10);
				solution[times] = "Case #"+ (string)temp +": "+(string)temp2;
			}
			else
			{
				char temp[10];
				itoa(times+1,temp,10);
				solution[times] = "Case #"+ (string)temp +": Bad magician!";
			}
	}

	for (int i = 0;i < caseTime;i++)
	{
		fsout<<solution[i]<<endl;
	}

	fsout.close();
	return 0;
}