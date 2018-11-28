#include <iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<sstream>
using namespace std;

int main()
{	
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	string Num = "";
	stringstream stream;
	int arr[10] = { 0,1,2,3,4,5,6,7,8,9 };
	int Counter = 0;
	int Mul = 1;
	int testCases;
	int x;
	in >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		stream.str("");
		Counter = 0;
		Mul = 1;
		in >> x;
		if (x == 0)
		{
			out << "Case #" << i+1 << ": INSOMNIA";
			if (i != testCases - 1)
				out << endl;
			continue;
		}
		
		while (Counter < 10)
		{
			stream.str("");
			Num = "";
			stream << x* Mul;
			Num = stream.str();
			for (int i = 0; i < Num.length(); i++)
			{
				if (arr[Num[i]-'0'] == Num[i] - '0')
				{
					Counter++;
					arr[Num[i] - '0'] = -1;
					continue;
				}
				if (Counter == 10)
					break;
			}
			Mul++;
			if (Counter == 10)
				break;
		}
		out << "Case #" << i +1<< ": " << Num;
		if (i != testCases - 1)
			out << endl;
		for (int i = 0; i < 10; i++)
		{
			arr[i] = i;
		}
	}
	
	return 0;
}
