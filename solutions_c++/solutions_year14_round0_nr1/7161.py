#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <math.h>
#include <limits.h>
using namespace std;

class MagicCards
{
	private:
		int	FirstSelectRow[4];
		int SecondSelectRow[4];
		int SameCardCount;
		int SameCard;
		//vector<int> ThirdRow[4];
		//vector<int> FourthRow[4];
		void CompareCards()
		{
			this->SameCardCount = 0;
			
			for( int i=0; i<4; i++ )
			{
				for( int j=0; j<4; j++ )
				{
					if( FirstSelectRow[i] == SecondSelectRow[j] )
					{
						this->SameCard = FirstSelectRow[i];
						this->SameCardCount++;
					}
				}
			}
		}
	public:
		void InputFirstCards( int firstcol, int secondcol, int thirdcol, int fourthcol )
		{
			this->FirstSelectRow[0] = firstcol;
			this->FirstSelectRow[1] = secondcol;
			this->FirstSelectRow[2] = thirdcol;
			this->FirstSelectRow[3] = fourthcol;
		}
		void InputSecondCards( int firstcol, int secondcol, int thirdcol, int fourthcol )
		{
			this->SecondSelectRow[0] = firstcol;
			this->SecondSelectRow[1] = secondcol;
			this->SecondSelectRow[2] = thirdcol;
			this->SecondSelectRow[3] = fourthcol;
			
			this->CompareCards();
		}
		int SameCardNum( void )
		{
			return this->SameCardCount;
		}
		int OutputSameCard( void )
		{
			return this->SameCard;
		}
};

int main( int argc, char** argv )
{
	ifstream myfile;
	int CaseNum;
	int WhatRow;
	int FirstCol, SecondCol, ThirdCol, FourthCol;
	
	MagicCards cards;
		
	myfile.open( argv[1] );
	
	if( myfile.is_open() )
	{
		myfile >> CaseNum;
		
		for( int i=0; i<CaseNum; i++ )
		{
			myfile >> WhatRow;
			//cout << "WhatRow: " << WhatRow << endl;
			
			for( int j=0; j<4; j++ )
			{
				myfile >> FirstCol >> SecondCol >> ThirdCol >> FourthCol;
				//cout << FirstCol << ", " << SecondCol << ", " << ThirdCol << ", " << FourthCol << endl;
				
				if( j == WhatRow-1 )
				{
					cards.InputFirstCards( FirstCol, SecondCol, ThirdCol, FourthCol );
				}
			}
			
			myfile >> WhatRow;
			//cout << "WhatRow: " << WhatRow << endl;
			
			for( int j=0; j<4; j++ )
			{
				myfile >> FirstCol >> SecondCol >> ThirdCol >> FourthCol;
				//cout << FirstCol << ", " << SecondCol << ", " << ThirdCol << ", " << FourthCol << endl;
				
				if( j == WhatRow-1 )
				{
					cards.InputSecondCards( FirstCol, SecondCol, ThirdCol, FourthCol );
				}
			}
			
			if( cards.SameCardNum() == 1 )
				cout << "Case #" << i+1 << ": " << cards.OutputSameCard() << endl;
			else if( cards.SameCardNum() == 0 )
				cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
			else if( cards.SameCardNum() > 1 )
				cout << "Case #" << i+1 << ": Bad magician!" << endl;
		}
	}
	
	myfile.close();
	return 0;
}
