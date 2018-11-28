#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int x;
	int answer;
	int noofcases;
	int rowselection1;
	int rowselection2;
	bool row1 = false;
	bool row2 = false;
	bool row3 = false;
	bool row4 = false;
	vector<int> vectorofint;


	ifstream infile;
	infile.open ("test.in");

	while(infile>>x)
	{
		vectorofint.push_back(x);
	}
	
	infile.close();

	noofcases = vectorofint[0];
	vectorofint.erase(vectorofint.begin());

	ofstream outfile;
	outfile.open("output.txt");

	for(int i = 0; i < noofcases; i++)
	{
		row1 = false;
		row2 = false;
		row3 = false;
		row4 = false;
		rowselection1 = vectorofint[0];
		rowselection2 = vectorofint[17];
		vectorofint.erase(vectorofint.begin()+17);
		vectorofint.erase(vectorofint.begin());
		
		if( rowselection2 == 4 )
		{
			vectorofint.erase(vectorofint.begin()+16,vectorofint.begin()+28);
		}
			else if ( rowselection2 == 3 )
			{
				vectorofint.erase(vectorofint.begin()+28,vectorofint.begin()+32);
				vectorofint.erase(vectorofint.begin()+16,vectorofint.begin()+24);
			}
				else if( rowselection2 == 2)
				{
					vectorofint.erase(vectorofint.begin()+24,vectorofint.begin()+32);
					vectorofint.erase(vectorofint.begin()+16,vectorofint.begin()+20);
				}
					else
					{
						vectorofint.erase(vectorofint.begin()+20,vectorofint.begin()+32);
					}

		if( rowselection1 == 4 )
		{
			vectorofint.erase(vectorofint.begin(),vectorofint.begin()+12);
		}
			else if( rowselection1 == 3 )
			{
				vectorofint.erase(vectorofint.begin()+12,vectorofint.begin()+16);
				vectorofint.erase(vectorofint.begin(),vectorofint.begin()+8);
			}
				else if( rowselection1 == 2 )
				{
					vectorofint.erase(vectorofint.begin()+8,vectorofint.begin()+16);
					vectorofint.erase(vectorofint.begin(),vectorofint.begin()+4);
				}
					else
					{
						vectorofint.erase(vectorofint.begin()+4,vectorofint.begin()+16);
					}

		if ( vectorofint[0] == vectorofint[4] )
		{
			row1 = true;
			answer = vectorofint[0];
		}
			else if ( vectorofint[0] == vectorofint[5] )
			{
				row1 = true;
				answer = vectorofint[0];
			}
				else if ( vectorofint[0] == vectorofint[6] )
				{
					row1 = true;
					answer = vectorofint[0];
				}
					else if ( vectorofint[0] == vectorofint[7] )
					{
						row1 = true;
						answer = vectorofint[0];
					}

		if ( vectorofint[1] == vectorofint[4] )
		{
			row2 = true;
			answer = vectorofint[1];
		}
			else if ( vectorofint[1] == vectorofint[5] )
			{
				row2 = true;
				answer = vectorofint[1];
			}
				else if ( vectorofint[1] == vectorofint[6] )
				{
					row2 = true;
					answer = vectorofint[1];
				}
					else if ( vectorofint[1] == vectorofint[7] )
					{
						row2 = true;
						answer = vectorofint[1];
					}

		if ( vectorofint[2] == vectorofint[4] )
		{
			row3 = true;
			answer = vectorofint[2];
		}
			else if ( vectorofint[2] == vectorofint[5] )
			{
				row3 = true;
				answer = vectorofint[2];
			}
				else if ( vectorofint[2] == vectorofint[6] )
				{
					row3 = true;
					answer = vectorofint[2];
				}
					else if ( vectorofint[2] == vectorofint[7] )
					{
						row3 = true;
						answer = vectorofint[2];
					}

		if ( vectorofint[3] == vectorofint[4] )
		{
			row4 = true;
			answer = vectorofint[3];
		}
			else if ( vectorofint[3] == vectorofint[5] )
			{
				row4 = true;
				answer = vectorofint[3];
			}
				else if ( vectorofint[3] == vectorofint[6] )
				{
					row4 = true;
					answer = vectorofint[3];
				}
					else if ( vectorofint[3] == vectorofint[7] )
					{
						row4 = true;
						answer = vectorofint[3];
					}

		if( row1==false && row2 == false && row3 ==false && row4 == false )
		{
			outfile << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
		else if ( ( row1 == true && row2 == true ) || ( row1 == true && row3 == true ) || ( row1 == true && row4 == true ) || ( row2 == true && row3 == true ) || ( row2 == true && row4 == true ) || ( row3 == true && row4 == true ) )
		{
			outfile << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
		else
		{
			outfile << "Case #" << i + 1 << ": " << answer << endl;
		}

		vectorofint.erase(vectorofint.begin(), vectorofint.begin()+8);
	}

	outfile.close();

	return 0;
}