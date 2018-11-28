#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include "decnum.h"

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("A-small.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("A-small.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//输入
		char t[40], r[40];
		inFile >> r >> t;
		string tStr = t, rStr= r;
		//操作区
		decnum blackPaint(tStr.c_str(), tStr.length()), radius(rStr.c_str(), rStr.length());

		decnum k = (root(pow((radius*2-1), 2)+blackPaint*8, 2)-(radius*2-1))/4;

		//输出
		outFile << "Case #" << i+1 << ": " << k << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}