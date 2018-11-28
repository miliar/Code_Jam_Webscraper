#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
void main()
{
	char words;
	int testCasesNumber;
	int caseNumber=0;
	int XrTOl=0;
	int XlTOr=0;
	int Xrows=0;
	int XColumn=0;
	int OrTOl=0;
	int OlTOr=0;
	int Orows=0;
	int OColumn=0;
	int dotNumber=0;
	int Xwon=0;
	int Owon=0;
	string line;
	char matrix[4][4];
	ifstream infile ("A-large.in");
	ofstream outfile ("A-large.out");
	if(infile.is_open())
	{

		infile >> testCasesNumber;
		for (int u=0;u<testCasesNumber;u++)
		{
			caseNumber++;
			int j=0;
			for(int m=0;m<4;m++)
			{
				infile >> line;
				for (int i=0; i < line.length(); i++)
				{
					matrix[j][i]=line[i];
				}
				j++;
			}
			//Begin ALGO
			//[1] CHECK DIAGONAL From Left to Right

			for(int i=0;i<4;i++)
			{
				if(matrix[i][i]=='X')
					XlTOr++;
				else if(matrix[i][i]=='O')
					OlTOr++;
				else if(matrix[i][i]=='T')
				{
					XlTOr++;
					OlTOr++;
				}
			}
			if(XlTOr==4)
				Xwon++;
			else if(OlTOr==4)
				Owon++;
			//[2] CHECK DIAGONAL From RIGHT to LEFT
			for(int i=0;i<4;i++)
			{
				if(matrix[i][3-i]=='X')
					XrTOl++;
				else if(matrix[i][3-i]=='O')
					OrTOl++;
				else if(matrix[i][3-i]=='T')
				{
					XrTOl++;
					OrTOl++;
				}
			}
			if(XrTOl==4)
				Xwon++;
			else if(OrTOl==4)
				Owon++;
			//[3] CHECK ROWS
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					if(matrix[i][j]=='X')
						Xrows++;
					else if(matrix[i][j]=='O')
						Orows++;
					else if(matrix[i][j]=='T')
					{
						Xrows++;
						Orows++;
					}
				}
				if(Xrows==4)
					Xwon++;
				else if(Orows==4)
					Owon++;
				Xrows=0;
				Orows=0;
			}
			

			//[4] CHECK COULUMN
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					if(matrix[j][i]=='X')
						XColumn++;
					else if(matrix[j][i]=='O')
						OColumn++;
					else if(matrix[j][i]=='T')
					{
						XColumn++;
						OColumn++;
					}
					else{
						dotNumber++;
					}
				}
				if(XColumn==4)
					Xwon++;
				else if(OColumn==4)
					Owon++;
				XColumn=0;
				OColumn=0;
			}
			if(outfile.is_open())
			{

				outfile<<"Case #"<<caseNumber<<": ";
				if(Xwon==1 && Owon==1)
				{
					outfile<<"Draw"<<endl;
				}
				else if(Xwon>=1)
					outfile<<"X won"<<endl;
				else if(Owon>=1)
					outfile<<"O won"<<endl;
				else if(dotNumber)
					outfile<<"Game has not completed"<<endl;
				else
					outfile<<"Draw"<<endl;
			}
			else cout << "Unable to open file";
			XrTOl= XlTOr= Xrows= XColumn= OrTOl= OlTOr= Orows= OColumn= Xwon= Owon=dotNumber=0;
		}
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file"; 
}