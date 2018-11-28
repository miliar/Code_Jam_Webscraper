// GCJ_2016_QR_B.cpp : Defines the entry point for the console application.
//

// GCJ_2016_QR_A.cpp : Defines the entry point for the console application.
//




#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;

int _count = 0;

void F(string & s)
{
	//cout << "IN" << endl;
	char sign = s[0];
	int i = 1;
	while (i < s.size() && s[i] == sign)
	{
		++i;
	}

	if (i == s.size() )
	{
		
		if(sign == '-')
			++_count;
		return;
	}

	if (sign == '-')
	{
		for (int j = 0;j < i;++j)
			s[j] = '+';
	}
	else if (sign == '+')
	{
		for (int j = 0;j < i;++j)
			s[j] = '-';
	}
	++_count;

	return F(s);
}


int main()
{

	

	ifstream in("B-large.in");
	ofstream out("result.txt");



	int TestCount = 0;
	in >> TestCount;



	for (int TestNumber = 1; TestNumber <= TestCount; ++TestNumber)
	{

		cout << "Test # " << TestNumber << endl;

		string stack;
	
		in >> stack;

	
		_count = 0;

		if (stack.size() == 1)
		{
		
			if (stack[0] == '-')
				_count++;
		}
		
		else
			F(stack);

		out << "Case #" << TestNumber << ": " << _count << '\n';
	




	}//


	in.close();
	out.close();


	system("PAUSE");
	return 0;
}

