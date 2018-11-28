#include <iostream>
#include <conio.h>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <sstream>
#include <iomanip>
#include <algorithm> 
#define LARGE
using namespace std;

void main()
{
#ifdef SMALL
	freopen("C:\\sample\\CodeJam\\A-small-attempt0.in","rt",stdin);
	freopen("C:\\sample\\CodeJam\\A-small.out","wt",stdout);
#else
	freopen("C:\\sample\\CodeJam\\Qualification\\Magician\\A-small-attempt0.in","rt",stdin);
	freopen("C:\\sample\\CodeJam\\Qualification\\Magician\\A-small-attempt0.out","wt",stdout);
#endif
	
	int numTestCases;
	cin>>numTestCases;
	//bool gameWonFlag = false, fullFlag = true;
	//string myString[4];
	for(int y = 0 ; y < numTestCases; y++)
	{
		//gameWonFlag = false; fullFlag = true;
		int choiceA, choiceB, result;
		int a[4][4], b[4][4];
		bool found = false, multiple = false;
		cin>>choiceA;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> a[i][j];
			}
		}
		cin>>choiceB;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> b[i][j];
			}
		}
		--choiceA; --choiceB;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(a[choiceA][i] == b[choiceB][j])
				{
					if(found == false)
					{
						found = true;
						result = a[choiceA][i];
					}
					else
					{
						multiple = true;
					}
				}
			}
		}
		if(!found)
		{
			cout<<"\nCase #"<<y+1<<": Volunteer cheated!";
		}
		else if(multiple)
		{
			cout<<"\nCase #"<<y+1<<": Bad magician!";
		}
		else
		{
			cout<<"\nCase #"<<y+1<<": "<<result;
		}
		
	}
}

