#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <sstream>

using namespace std;

class Pali
{
private:
	double start, finish;
	bool isPali(double num);


public:
	void getLimit();
	int countPalis();

};


void Pali::getLimit()
{
	cin >> start >> finish;

}


bool Pali::isPali(double num)
{
	string test = "";
	stringstream mySt;
	if (fmod(num, 1) != 0)
		return false;
	mySt << num;
	test = mySt.str();
	int len = test.length();

	for (int i = 0, k = len-1; i < len/2; i++, k--)
	{
		if (test[i] != test[k])
			return false;
	}
	return true;
}

int Pali::countPalis()
{
	int counter = 0;
	for (int i = (int)start; i <= (int)finish; i++)
	{
		if (fmod(start, 10) == 1 || fmod(start, 10) == 4 || fmod(start, 10) == 5 || fmod(start, 10) == 6 ||fmod(start, 10) == 9  )
			if (isPali(start) && isPali(sqrt(start)))
			{
				counter++;
			}
		start++;
	}
	return counter;
}

int main()
{
	int numOfCases;
	Pali* cases;

	cin >> numOfCases;
	cases = new Pali[numOfCases];

	for (int i = 0; i < numOfCases; i++)
	{
		cases[i].getLimit();
	}

	for (int i = 0; i < numOfCases; i++)
	{
		cout << "Case #" << i+1 << ": " << cases[i].countPalis() << endl;
		
	}
}


