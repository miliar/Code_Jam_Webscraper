//Code Jam 2015 Qualifier
//Dijkstra

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char quatMultiply(char quat1, char quat2, bool &isNegative);

int main(void)
{
	int t, l, x;
	ifstream fin;
	ofstream fout;
	string input;
	char quatProduct;

	fin.open("C-small-attempt0.in");
	fout.open("output.txt");

	fin >> t;

	for (int a = 1; a <= t; a++)
	{
		bool isNegative = 0;
		fin >> l >> x >> input;
		
		quatProduct = '1';
		
		for (int b = 0; b < x; b++)					//find product of entire input
		{
			for (int c = 0; c < l; c++)
			{
				quatProduct = quatMultiply(quatProduct, input[c], isNegative);
			}			
		}
		bool isMaybe = ((quatProduct == '1') && isNegative == true);
		if (!isMaybe)/*~((quatProduct == '1') && (isNegative == true)))*/		//if product != -1, it cannot simplifly to ijk, so NO
		{
			fout << "Case #" << a << ": " << "NO\n";
			continue;
		}

		quatProduct = '1';
		isNegative = 0;
		bool isI = 0;
		bool isJ = 0;

		for (int b = 0; b < x; b++)							//check if i, then j
		{
			for (int c = 0; c < l; c++)
			{
				quatProduct = quatMultiply(quatProduct, input[c], isNegative);
				if (isI == 0 && quatProduct == 'i' && isNegative == 0)
				{
					isI = true;
					quatProduct = '1';
				}
				else if (isI == 1 && isJ == 0 && quatProduct == 'j' && isNegative == 0)
				{
					fout << "Case #" << a << ": " << "YES\n";
					isJ = true;
				}
			}
			if (isI == 1 && isJ == 1)
				break;
		}
		if (!(isI == 1 && isJ == 1))
			fout << "Case #" << a << ": " << "NO\n";
	}


	return 0;
}

char quatMultiply(char quat1, char quat2, bool &isNegative)
{
	int index1, index2;
	char quatProduct; 
	char quatTable[4][4] =			//table for quaternion product
	{
		{ '1', 'i', 'j', 'k' },
		{ 'i', '1', 'k', 'j' },
		{ 'j', 'k', '1', 'i' },
		{ 'k', 'j', 'i', '1' }
	};

	bool quatIsNegative[4][4] =		//table for whether quaternion is negative
	{
		{ 0, 0, 0, 0 },
		{ 0, 1, 0, 1 },
		{ 0, 1, 1, 0 },
		{ 0, 0, 1, 1 },
	};
	
	if (quat1 == '1')
		index1 = 0;
	else if (quat1 == 'i')
		index1 = 1;
	else if (quat1 == 'j')
		index1 = 2;
	else index1 = 3;

	if (quat2 == '1')
		index2 = 0;
	else if (quat2 == 'i')
		index2 = 1;
	else if (quat2 == 'j')
		index2 = 2;
	else index2 = 3;

	/*
	switch (quat1)
	{
	case '1': index1 = 0;
	case 'i': index1 = 1;
	case 'j': index1 = 2;
	case 'k': index1 = 3;
	}
	switch (quat2)
	{
	case '1': index2 = 0;
	case 'i': index2 = 1;
	case 'j': index2 = 2;
	case 'k': index2 = 3;
	}
	*/
	quatProduct = quatTable[index1][index2];
	isNegative = (isNegative ^ quatIsNegative[index1][index2]);
	
	return quatProduct;
}