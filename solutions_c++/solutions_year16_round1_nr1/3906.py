#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int testcase;
	ifstream inp;
	inp.open("input.txt");
	ofstream out;
	out.open("output.txt");
	string str;
	inp>>testcase;
	int caseInd=0;
	int i,j;
	for (caseInd = 1; caseInd <= testcase ; caseInd ++)
	{
		out<< "Case #"<<caseInd<<": ";
		inp>>str;
		string stTmp1 = "";
		string stTmp2 = "";
		string stRet = "";
		stRet = stRet + str[0];
		for (i=1;i<str.length();i++)
		{
			if (str[i] >= stRet[0])
			{
				stRet = str[i] + stRet; 
			}
			else
			{
				stRet = stRet + str[i];
			}
			
		}
		out<<stRet<<endl;
	}
	
	inp.close();
	out.close();
	
	return 0;
	
}
