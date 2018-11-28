#include <cstdlib>
#include <iostream>
#include <math.h>
#include <stack>
#include <fstream>
#include <string>
using namespace std;



int main()
{
	ifstream myfile;
	myfile.open("B-large.in");
	ofstream yourfile;
	yourfile.open("revenge.txt");
	int T, count, caseN;
	string txt;
	char temp;
	myfile >> T;
	caseN = 1;
	while (T>0)
	{
		myfile >> txt;
		count = 1;
		temp = txt[0];
		
		for (int i = 0; i < txt.length(); ++i)
		{
			if (txt[i] != temp)
			{
				count++;
				temp = txt[i];
			}
		}
		if (temp == '+')
		{
			yourfile << "Case #" << caseN << ": " << count - 1 << endl;
		}
		else 
			yourfile << "Case #" << caseN << ": " << count << endl;
		caseN++;
		T--;
	}
	
	return 0;
}