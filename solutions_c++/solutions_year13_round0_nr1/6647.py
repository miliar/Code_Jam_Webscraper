#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main()
{	
	ifstream infile;
	ofstream myfile;
	myfile.open("output.txt");

	string input;
	vector <string> test;
	int n;
	int x_row = 0, o_row=0, dots = 0, x_col =0, o_col =0, x_diag = 0, o_diag = 0;
	infile.open("A-large.in");
	getline (infile,input);
	//scanf(input.c_str(), "%d", &n);
	n = atoi(input.c_str());
	//cin>>n;

	for(int k=1; k<(n+1); k++)
	{
		dots = 0;
		bool flag = true;
		for(int i=0; i<4; i++)
		{
			//cin>>input;
			getline (infile,input);
			test.push_back(input);
		}

		for(int i=0; i<4; i++)
		{
			int count = 0;
			x_row = 0, o_row=0, x_col =0, o_col=0, x_diag = 0, o_diag = 0;
			for(int j=0; j<4; j++)
			{
				if(test[i][j]=='X')
					x_row++;
				else
					if(test[i][j] == 'T')
					{
						x_row++; o_row++;
					}
					else
					if(test[i][j]=='O')
						o_row++;
					else
						dots++;

				if(test[j][i]=='X')
					x_col++;
				else
					if(test[j][i] == 'T')
					{
						x_col++; o_col++;
					}
					else
					if(test[j][i]=='O')
						o_col++;
					else
						dots++;

				if(i==0)
				{
					if(test[i+count][j]=='X')
					x_diag++;
					else
						if(test[i+count][j] == 'T')
						{
							x_diag++; o_diag++;
						}
						else
							if(test[i+count][j]=='O')
								o_diag++;
							else
								dots++;
					count++;
				}

				if(i==3)
				{
					if(test[j][i-count]=='X') 
					x_diag++;
					else
						if( test[j][i-count] == 'T')
						{
							x_diag++; o_diag++;
						}
						else
							if(test[j][i-count]=='O')
								o_diag++;
							else
								dots++;
					count++;
				}
			}

			if(x_row == 4 || x_col == 4 || x_diag == 4)
			{
				//cout<<"X Won"<<endl;
				myfile<<"Case #"<< k <<": "<< "X won"<<endl;
				flag = false;
				break;
			}
			else
				if(o_row == 4 || o_col == 4 || o_diag == 4)
				{
					//cout<<"O Won"<<endl;
					myfile<<"Case #"<< k <<": "<< "O won"<<endl;
					flag = false;
					break;
				}
		}	
		if(flag)
		{
			if(dots == 0)
				myfile<<"Case #"<< k <<": "<< "Draw"<<endl;
				//cout<<"Draw"<<endl;
			else
				myfile<<"Case #"<< k <<": "<< "Game has not completed"<<endl;
				//cout<<"Game has not completed"<<endl;
		}
		test.clear();
		getline (infile,input);
	}

	infile.close();
	myfile.close();
	return 0;
}
