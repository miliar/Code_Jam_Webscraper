#include <fstream>
#include <string>
#include <iomanip>
#include <iostream>

using namespace std;

double c,f,x;
unsigned int farmsCount;

bool buy(double currentCookies)
{
	double with, without;
	without = (x - currentCookies)/(2.0 + farmsCount * f);
	with = (x - currentCookies + c) / (2.0 +(farmsCount + 1) * f);
	return ((with < without)? true:false);
}	

int main()
{
	ifstream ins("input.in");
	ofstream outs("output.out");
	size_t casesCount;
	ins >> casesCount;
	char* temp = new char[100];
	for (size_t caseNo = 1; caseNo <= casesCount; caseNo++)
	{
		outs <<"Case #" << caseNo << ": ";
		ins >> c >> f >> x;
		farmsCount = 0;
		double elapsedTime = 0.0;
		if(x < c)
		{
			outs << (x/2.0) << endl;
			continue;
		}
		while(true)
		{
			elapsedTime += c / (2.0 + farmsCount * f);
			if(buy(c))
			{
				farmsCount++;
			}
			else
			{
				break;
			}
		}
		elapsedTime += (x - c)/(2.0 + farmsCount * f);
		sprintf(temp, "%.7f", elapsedTime);
		outs << temp << endl;
	}
	
	delete []temp;
	ins.close();
	outs.close();
	return 0;
}