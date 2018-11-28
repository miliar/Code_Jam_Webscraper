#include<stdio.h>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

bool ispalindrome(int n)
{
	int n1,rev=0,rem;
	n1 = n;
	while (n > 0)
	{
		rem = n % 10;
		rev = rev * 10 + rem;
		n = n / 10; 
	}

	if (n1 == rev)
		return true;
	
	else
		return false;
	
}

int main()
{

	//int count = 0;
	vector <string> input;   //List of kuts
	vector <int> intList;

	int t;

	string line;
	ifstream theFile ("C-small-attempt2.in");
	if (theFile.is_open())
	{
		while (!theFile.eof())
		{
			getline (theFile, line); 
			string buf;
			stringstream ss(line);
			while(ss>> buf){
				intList.push_back(atoi(buf.c_str()));

			}

			//	intList.push_back(atoi(line.c_str()));

			//	count++;

		}
		theFile.close();
	}else
		cout <<"Invalid File homie!\n";


	t = intList[0];

	vector<string>::iterator itr;

	//cout <<"contents: " <<endl;
	//for(int i = 0; i < intList.size(); i++)
	//{
	//	cout <<intList[i] <<endl;
	//}

	//cout <<"Number of Test cases: " <<t << endl;



	int x = 1;
	for(int cas=1;cas<=t;cas++)
	{
		int answer=0,a,b,lo;
		float sq;

		a = intList[x];
		b = intList[x+1];

		for(int i=a;i<=b;i++)
		{
			sq = sqrt(i);lo=sq;
			if(sq==lo)
			{
				if((ispalindrome(i)==1)&&(ispalindrome(lo)==1)){answer++;}
			}
		}
		x = x+2;

		printf("Case #%d: %d\n",cas,answer);       
	}

	system("pause");
}