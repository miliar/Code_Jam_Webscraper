#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <ostream>
#include <sstream>
using namespace std;

bool checkPal(double a, double b)
{
	ostringstream t1;
    t1 << a;
    string test1 = t1.str();
	int one = test1.length() / 2;
	
	ostringstream t2;
    t2 << b;
    string test2 = t2.str();
	int two = test2.length() / 2;

	for(int i = 0; i < one; i++)
	{
		if(test1.at(0) != test1.at(test1.length() - 1 - i))
			return false;
	}

	for(int i = 0; i < two; i++)
	{
		if(test2.at(0) != test2.at(test2.length() - 1 - i))
			return false;
	}
	return true;
}

void testSet(double start, double end)
{
	int count = 0;
	double check = 0;
	for(double i = start; i <= end; i++)
	{
		check = sqrt(i);
		if(check == floor(check))
		{
			if(checkPal(i, check))
				count++;
		}
	}

	cout << count;
}

int main(int argc, char *argv[])
{
	ifstream input;
	input.open(argv[1]);
	if(!input.is_open())
	{
		cout << "Error Opening";
		return 0;
	}
	double start, end;
	int total;
	input >> total;
	for(int count = 0; count < total; count++)
	{
		input >> start;
		input >> end;
		cout << "Case #" << count + 1 << ": ";
		testSet(start, end);
		cout << endl;
	}
	
}