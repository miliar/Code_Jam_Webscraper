#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <string>
#include "decnum.h"
#include <set>
#include <vector>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("C-small.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("C-small.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	//string lib[] = {"3","212","11211","111111111"}; //possible lib
	set<decnum, less<decnum>> FnSNums; // init nums single digit
	FnSNums.insert(pow(decnum(1),2)); 
	FnSNums.insert(pow(decnum(2),2)); 
	FnSNums.insert(pow(decnum(3),2)); 
	vector<string> FnSlib; // c^2的和小于10
	FnSlib.push_back("11"); 
	FnSlib.push_back("22");
	FnSlib.push_back("101");
	FnSlib.push_back("111");
	FnSlib.push_back("121");
	FnSlib.push_back("202");
	FnSlib.push_back("212");
	FnSlib.push_back("1111");
	FnSlib.push_back("11011");
	FnSlib.push_back("11111");
	FnSlib.push_back("11211");
	FnSlib.push_back("111111");
	FnSlib.push_back("1110111");
	FnSlib.push_back("1111111");
	FnSlib.push_back("11111111");
	FnSlib.push_back("111101111");
	FnSlib.push_back("111111111");
  	for (int i = 0; i < FnSlib.size(); i++)
	{
		string lib_str = FnSlib[i];
		FnSNums.insert(pow(decnum(lib_str.c_str(), lib_str.length()),2));
	}

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		// find number of fair and square numbers greater or equal to A and smaller or equal than B.
		string A, B; // A and B - the endpoints of the interval Little John is looking at
		//输入
		inFile >> A >> B;
		decnum decA(A.c_str(), A.length()), decB(B.c_str(), B.length());
		//decnum rootA = root(decA,2), rootB = root(decB, 2);
		//操作区
		set<decnum, less<decnum>> resultNum(FnSNums.lower_bound(decA), FnSNums.upper_bound(decB));
		//输出
		outFile << "Case #" << i+1 << ": " << resultNum.size() << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}