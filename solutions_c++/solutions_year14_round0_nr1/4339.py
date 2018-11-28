#include<iostream>
#include<string.h>
#include<fstream>

using namespace std;

void main()
{
	int dashBoard[4][4],reArrangedDashBoard[4][4] , testcases=0, first_answer, second_answer, input , testCount=0 , count=0;

	ifstream fin("A-small-attempt1.in");
	ofstream fout("outputfile.txt");
	fin>>testcases;

	while (testCount!=testcases)
	{
		testCount++;
		fin>>first_answer;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				fin>>input;
				dashBoard[i][j]=input;
			}

			fin>>second_answer;

			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					fin>>input;
					reArrangedDashBoard[i][j]=input;
				}
				int i,j , found;
				
				for(i=0;i<4;i++)
				{
					for( j=0;j<4;j++)
					{
						if(dashBoard[first_answer-1][i]!=reArrangedDashBoard[second_answer-1][j])
							continue;
						else if(dashBoard[first_answer-1][i]==reArrangedDashBoard[second_answer-1][j])
						{
							count++;
							if(count==1)
								found= dashBoard[first_answer-1][i];
						}
					}
				}
				if(count==1)
				{
					fout<<"Case #"<<testCount<<": "<<found<<endl;
				}
				 else if(count>1)
				{
					fout<<"Case #"<<testCount<<":"<<" Bad magician!"<<endl;
				}
				else if(count==0)
				{
					fout<<"Case #"<<testCount<<":"<<" Volunteer cheated!"<<endl;
				}
				 count=0;
	}
}