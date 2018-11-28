#include <fstream>
#include <string>
#include <cmath>
#include <map>
#include <sstream>

using namespace std;


int main(void)
{
	ifstream input("C-small-attempt0.in");
	ofstream output("output.out");
	string len;
	getline(input,len);
	int numCases = atoi(len.c_str());
	string s1,s2,numString;
	int a,b,cnt;
	double m;
	map<int,bool> calc;
	bool square;
	for (int i = 0; i < numCases; i++)
	{
		cnt = 0;
		getline(input,s1);
		a = atoi(s1.substr(0,s1.find(' ')).c_str());
		s1 = s1.substr(s1.find(' ')+1);
		b = atoi(s1.c_str());
		for (int j = a ; j <= b; j++)
		{
			square = true;
			if (!calc.count(j))
			{
				ostringstream convert;
				convert << j;
				numString = convert.str();
				if (numString != string(numString.rbegin(),numString.rend()))
				{
					calc[j] = false;
					square = false;
					continue;
				}
				m = sqrt((double)j);
				ostringstream convert2;
				convert2 << m;
				numString = convert2.str(); 
				if (numString != string(numString.rbegin(),numString.rend()))
				{
					calc[j] = false;
					square = false;
					continue;
				}
				if (square)
				{
					calc[j] = true;
					cnt++;
				}
				else 
				{
					calc[j] = false;
				}
			}
			else 
			{
				if (calc[j])
					cnt++;
			}
		}
		output << "Case #" << i+1 << ": " << cnt << endl;
	}
	input.close();
	output.close();
	return 0;
}
